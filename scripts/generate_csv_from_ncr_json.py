#=======================================================================================================================================================================================================================
# Title          : generate_csv_from_ncr_json.py
# Description    : The program reads NCR_items.json file , performs ETL and generate items.csv, categories.csv and mappings.csv file as per V3 format.
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-08-19
# Version        : 1.0
# Python version : 3.7.3
# Command line   : python generate_csv_from_ncr_json.py --items_file /Users/capgemini/scripts/test/NCR_Items_Latest.json --output_location /Users/capgemini/scripts/test/
#=======================================================================================================================================================================================================================

import sys
import csv
import argparse
import json
import pandas as pd
from datetime import datetime

def create_parser():
	""" This function will return command line parser """
	try:
		parser=argparse.ArgumentParser(description='Script to generate csv files from NCR json files',prog='generate_csv_from_ncr_json.py')
		parser.add_argument('--items_file', dest='items_file', help='pass items filename with full path')
		parser.add_argument('--output_location', dest='output_location', help='pass items filename with full path')
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
		if not args.items_file or not args.output_location:
			parser.error('Incorrect number of arguments passed: output_location and items_file required')
		return args

	except Exception as e:
		print(e)
		raise e

def generate_items_file(item_file,output_location):
	""" This function reads the item_file and generate the items.csv file """
	try:
		item_name_list=[]
		item_id_list=[]
		item_sku_id_list=[]
		conv_none_to_null = lambda i : i or ''

		with open(item_file) as f:
			data = json.load(f)['Result']
			for items_data in data:
				#print(items_data['IsMenuItem'],items_data['IsModifier'])
				if items_data['IsMenuItem'] ==True or items_data['IsModifier'] ==True:			
					item_base_name=conv_none_to_null(items_data['Name'])

					for item_det in items_data['ItemVariations']:
						item_name='"'+item_base_name+' '+conv_none_to_null(item_det['Variation1'])+'"'
						item_id='"'+str(item_det['ExternalItemId'])+'"'
						sku_id_str='"'+'[{""type_of_id"":2,""id"":"'+item_id+'"}]"'
						item_sku_id_list.append(sku_id_str)
						item_name_list.append(item_name)
						item_id_list.append(item_id)

		# Creating pandas dataframe and rearranging the columns based on V3 spec
		df = pd.DataFrame(list(zip(item_id_list, item_name_list, item_sku_id_list)),columns =['item_id', 'name','additional_ids'])
		df.drop_duplicates(subset=['item_id'], keep='first',inplace=True)

		df['type_of_id'],df['description'],df['msrp'],df['is_modifier'],df['operation_type']=1,'','','false',0 #### change operation type from 0 to 1 when update
		df = df[['item_id', 'type_of_id', 'name', 'description', 'msrp', 'is_modifier', 'operation_type', 'additional_ids']]

		# Creating filename
		file_name = 'items_'+datetime.now().strftime('%Y%m%d%H%M%S.csv')
		
		# Writing data to csv file
		df.to_csv(output_location+file_name,header=False,index=False,quoting=csv.QUOTE_NONE,escapechar='\\')
		
		#Below used for finding duplicates during ETL based on column names
		#print(df[df.duplicated(['item_id'])].item_id)

	except Exception as e:
		print(e)
		raise e

