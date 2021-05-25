#============================================================================================================================
# Title			 : retry_logic_pepcoin.py
# Description    : The program performs the below tasks :-
#				 	a) Checks the failure table for the users and send to API for point deduction.
# 					b) Once the points are deducted the entry for that user will be deleted from failure table
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-02-05
# Version        : 1.0
# Python version : 3.7.3
#============================================================================================================================

import sys
import os
import pandas as pd
import time
import pymssql
from datetime import datetime
import pymysql
import requests
import json
import logging
import configparser
from cryptography.fernet import Fernet
from pandas.io import sql
from sqlalchemy import create_engine

# the below import needs to be removed in prod. We will not be using pyodbc
import pyodbc

# Setting variables (hardcoding)
config_file="/opt/nifi/data/processor_input/pepcoin/config/pepcoin_config.ini"
log_dir="/opt/nifi/data/processor_input/pepcoin/logs"
download_dir="/opt/nifi/data/processor_input/pepcoin/downloads/"



def get_configuration(config_file_path,section):
	""" This function is used to get all the configuration from config file which is required to run the program """
	try:
		cf=configparser.SafeConfigParser()
		cf.read(config_file_path)
		return cf[section].values()

	except Exception as e:
		print('Program failed with the error :',e)


def decrypt_pwd(enc_text,key):
	""" This function is used for password decryption """
	try:
		f = Fernet(key)
		decrypted_text=f.decrypt(enc_text).decode('utf-8')
		return decrypted_text
	except Exception as e:
		print(e)
		raise e


def create_mysql_connection(host,user,password,db):
	""" This function is used to create connection to mysql database """
	try:
		con = pymysql.connect(host=host,user=user,password=password,db=db)
		return con

	except Exception as e:
		logger.error('Program failed with the below exception while creating connection to mysql database.\n',e)
		print('Program failed with the below exception while creating connection to mysql database :',e)
		sys.exit(1)


def create_mssql_connection(server,port,user,password,database):
	""" This function is used to create connection to mssql server database """
	try:
		#con=pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+ password)
		con=pymssql.connect(server=server,port=port,user=user,password=password,database=database)
		return con

	except Exception as e:
		logger.error('Program failed with the below exception while creating connection to mssql database.\n',e)
		print('Program failed with the below exception while creating connection to mssql database :',e)
		sys.exit(1)

def create_csv_dump(mysqlhost,mysqluser,mysqlpassword,mysqldb):
	""" This function will generate a csv containing details about the users whose points are deducted today """ 
	try:
		mysqlconn=create_mysql_connection(mysqlhost,mysqluser,mysqlpassword,mysqldb)

		query="""select * from temp_30days_already_debited_users where date_format(insertdatetime,'%Y%m%d') = date_format(sysdate(),'%Y%m%d')"""
		
		result_filename=download_dir+"points_deduction_details_{0}.csv".format(datetime.now().strftime("%Y%m%d"))
		
		results = pd.read_sql_query(query, mysqlconn)
		
		results.to_csv(result_filename, index=False)

		logger.info("User data with points deduction details are written in csv file inside downloads folder")
		print("User data with points deduction details are written in csv file inside downloads folder")
		
		mysqlconn.close()

	except Exception as e:
		logger.error ("ERROR: An error occured while writing user data with points deduction details in csv file")
		print("ERROR : An error occured while writing user data with points deduction details in csv file",e)



