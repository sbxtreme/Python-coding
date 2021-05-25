#=============================================================================================================================================
# Description         : The below script does the following:
#						a) Get the data from datalake and perform ETL
#						b) Generate a fullfilment file
#						c) Log all the details about the program
#						d) Delete the log files and processed files which are older than 7 days
# Author 		      : Shobhit Bhatnagar
# Date                : 2021-03-01
# Version        	  : 1.0
# Glue Python version : 3.6
#=============================================================================================================================================

import sys
import json
import boto3
import copy
import time
import requests
import pandas as pd
import awswrangler as wr
from datetime import datetime,timedelta


################################################# Global Setting / Variables #################################################
bucket="choicehotels-stg-sessionm-com"
key="glue"
database="choicehotels_mazu_std"
query_result_location="s3://teams-stg-sessionm-com/integration/athena/choicehotels/"
output_filename=key+'/Fulfillment_elite_points_v2_'+datetime.now().strftime("%Y%m%d%H%M%S")+'.csv'
log_filename='s3://choicehotels-stg-sessionm-com/glue/logs/fulfillment_job_logs'
glue_bucket_log_key="glue/logs"
msg_log="Log files older than 7 days are deleted from s3://choicehotels-stg-sessionm-com/glue/logs/fulfillment_job_logs/"
log_file_pattern='fulfillment_job_logs'
s3 = boto3.resource('s3')
###############################################################################################################################


def get_query_status(client, query_execution_id):
	""" This function gets This query execution status in athena """
	try:
		response = client.get_query_execution(
		    QueryExecutionId=query_execution_id
		)
		
		#print(response)
		return response

	except Exception as e:
		print("An error occured in get_query_status function:",e)
		raise e
		sys.exit(1)


def format_result(results):
	""" This function format the results passed as Athena response """
	try:
		columns = [col['Label'] for col in results['ResultSet']['ResultSetMetadata']['ColumnInfo']]
		formatted_results = []
		for result in results['ResultSet']['Rows'][0:]:
			values = []
			for field in result['Data']:
				try:
					values.append(list(field.values())[0]) 
				except:
					values.append('')
			formatted_results.append(dict(zip(columns, values)))
		return formatted_results

	except Exception as e:
		print("An error occured in format_result function:",e)
		raise e
		sys.exit(1)


def execute_query(database, query, query_result_location):
	""" This function executes the SQL on athena """
	try:
		print("--> Query to Execute on Mazu:\n",query.replace("\n", " "))
		athena_client = boto3.client('athena')
		response = athena_client.start_query_execution(
		    QueryString=query,
		    QueryExecutionContext={
		        'Database': database
		    },
		    ResultConfiguration={
		        'OutputLocation': query_result_location
		    }
		)
		query_execution_id = response['QueryExecutionId']
		print("--> Query_execution_id : "  + query_execution_id)
		query_status = get_query_status(athena_client, query_execution_id)

		while query_status['QueryExecution']['Status']['State'] in ['RUNNING', 'QUEUED']:
			print("--> Query Status on Check: %s" % query_status['QueryExecution']['Status']['State'])
			time.sleep(15)
			query_status = get_query_status(athena_client, query_execution_id)

		# Changes to get more than 1000 records from athena
		marker = None
		formatted_results = []
		num_of_pages = 0

		while True:
			paginator = athena_client.get_paginator('get_query_results')
			response_iterator = paginator.paginate( 
				QueryExecutionId=query_execution_id,
				PaginationConfig={
            				'MaxItems': 1000,
            				'PageSize': 1000,
            				'StartingToken': marker})

			for page in response_iterator:
				num_of_pages+=1
				print("Page Number:",num_of_pages)
				pages_list=format_result(page)

				formatted_results.extend(pages_list)

			try:
				marker = page['NextToken']
			except KeyError:
				break

		formatted_results.pop(0)
		print("Number of records:",len(formatted_results))
		return formatted_results


	except Exception as e:
		print("An error occured in execute_query function:",e)
		raise e
		sys.exit(1)
		
		
