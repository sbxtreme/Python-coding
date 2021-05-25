#============================================================================================================
# Description         : The below script does the following:
#						a) Get the file from S3
#						b) Read the file and perform ETL
#						c) Generate a new file based on the ETL logic and place it on s3 for smsync to pick
#                       d) Move the original file to processed directory with .done prefix
# Author 		      : Shobhit Bhatnagar
# Date                : 2021-03-11
# Glue Version        : 1.0
# Python version 	  : 3.6
#=============================================================================================================

import io
import sys
import json
import time
import boto3
import uuid
import pandas as pd
import awswrangler as wr
from datetime import datetime,timedelta


#========================================= Global Initialization ======================================================
# Bucket and file details
source_bucket="choicehotels-stg-sessionm-com"
source_bucket_key="etl/delayed_point_multiplier/"
processed_file_key="etl/delayed_point_multiplier/processed_files"
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')
source_path="choicehotels-stg-sessionm-com/etl/delayed_point_multiplier"
dest_path="choicehotels-stg-sessionm-com/etl/delayed_point_multiplier/processed_files"
smsync_path="choicehotels-stg-sessionm-com/etl/upload"
output_file_path="s3://"+smsync_path+"/new_28a955eaab718efd12f030f71ea094b458666c64_{0}_choicehotels-events_event.csv"
#=======================================================================================================================


def get_filenames_from_S3(source_bucket,source_bucket_key):
	""" This function reads file from S3 """
	try:
		source_bucket = s3.Bucket(source_bucket)
		source_files = [object.key for object in source_bucket.objects.filter(Prefix=source_bucket_key)]
		
		print("Getting file from S3")
		
		return source_files

	except Exception as e:
		print("An error occured in get_filenames_from_S3 function:",e)
		raise e
		sys.exit(1)
		
		
def read_file_contents(bucket,filename):
	""" This function opens and reads the file content """
	try:
		obj = s3_client.get_object(Bucket=bucket, Key=filename)
		initial_df = pd.read_csv(io.BytesIO(obj['Body'].read()))

		print("Reading file contents")
		
		return initial_df

	except Exception as e:
		print("An error occured in read_file_contents function:",e)
		raise e
		sys.exit(1)
		

def write_files_to_S3(data,output_file_path):
	""" This function writes data to json file and uploads on S3 bucket """
	try:
		time.sleep(1)
		output_file_path=output_file_path.format(datetime.now().strftime("%Y%m%d%H%M%S"))
		wr.s3.to_csv(df=data,path=output_file_path,index=False)
		
		print("Writing data to an output file {0} on S3".format(output_file_path))
		
	except Exception as e:
		print("An error occured in write_log_data_to_S3 function:",e)
		raise e
		sys.exit(1)
		

def move_file_from_S3(source_bucket,processed_file_key,filename):
	""" This function moves the file from one directory of S3 to another """
	try:
		actual_file=filename.split("/")[-1]
		copy_source = {'Bucket': source_bucket, 'Key':filename}
		s3.meta.client.copy(copy_source, source_bucket, processed_file_key+'/'+'done.'+actual_file)
		
		print("File copied from {0} directory to {1} directory".format(source_path,dest_path))
		
		# Deleting file from existing directory
		s3.Object(source_bucket, filename).delete()

		print("File removed from {} directory".format(source_path))

	except Exception as e:
		print("An error occured in move_file_from_S3 function:",e)
		raise e
		sys.exit(1)


def etl_data(df):
	""" the below function performs ETL on the file """
	try:
		entries_to_remove = ['external_id', 'event_name','occurred_at','transaction_id','context']
		columns_for_etl = [x for x in list(df) if x not in entries_to_remove]
		df.insert(0,'context','')

		# Logic to create context column data
		for idx, row in df.iterrows():
			context_dict={}
			for cols in columns_for_etl:
				context_dict[cols] = row[cols]

			context_row=json.dumps(context_dict)
			context_val=context_row
			df.at[idx,'context'] = context_val

		cols = df.columns.tolist()
		cols.append(cols.pop(cols.index('context')))
		df = df[cols]
		
		# Removing unwanted columns from dataframe after ETL
		df.drop(columns=[col for col in df.columns if col not in entries_to_remove], inplace=True)

		print("Performing ETL on original file")
		
		return df
		
	except Exception as e:
		print("An error occured in etl_data function:",e)
		raise e
		sys.exit(1)


def main():
    """ Program execution starts from here """
    try:
        file_pattern="stg_dpm"
        
        print('='*5,"Glue Job Execution Started on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)
        
        # Getting filenames from S3
        data = get_filenames_from_S3(source_bucket,source_bucket_key)
        #orig_filename = list(filter(lambda x: file_pattern in x, data))[0]
        
        # Checking files based on file_pattern defined above
        files_to_process=[orig_filename for orig_filename in data if not ('done.' in orig_filename ) and (file_pattern in orig_filename )]
        
        if not files_to_process:
            print("No files found with the pattern *{0}* to process".format(file_pattern))
        else:
            for orig_filename in files_to_process:
                print("\nProcessing {0} file".format(orig_filename))
                
                # Reading file content
                initial_df=read_file_contents(source_bucket,orig_filename)
                
                # Logic to create context column data
                final_df=etl_data(initial_df)
                
                # Writing file content to S3
                write_files_to_S3(final_df,output_file_path)
                
                # Move the file to processed directory
                move_file_from_S3(source_bucket,processed_file_key,orig_filename)
                
        print('='*5,"Glue Job Execution Ended   on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)
    
    except Exception as e:
        print("An error occured in main function:",e)
        raise e
        sys.exit(1)
        
if __name__=='__main__':
	main()