def deduct_point_api(userid,url,headers,mssqlserver,mssqlport,mssqluser,mssqlpassword,mssqldatabase):
	""" This function will call the api , deduct the points for the users and will return the userids once the operatiom is successful """
	try:
		'''
		 Default points to be deducted will be 25.
		 If the points are not sufficient then get the points from incentive table for that user and deduct the exact points 
		'''

		points=25 # default points
		# the below is hardcoded and will be changed based on environment
		payload = {
					"retailer_id": "F68C89D4-8476-4386-A976-D5069ED3590F",
					"spends": [{
						"retailer_id": "F68C89D4-8476-4386-A976-D5069ED3590F",
				            "user_id": userid, # this is the userid substituted via dataframe passed in function
						"spend_details": [{
							"amount": points,
							"point_account_ids": ["6B58E711-A192-41C9-9E70-EA01C419FD40"],
							"reference_id": "Rolling_Campaign_Spend_Multiple",
							"reference_type": "INCENT.Outcomes",
							"force_spend": "false",
							"rank": 0,
							"is_return": "false"
						}],
						"allow_partial_success": "false",
						"culture": "en-US"
					}],
					"culture": "en-US"
				}


		response = requests.post(url,data=json.dumps(payload),headers=headers)

		# getting status code and response json for applying further logic
		status_code=response.status_code
		data= response.json()

		############# Below is the logic to deduct points if the points are less than 25 ###############

		if status_code==400 and data['errors']['errors'][0]['code']=='insufficient_points':
			print('-----> Inside the block where response code is 400 due to insufficient points in the user account')
			
			# checking user points in incentive db and and deduct the exact points
			mssqlcon=create_mssql_connection(mssqlserver,mssqlport,mssqluser,mssqlpassword,mssqldatabase)
			
			# this is hardcoded and needs to be changed in stg and prod accordingly
			query="""SELECT  AvailableBalance  FROM [INCENT].[UserPointAccounts]  (nolock) where retailerid = 'F68C89D4-8476-4386-A976-D5069ED3590F' and userid=?"""
			
			params = [userid]
			
			cursor=mssqlcon.cursor()
			
			cursor.execute(query,params)
			
			user_points=int(cursor.fetchone()[0])

			print('-----> User points from incentive db:',user_points)
			
			cursor.close()
			
			mssqlcon.close()

			# calling API with new points
			if user_points !=0:
			# the below is hardcoded and will be changed based on the environment
				payload = {
						"retailer_id": "F68C89D4-8476-4386-A976-D5069ED3590F",
						"spends": [{
							"retailer_id": "F68C89D4-8476-4386-A976-D5069ED3590F",
					            "user_id": userid, # this is the userid substituted via dataframe passed in function
							"spend_details": [{
								"amount": user_points,
								"point_account_ids": ["6B58E711-A192-41C9-9E70-EA01C419FD40"],
								"reference_id": "Rolling_Campaign_Spend_Multiple",
								"reference_type": "INCENT.Outcomes",
								"force_spend": "false",
								"rank": 0,
								"is_return": "false"
							}],
							"allow_partial_success": "false",
							"culture": "en-US"
						}],
						"culture": "en-US"
					}

				response = requests.post(url,data=json.dumps(payload),headers=headers)

				# creating dict for creation of dataframe which needs to be returned
				data = {'userid_response_pointsdeducted': str(userid)+'_'+str(response.status_code)+'_'+str(user_points)}

				# dataframe to be returned
				df_response_data=pd.Series(data)

				# logger needs to be added here
				logger.info(df_response_data)

				return df_response_data
			
			else:
				print('-----> No points are deducted for the user as the points are already 0')
				data = {'userid_response_pointsdeducted': str(userid)+'_'+str(response.status_code)+'_'+str(user_points)}
				df_response_data=pd.Series(data)
				return df_response_data

		else:		

			# creating dict for creation of dataframe which needs to be returned
			data = {'userid_response_pointsdeducted': str(userid)+'_'+str(response.status_code)+'_'+str(points)}

			# dataframe to be returned
			df_response_data=pd.Series(data)

			# logger needs to be added here
			logger.info(df_response_data)

			return df_response_data

	except Exception as e:
		logger.error('An error occured while hitting the API endpoint:',e)
		print('An error occured while hitting the API endpoint:',e)




