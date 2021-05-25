#=======================================================================================================================================
# Title          : verify_data_V3.py
# Description    : The program performs the below tasks:
#					1. Fire the delete API to delete catalog on csc stg
#					2. Verify if all the items are deleted from the database
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-08-19
# Version        : 1.0
# Python version : 3.7.3
# Command line   : python verify_data_V3.py --item_file_location /Users/capgemini/scripts/test/ --delete_and_verify NO
#=======================================================================================================================================
import os
import sys
import json
import pandas as pd
import glob
import argparse
import requests

###################################################### Hard codings (env specific) ####################################################################################
# The below is for csc stage

api_endpoint_delete="https://domains-connecteast1.stg-sessionm.com/catalog/api/3.0/catalog/product/enqueue/delete_product_catalog"
api_endpoint_normalize="https://domains-connecteast1.stg-sessionm.com/catalog/api/3.0/catalog/product/master/normalize"
retailer_id="F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96"
headers={"Content-type": "application/json; charset=UTF-8","Authorization": "Basic U2Vzc2lvbk1fY3NjOmtiRjBmOGFBVEFQZ3FEbmZ1Mk8y"}

# The below is for csc prod

#api_endpoint_delete="https://domains-csc.ent-sessionm.com/catalog/api/3.0/catalog/product/enqueue/delete_product_catalog"
#api_endpoint_normalize="https://domains-csc.ent-sessionm.com/catalog/api/3.0/catalog/product/master/normalize"
#retailer_id="97870248-AA40-4D69-9764-594CFC81FF1A"
#headers={"Content-type": "application/json; charset=UTF-8","Authorization": "Basic U2Vzc2lvbk1JbnRlcm5hbDo4MGNmZmM1MTNhZGM4NzFkZDQyYzJmMDVmY2NmNTcxMQ=="}

########################################################################################################################################################################

def create_parser():
	""" This function will return command line parser """
	try:
		parser=argparse.ArgumentParser(description='Script to verify if the data is in dynamodb or not',prog='verify_data_V3.py')
		parser.add_argument('--item_file_location', dest='item_file_location', help='pass items filelocation with full path')
		parser.add_argument('--delete_and_verify', dest='delete_and_verify', help='this flag can be YES or NO')
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
		if not args.item_file_location or not args.delete_and_verify:
			parser.error('Incorrect number of arguments passed: output_location and delete_and_verify flag required')
		return args

	except Exception as e:
		print(e)
		raise e


def fire_delete_api():
	""" This function deletes the data from dynamodb """
	try:
		payload= {"retailer_id": retailer_id}
		response = requests.post(api_endpoint_delete,data=json.dumps(payload),headers=headers)
		
		# getting status code and response json
		status_code=response.status_code
		response_data= response.json()
		return status_code,response_data

	except Exception as e:
		print(e)
		raise e



def read_items_csv(item_file_location):
	""" This function gets all the item_ids from items.csv file """
	try:
		items_csv=glob.glob(item_file_location+'items_*.csv')
		header_list = ['item_id', 'type_of_id', 'name', 'description', 'msrp', 'is_modifier', 'operation_type', 'additional_ids']
		df_items=pd.read_csv(items_csv[0],names=header_list)
		return df_items['item_id']

	except Exception as e:
		print(e)
		raise e

def normalize_api(item_id):
	""" This function get the data from database (Dynamodb) """
	try:
		payload={
				    "retailer_id": retailer_id,
				    "catalog_type": 1,
				    "ids": [
				        {
				            "store_id": "00000000-0000-0000-0000-000000000000",
				            "type_of_id":1,
				            "id":item_id
				        }
				    ]
				}

		response = requests.post(api_endpoint_normalize,data=json.dumps(payload),headers=headers)
		response_data= response.json()
		return response_data

	except Exception as e:
		print(e)
		raise e


def main(argv=None):
	""" Program execution starts from here """
	try:
		if argv is None:
			argv=sys.argv
		args= parse_args(argv[1:])

		if args.delete_and_verify=='NO':
			# this will just verify the data

			# step1: read items csv and get item_id dataframe
			print('Step1 : Get all the item_ids from items.csv file')
			df_item_ids=read_items_csv(args.item_file_location)

			# step2: run normalize api to get the items from database after delete
			print('Step2 : Running normalize api to check the data in dynamo')
			
			count=0
			for row in df_item_ids:
				count+=1
				response_data=normalize_api(row)
				print(response_data)
				if count>=5:
					break
		else:

			# step1 : fire delete api
			print('Step1 : Firing delete API')
			status_code,response=fire_delete_api()

			if status_code==202:
				print('\t',response)
				
				# step2: read items csv and get item_id dataframe
				print('Step2 : Get all the item_ids from items.csv file')
				df_item_ids=read_items_csv(args.item_file_location)
				
				# step3: run normalize api to get the items from database after delete
				print('Step3 : Running normalize api to check the data in dynamo after deletion')
				
				count=0
				for row in df_item_ids:
					count+=1
					response_data=normalize_api(row)
					print(response_data)
					if count>=5:
						break

			else:
				print('An error occured while deleting data from Dynamodb')

	except Exception as e:
		print(e)
		raise e

if __name__=="__main__":
	sys.exit(main())
