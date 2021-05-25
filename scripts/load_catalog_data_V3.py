#==============================================================================================================================================================================
# Title          : load_catalog_data.py
# Description    : The program performs the below tasks :-
#				    a) Reads csv files and upload to S3 bucket. 
#					b) Generate Presigned URLs for the files uploaded.
#					c) Call V3 API for catalog ingestion.
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-08-19
# Version        : 1.0
# Python version : 3.7.3
# Command line   : python load_catalog_data_V3.py --file_location /Users/capgemini/scripts/test/ --S3_bucket_location economy-stg-sessionm-com/nifi/csc-stg/ --profile stg
#==============================================================================================================================================================================

import os
import sys
import boto3
import argparse
import glob
import requests
import json
from datetime import datetime
from botocore.client import Config


#to switch on the boto3 debugger uncomment the below
#boto3.set_stream_logger('')

###################################################### Hard codings (env specific) ################################################################################
# The below is for csc stage

api_endpoint="https://domains-connecteast1.stg-sessionm.com/catalog/api/3.0/catalog/product/enqueue/ingest_product_catalog_file"
retailer_id="F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96"
headers={"Content-type": "application/json; charset=UTF-8","Authorization": "Basic U2Vzc2lvbk1fY3NjOmtiRjBmOGFBVEFQZ3FEbmZ1Mk8y"}

# The below is for csc prod

#api_endpoint="https://domains-csc.ent-sessionm.com/catalog/api/3.0/catalog/product/enqueue/ingest_product_catalog_file"
#retailer_id="97870248-AA40-4D69-9764-594CFC81FF1A"
#headers={"Content-type": "application/json; charset=UTF-8","Authorization": "Basic U2Vzc2lvbk1JbnRlcm5hbDo4MGNmZmM1MTNhZGM4NzFkZDQyYzJmMDVmY2NmNTcxMQ=="}
####################################################################################################################################################################


def create_parser():
	""" This function will return command line parser """
	try:
		parser=argparse.ArgumentParser(description='Script to load the catalog data to dynamodb using V3 endpoint',prog='load_catalog_data.py')
		parser.add_argument('--file_location', dest='file_location', help='pass the path where all the csv files reside')
		parser.add_argument('--S3_bucket_location', dest='S3_bucket_location', help='pass the S3 bucket location')
		parser.add_argument('--profile', dest='profile', help='AWS profile')
		parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
		return parser

	except Exception as e:
		print(e)
		raise e

def parse_args(arguments):
	""" This function will parse the command line arguments """
	try:
		parser=create_parser()
		args=parser.parse_args(arguments)

		''' check for mandatory parameters '''
		if not args.file_location or not args.S3_bucket_location or not args.profile:
			parser.error('Incorrect number of arguments passed: files, bucket and AWS profile required')
		return args

	except Exception as e:
		print(e)
		raise e

def upload_csv_to_S3(profile,file_location,S3_bucket_location):
	""" This function will upload the files to S3 """
	try:
		session = boto3.Session(profile_name=profile)
		s3 = session.client('s3')
		S3_bucket_key=S3_bucket_location.split("/",1)
		S3_bucket,key=S3_bucket_key[0],S3_bucket_key[1]
		files_to_load=file_location+'*.csv'
		csv_files = glob.glob(files_to_load)

		for filename in csv_files:
			key_base=''
			base=os.path.basename(filename)
			key_base=key+base
			s3.upload_file(filename, S3_bucket, key_base)
			print("Uploaded %s file into %s bucket" % (filename,S3_bucket_location))
			
		print("All Files Uploaded Successfully!")

	except Exception as e:
		print (e)
		raise e

def generate_presigned_urls(S3_bucket_location,file_location,profile):
	""" This function is used to generate the presigned URLs """
	try:
		session = boto3.Session(profile_name=profile)
		#s3 = session.client('s3')
		s3 = session.client('s3',config=Config(signature_version='s3v4'))
		S3_bucket_key=S3_bucket_location.split("/",1)
		S3_bucket,key=S3_bucket_key[0],S3_bucket_key[1]
		files_pattern=file_location+'*.csv'
		csv_files = glob.glob(files_pattern)

		files_presigned_urls=dict()

		for filename in csv_files:
			key_base=''
			base=os.path.basename(filename)
			key_base=key+base
			url = s3.generate_presigned_url(
                ClientMethod='get_object',
                Params={'Bucket': S3_bucket, 'Key': key_base, },
                #ExpiresIn=60,
                ExpiresIn=604800
            )

			files_presigned_urls[base]=url

		return files_presigned_urls

	except Exception as e:
		print(e)
		raise e

def load_catalog_data(files_presigned_urls):
	""" This function is used for calling V3 ingest API """
	try:
		# Seperating Urls based on file names
		for key in files_presigned_urls:
			if key.startswith("item"):
				url_items=files_presigned_urls[key]
			elif key.startswith("categories"):
				url_categories=files_presigned_urls[key]
			else:
				url_mappings=files_presigned_urls[key]

		# Get the file names
		key_list = list(files_presigned_urls.keys()) 
		val_list = list(files_presigned_urls.values())

		items_file=key_list[val_list.index(url_items)]
		categories_file=key_list[val_list.index(url_categories)]
		mappings_file=key_list[val_list.index(url_mappings)]

		payload= {
				    "retailer_id": retailer_id,
				    "product_catalogs": [
				        {
				            "file_grouping": 1,
				            "files": [
				            	{
				                    "url": url_items,
				                    "transfer_type": 2,
				                    "file_name": items_file,
				                    "authorization_header": None,
				                    "file_format": 1,
				                    "is_compressed": False
				                },
				                {
				                    "url": url_categories,
				                    "transfer_type": 2,
				                    "file_name": categories_file,
				                    "authorization_header": None,
				                    "file_format": 1,
				                    "is_compressed": False
				                },
				                {
				                    "url": url_mappings,
				                    "transfer_type": 2,
				                    "file_name": mappings_file,
				                    "authorization_header": None,
				                    "file_format": 1,
				                    "is_compressed": False
				                }
				            ]
				        }
				    ]
				 }

		print(payload)
		
		response = requests.post(api_endpoint,data=json.dumps(payload),headers=headers)

		# getting status code and response json for applying further logic
		status_code=response.status_code
		response_data= response.json()

		return status_code, response_data

	except Exception as e:
		print(e)
		raise e

def main(argv=None):
	""" Program execution starts from here """
	try:
		if argv is None:
			argv=sys.argv
		args= parse_args(argv[1:])

		print("\n----> Step 1: Uploading files to S3 bucket:")
		# This function will upload the csv files to S3 bucket
		upload_csv_to_S3(args.profile,args.file_location,args.S3_bucket_location)

		print("\n----> Step 2: Generating presigned Urls for the uploaded files:")
		# This function will generate presigned Urls for the files which are uploaded to S3
		files_presigned_urls=generate_presigned_urls(args.S3_bucket_location,args.file_location,args.profile)
		print("Presigned Urls Generated:\n",files_presigned_urls)

		print("\n----> Step 3: Calling V3 Catalog ingestion API to load data into Dynamodb:")
		# This function will load the catalog data using V3 endpoint
		status_code, response_data= load_catalog_data(files_presigned_urls)
		print ("Status code from Ingestion API:",status_code)
		print ("Response from Ingestion API:",response_data,"\n")

	except Exception as e:
		print(e)
		raise e

if __name__=="__main__":
	print('='*10,'Catalog ingestion process V3 started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*10)
	main()
	print('='*10,'Catalog ingestion process V3 ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*10)

