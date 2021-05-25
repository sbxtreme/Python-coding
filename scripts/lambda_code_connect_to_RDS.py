#==============================================================================================================
# Description    : The below lambda function connects to Core , get the data , write and upload it to S3
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-10-24
# Version        : 1.0
# Python version : 3.7
#================================================================================================================

import sys
import pymysql
import json
import boto3
import pyodbc
from datetime import datetime


################################################# Global Setting / Variables #################################################
createuser_sql="createuser.sql"
bucket="sftp-enterprise-production"
key="csc/downloads/api_publishing"
output_filename=key+'/csc_latest_usercreate_'+datetime.now().strftime("%Y%m%d%H%M%S")+'.json'
host='core-db-csc.ent.local'
user='sessionm'
password='xYTgh8Gy6juLCd66'
db='greyhound_csc'

# the below is for testing
conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};\
			  SERVER='+'lt-app-beta-db.ent.local'+';DATABASE='+'csc'+';UID='+'loyaltree'+';PWD='+'tdYNIoC3!paMyUQV')


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


# the below is commented out for testing
'''
def create_mysql_connection(host,user,password,db):
	""" This function is used to creating connection to core database """
	try:
		con = pymysql.connect(host=host,user=user,password=password,db=db)
		return con

	except Exception as e:
		print('Program failed with the below exception while creating connection to mysql database :',e)
'''

def execute_sql(con,sql_query):
	""" This function executes SQL on core database """
	try:
		cursor=con.cursor()
		cursor.execute(sql_query)

		# getting column details for creating json structure
		keys = []

		for column in cursor.description:
			keys.append(column[0])
		key_number = len(keys)

		# getting data and converting it into json structure
		json_data = []

		for row in cursor.fetchall():
			item = dict()
			for q in range(key_number):
				item[keys[q]] = row[q]
			json_data.append(item)

		return json_data

		cursor.close()
		con.close()

	except Exception as e:
		print(e)
		raise e


def write_data_to_S3(userdata):
	""" This function writes data to json file and uploads on S3 bucket """
	try:
		s3=boto3.client('s3')
		uploadByteStream = bytes(json.dumps(userdata,indent=4).encode('UTF-8'))
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
		query = get_sql_from_file(createuser_sql)

		# the below is commented out for testing
		'''
		print("Step2: Creating connection to CSC Core database")
		con = create_mysql_connection(host,user,password,db)
		'''

		print("Step3: Executing SQL on Core to get latest users created")
		rows_returned = execute_sql(conn,query)
		
		print("Step3: Writing data in a json file on {} location".format(bucket+'/'+key))
		write_data_to_S3(rows_returned)

		print('='*5,"Lambda Execution Completed Successfully on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)

	except Exception as e:
		print(e)
		raise e