def generate_categories_file(items_file,output_location):
	""" This function reads the item file and generate the categories.csv file """
	try:
		cat_name_list=[]
		cat_id_list=[]
		conv_none_to_null = lambda i : i or ''

		with open(items_file) as f:
			data = json.load(f)['Result']
			for records in data:
				if records['IsMenuItem'] ==True or records['IsModifier'] ==True:
					Cat_id='"'+str(conv_none_to_null(records['ItemCategoryId']))+'"'
					Cat_name='"'+conv_none_to_null(records['ItemCategoryName'])+'"'
					cat_name_list.append(Cat_name)
					cat_id_list.append(Cat_id)

		# Creating pandas dataframe and rearranging the columns based on V3 spec
		df = pd.DataFrame(list(zip(cat_id_list, cat_name_list)),columns =['category_id', 'name'])
		df.drop_duplicates(subset=['category_id'], keep='first',inplace=True)

		df['type_of_id'],df['description'],df['operation_type'],df['additional_ids']=1,'',0,'' #### change operation type from 0 to 1 when update
		df = df[['category_id', 'type_of_id', 'name', 'description', 'operation_type', 'additional_ids']]

		# Replacing "" from '' from category_id and name
		df['category_id'].replace('""','',inplace=True)
		df['name'].replace('""','',inplace=True)

		# Creating filename
		file_name = 'categories_'+datetime.now().strftime('%Y%m%d%H%M%S.csv')

		# Writing data to csv file
		df.to_csv(output_location+file_name,header=False,index=False,quoting=csv.QUOTE_NONE,escapechar='\\')
		
	except Exception as e:
		print(e)
		raise e

def generate_mappings_file(items_file,output_location):
	""" This function reads the items_file and generate the mappings.csv file """
	try:
		parent_id =[]
		child_id=[]
		is_item_rel=[]
		conv_none_to_null = lambda i : i or ''

		with open(items_file) as f:
			data = json.load(f)['Result']
			for records in data:
				if records['IsMenuItem'] ==True or records['IsModifier'] ==True:

					Cat_id='"'+str(conv_none_to_null(records['ItemCategoryId']))+'"'
					parent_id.append('""')
					child_id.append(Cat_id)
					is_item_rel.append('false')

					for items in records['ItemVariations']:
						item_id='"'+str(items['ExternalItemId'])+'"'
						child_id.append(item_id)
						parent_id.append(Cat_id)
						is_item_rel.append('true')

		# Creating pandas dataframe and rearranging the columns based on V3 spec
		df = pd.DataFrame(list(zip(parent_id, child_id, is_item_rel)),columns =['parent_id', 'child_id', 'is_item_rel'])
		df['parent_type_of_id'],df['child_type_of_id'],df['operation_type']=1,1,0 #### change operation type from 0 to 1 when update
		df = df[['parent_id', 'parent_type_of_id', 'child_id', 'child_type_of_id', 'is_item_rel', 'operation_type']]

		#print(df.groupby(['parent_id', 'child_id']).size()) # this gives the duplicate count group by parent and child id
		df.drop_duplicates(subset=['parent_id','child_id'], keep='first',inplace=True)

		# Replacing "" from '' from category_id and name
		df['parent_id'].replace('""','',inplace=True)
		df['child_id'].replace('""','',inplace=True)

		# Creating filename
		file_name = 'mappings_'+datetime.now().strftime('%Y%m%d%H%M%S.csv')

		# Writing data to csv file
		df.to_csv(output_location+file_name,header=False,index=False,quoting=csv.QUOTE_NONE,escapechar='\\')

	except Exception as e:
		print(e)
		raise e

def main(argv=None):
	""" Program execution starts from here """
	try:
		if argv is None:
			argv=sys.argv
		args= parse_args(argv[1:])

		# The below function will generate items file
		generate_items_file(args.items_file,args.output_location)
		print('Items file generated!')

		# The below function will generate categories file
		generate_categories_file(args.items_file,args.output_location)
		print('Categories file generated!')

		# The below function will generate mappings file
		generate_mappings_file(args.items_file,args.output_location)
		print('Mappings file generated!')

	except Exception as e:
		print(e)
		raise e

if __name__=="__main__":
	# ************** Important message ************** #
	print("\nIMPORTANT MESSAGE:")
	print("Once ETL file is generated , in the Items csv file remove \\ character.\n")
	# ************** Important message ************** #
	print('---- CSV generation process started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'----')
	main()
	print('---- CSV generation process completed on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'----')