def write_log_data_to_S3(log_data):
	""" This function writes data to json file and uploads on S3 bucket """
	try:
		wr.s3.to_csv(df=log_data,path=log_filename+'_'+datetime.now().strftime("%Y%m%d%H%M%S")+'.log',index=False)
		
	except Exception as e:
		print("An error occured in write_log_data_to_S3 function:",e)
		raise e
		sys.exit(1)


def delete_older_file(bucket_name,keys,pattern,msg):
	""" This function is used to delete files older than 7 days """
	try:
		s3 = boto3.client('s3')
		files = s3.list_objects_v2(Bucket=bucket_name,Prefix=keys)['Contents']
		old_files = [{'Key': file['Key']} for file in files if file['LastModified'] < datetime.now().astimezone() - timedelta(days=7) and pattern in file['Key']]
		#print(old_files)

		if old_files:
			s3.delete_objects(Bucket=bucket_name, Delete={'Objects': old_files})
			print("\n",msg)
		else:
			print("\nNo Older Files to delete")

	except Exception as e:
		print("An error occured in delete_older_file function:",e)
		raise e
		

def write_data_to_S3(transaction_data):
	""" This function writes data to json file and uploads on S3 bucket """
	try:
		s3=boto3.client('s3')
		uploadByteStream = bytes(json.dumps(transaction_data).encode('UTF-8'))
		s3.put_object(Bucket=bucket, Key=output_filename, Body=uploadByteStream)
		print("--> File uploaded to S3")
		
	except Exception as e:
		print("An error occured in write_data_to_S3 function:",e)
		raise e
		sys.exit(1)
		
def main():
	""" Program execution starts from here """
	try:
		print('='*5,"Glue Job Execution Started on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)
		query_for_window_data="""select
								eum.external_user_id as account_number,
								external_user_id_type as account_type,
								upt.point_modification as point_modification,
								upt.point_transaction_id as point_transaction_id,
								date_format(upt.time_of_occurrence, '%Y-%m-%dT%H:%i:%sZ') as created_at,
								cma.campaign_id as campaign_id,
								cma.starts_at as campaign_start_date,
								cma.ends_at as campaign_end_date,
								ca.achievement_id as promo_id,
								ca.name as promo_name,
								upt.reference_id as reference_id,
								upt.time_of_occurrence as time_of_occurrence,
								upt.user_id as user_id
								from user_point_transactions upt 
								inner join campaign_achievements ca on upt.reference_id=ca.external_id
								inner join external_user_mappings eum on eum.user_id=upt.user_id
								inner join point_accounts pa on pa.point_account_id= upt.point_account_id
								inner join campaign_attributes cma on cma.campaign_id=ca.ad_campaign_id
								where upt.reference_type='Behavior'
								and eum.external_user_id_type='customer_id'
								and ca.achievement_type='behavior'
								and upt.created_at >= current_date - interval '2' day -- this is used for testing. It should be below commented conditon
								-- where date(created_at) = current_date - interval '1' day 
								-- and upt.user_id='4ef53b24-3e31-11eb-8331-72468095f9cd'
								order by user_id,reference_id,time_of_occurrence"""

		query_for_stay_id="""with subquery as (
								SELECT transaction_id,achievement_id FROM campaign_activity WHERE achievement_id IN
								(
									SELECT DISTINCT(ca.achievement_id)
									FROM user_point_transactions upt INNER JOIN campaign_achievements ca
									ON upt.reference_id=ca.external_id
									WHERE upt.reference_type='Behavior'
									AND upt.data_date = Date('2020-12-14') -- this is used for testing. It should be below commented conditon
									-- AND date(created_at) = current_date - interval '1' day 
									) AND action IN ('composite:achievement:event','goal:achievement:event')
								)
								select distinct(request_id) as request_id,user_id,time_stamp from subquery sb 
								inner join campaign_event ce on upper(ce.transaction_id)= upper(sb.transaction_id)
								order by user_id,time_stamp"""

		df_window = wr.athena.read_sql_query(sql=query_for_window_data,database=database,s3_output=query_result_location)
		df_stay_id = wr.athena.read_sql_query(sql=query_for_stay_id,database=database,s3_output=query_result_location)
		
		print(df_window)
		print(df_stay_id)
		
		print('='*5,"Glue Job Execution Ended on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)


	except Exception as e:
		print(e)

if __name__== "__main__":
	main()