def retry_logic(mysqluser,mysqlpassword,mysqlhost,mysqldb,mysqlconn,url,headers,mssqlserver,mssqlport,mssqluser,mssqlpassword,mssqldatabase):
	try:
		query="""select distinct(userid) from greyhound_integration_pepsi_addon_point_expiration.temp_point_deduction_failure"""
		

		df_user_ids = pd.read_sql_query(query, mysqlconn)

		if not df_user_ids['userid'].empty:		
			print('Calling API for point deduction')
			logger.info('Calling API for point deduction')

			df_response_data=df_user_ids['userid'].apply(deduct_point_api,args=(url,headers,mssqlserver,mssqlport,mssqluser,mssqlpassword,mssqldatabase))

			df_final_data=pd.DataFrame(columns=['userid','response','pointsdeducted'])

			df_final_data[['userid','response','pointsdeducted']] = df_response_data.userid_response_pointsdeducted.str.split("_",expand=True,)

			# connecting using sqlalchemy to database (MYSQL)
			mysql_conn_string='mysql://'+mysqluser+':'+mysqlpassword+'@'+mysqlhost+'/'+mysqldb

			engine = create_engine(mysql_conn_string)

			with engine.connect() as conn, conn.begin():
				df_final_data[df_final_data['response']=='200'][['userid','pointsdeducted']].to_sql('temp_30days_already_debited_users', conn, if_exists='append',index=False,schema=mysqldb)

				print('Response Data from API via failure table:\n',df_final_data,'\n')
				logger.info('Below is the response data from API:')
				logger.info(df_final_data)

				if df_final_data[df_final_data['response']=='200'].empty is False:
					# deleting from the failure table if the points are deducted for the failed records during retry process
					
					logger.info('Deleting the userid from failure table as points are deducted for the below users while retrying')
					print('Deleting the userid from failure table as points are deducted for the below users while retrying')
					
					s=df_final_data[df_final_data['response']=='200']['userid']
					
					query_delete="""delete from greyhound_integration_pepsi_addon_point_expiration.temp_point_deduction_failure where userid in ({}) """.format(', '.join(map(repr, tuple(s))))

					print('Delete query: ',query_delete)
					logger.info(query_delete)
					
					cursor=mysqlconn.cursor()
					cursor.execute(query_delete)
					cursor.close()
					mysqlconn.commit()
					mysqlconn.close()

				# checking the dataframe for the users whose points are not deducted from API due to some error
				if df_final_data[df_final_data['response']!='200'].empty is False:
					
					logger.error('For the below list of users points are not deducted.Below is the json response from the API\n{0}'.format(df_final_data[df_final_data['response']!='200']))
					print('ERROR: For few users the points are not deducted. Proceeding for the rest of the users')
					
					# inserting failures in temp_point_deduction_failure table with response code except the records whose points are 0.

					df_error_data=df_final_data[df_final_data['pointsdeducted']!='0']

					df_error_data[df_error_data['response']!='200'][['userid','response']].to_sql('temp_point_deduction_failure', conn, if_exists='append',index=False,schema=mysqldb)
					
					print('Failures are inserted in temp_point_deduction_failure table')
					logger.info('Failures are inserted in temp_point_deduction_failure table')
				
				else:
					print('Insert completed in temp_30days_already_debited_users table after point deduction')
					logger.info('Insert completed in temp_30days_already_debited_users table after point deduction')

		else:
			print('No Users available in failure table temp_point_deduction_failure for point deduction')
			logger.info('No Users available in failure table temp_point_deduction_failure for point deduction')


		logger.info('Retry process completed')
	except Exception as e:
		logger.error('An error occured in retry logic function:',e)





def main(argv=None):
		""" Program execution starts from this function """

		try:
		# getting configurations from config file
			values=list(get_configuration(config_file,'PEPCOIN_CONFIG'))
			mssqlserver=values[0]
			mssqlport=values[1]
			mssqluser=values[2]
			mssql_enctext=values[3]
			mssqldatabase=values[4]
			mysqlhost=values[5]
			mysqluser=values[6]
			mysql_enctext=values[7]
			mysqldb=values[8]
			mssql_key=values[9]
			mysql_key=values[10]
			url=values[13]
			api_enctext_key=values[14]
			api_enctext=values[15]


			# below block decrypt the passwords for creating database connection
			mssql_enctext=mssql_enctext.encode('utf-8')
			mysql_enctext=mysql_enctext.encode('utf-8')
			mssql_key=mssql_key.encode('utf-8')
			mysql_key=mysql_key.encode('utf-8')
			api_enctext_key=api_enctext_key.encode('utf-8')
			api_enctext=api_enctext.encode('utf-8')

			# decrypting text
			mssqlpassword=decrypt_pwd(mssql_enctext,mssql_key)
			mysqlpassword=decrypt_pwd(mysql_enctext,mysql_key)
			api_auth_token=decrypt_pwd(api_enctext,api_enctext_key)

			headers={"Content-type": "application/json; charset=UTF-8","Authorization": api_auth_token}

			print('-'*20,'Retry logic for users point deduction program started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*20)

			# creating mysql connection
			mysqlconn=create_mysql_connection(mysqlhost,mysqluser,mysqlpassword,mysqldb)

			# calling retry logic function
			retry_logic(mysqluser,mysqlpassword,mysqlhost,mysqldb,mysqlconn,url,headers,mssqlserver,mssqlport,mssqluser,mssqlpassword,mssqldatabase)

			# calling create_csv_dump fuction for creating csv file containing details of the users whose points are deducted today
			create_csv_dump(mysqlhost,mysqluser,mysqlpassword,mysqldb)

			print('-'*20,'Retry logic for users point deduction program ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*20)

		except Exception as e:
			logger.error('Program failed with the below exception.\n',e)
			print('Program failed with the error :',e)
			sys.exit(1)



""" Creating logger for program """
log_file_name='retry_logic_pepcoin'
log_file_name +='_'+datetime.now().strftime("%Y%m%d_%H%M%S")+'.log'

file_path=log_dir+'/'+log_file_name
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler=logging.FileHandler(file_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


if __name__=="__main__":
	sys.exit(main())
