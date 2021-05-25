#====================================================================================================================================
# Description    : This below lambda function connects to Athena Mazu datalake , fires a SQL , write data to json and store in S3
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-10-22
# Version        : 1.0
# Python version : 3.8
#====================================================================================================================================

import sys
import boto3
import time
import json
from datetime import datetime

################################################# Global Setting / Variables #################################################
transactions_sqlfile="transactions.sql"
bucket="sftp-enterprise-production"
key="csc/downloads/api_publishing"
database="csc_mazu_std"
query_result_location="s3://teams-ent-sessionm-com/integration/athena/csc/"
output_filename=key+'/csc_latest_transactions_'+datetime.now().strftime("%Y%m%d%H%M%S")+'.json'
###############################################################################################################################

def get_sql_from_file(file_loc):
	""" This function gets the sql query from sql file for further execution """
	try:
		f = open(file_loc, "r")
		return f.read()

	except Exception as e:
		print("An error occured in get_sql_from_file function:",e)
		raise e
		sys.exit(1)


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


		results = athena_client.get_query_results(
		QueryExecutionId=query_execution_id,
		#MaxResults=1000
		)

		rows_returned = []
		header_rows = True
		headers = []

		for row in results["ResultSet"]["Rows"]:
			print(row)
			data_set = row["Data"]
			
			if header_rows:
				for data in data_set:
					headers.append(data["VarCharValue"])
				
				header_rows = False
			else:
				idx = 0
				each_row = {}
				for data in data_set:
					if "VarCharValue" in data:
						value=data["VarCharValue"]
					else:
						value=''

					each_row[headers[idx]] = value
					
					idx += 1
				rows_returned.append(each_row)
		
		if len(rows_returned) > 0:
			print("--> Query execution & result extraction finished")
			return rows_returned

		print("--> Query execution & result extraction finished")
		return None

	except Exception as e:
		print("An error occured in execute_query function:",e)
		raise e
		sys.exit(1)


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


def lambda_handler(event, context):
	""" Program execution starts from here """
	try:
		print('='*5,"Lambda Execution Started on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)

		print("Step1: Getting SQL Query from SQL file")
		query = get_sql_from_file(transactions_sqlfile)

		print("Step2: Executing SQL on Mazu Datalake to get latest transactions")
		rows_returned = execute_query(database,query,query_result_location)
		
		print("Step3: Writing data in a json file on {} location".format(bucket+'/'+key))
		write_data_to_S3(rows_returned)

		print('='*5,"Lambda Execution Completed Successfully on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)

	except Exception as e:
		print(e)
		raise e