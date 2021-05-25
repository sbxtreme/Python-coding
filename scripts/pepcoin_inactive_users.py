#============================================================================================================================
# Title			 : pepcoin_inactive_users.py
# Description    : The program performs the below tasks :-
#				    a) Reads the data from MSSQL for the pepcoin users which have not made transaction in last 120 days
#					b) Store the data in MySQL temp tables
#					c) Call the API for point deduction for those users whose points have not been deducted in last 30 days
# 					d) Creates a csv file for the users whose points are deducted and place the file in downloads folder
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
from subprocess import Popen, PIPE

rundate=sys.argv[1]

print('Inside the pepcoin point deduction script and running for date:',rundate)

# this import needs to be removed as this will not be used in prod
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


def logfile_removal():
	""" This function is used to remove old log files from the server """
	try:
		cmd="find "+log_dir+" -name '*.log' -type f -mtime +7 -exec rm -f {} \;"

		p = Popen(cmd, shell=True,stdout=PIPE, stderr=PIPE)
		out, err = p.communicate()

		if not err:
			print('\tLogs older than 7 days are removed!')
		else:
			print('\tERROR occured while removing logs:\n',err)
		
	except Exception as e:
		print ('Program failed with the error while removing log files from log directory:',e)
		sys.exit(1)

def create_mssql_connection(server,port,user,password,database):
	""" This function is used to create connection to mssql server database """
	try:
		#con=pymssql.connect(server=server,port=port,user=user,password=password,database=database)
		con = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+ password)
		return con

	except Exception as e:
		logger.error('Program failed with the below exception while creating connection to mssql database.\n',e)
		print('Program failed with the below exception while creating connection to mssql database :',e)
		sys.exit(1)

def create_mysql_connection(host,user,password,db):
	""" This function is used to create connection to mysql database """
	try:
		con = pymysql.connect(host=host,user=user,password=password,db=db)
		return con

	except Exception as e:
		logger.error('Program failed with the below exception while creating connection to mysql database.\n',e)
		print('Program failed with the below exception while creating connection to mysql database :',e)
		sys.exit(1)

def deduct_point_api(userid,url,headers,mssqlserver,mssqlport,mssqluser,mssqlpassword,mssqldatabase):
	""" This function will call the api , deduct the points for the users and will return the userids once the operatiom is successful """
	try:
		'''
		 Default points to be deducted will be 25.
		 If the points are not sufficient then get the points from incentive table for that user and deduct the exact points 
		'''

		points=25 # default points
		# payload is hardcoded and will be changed in stg and prod accordingly
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
			print('       Inside the block where response code is 400 due to insufficient points in the user account')
			
			# checking user points in incentive db and and deduct the exact points
			mssqlcon=create_mssql_connection(mssqlserver,mssqlport,mssqluser,mssqlpassword,mssqldatabase)
			
			# this is hardcoded and will be changed in stg and prod accrodingly
			query="""SELECT AvailableBalance FROM [INCENT].[UserPointAccounts]  (nolock) where retailerid = 'F68C89D4-8476-4386-A976-D5069ED3590F' and userid=?"""
			
			print('       Userids for which point deduction will happen:',userid)
			params = [userid]
			
			cursor=mssqlcon.cursor()
			
			cursor.execute(query,params)
			
			user_points=int(cursor.fetchone()[0])

			print('       User points from incentive db:',user_points)
			
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
				print('       No points are deducted for the user as the points are already 0')
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



def create_csv_dump(mysqlhost,mysqluser,mysqlpassword,mysqldb):
	""" This function will generate a csv containing details about the users whose points are deducted today """ 
	try:
		mysqlconn=create_mysql_connection(mysqlhost,mysqluser,mysqlpassword,mysqldb)

		query="""select * from temp_30days_already_debited_users where date_format(insertdatetime,'%Y%m%d') = date_format(sysdate(),'%Y%m%d')"""
		
		result_filename=download_dir+"points_deduction_details_{0}.csv".format(datetime.now().strftime("%Y%m%d"))
		
		results = pd.read_sql_query(query, mysqlconn)
		
		results.to_csv(result_filename, index=False)

		logger.info("User data with points deduction details are written in csv file inside downloads folder")
		print("Step15: User data with points deduction details are written in csv file inside downloads folder")
		
		mysqlconn.close()

	except Exception as e:
		logger.error ("ERROR: An error occured while writing user data with points deduction details in csv file")
		print("ERROR : An error occured while writing user data with points deduction details in csv file",e)
		


def data_processing(mssqlserver,mssqlport,mssqluser,mssqlpassword,mssqldatabase,mysqlhost,mysqluser,mysqlpassword,mysqldb,url,headers):
	""" The below function is used for performing data processing """
	try:

		''' Below queries will be fired against DBs (MSSQL and MYSQL) '''

		# to get the transactions from mssql for pepsi retailer and get the users which have not made any transaction in last 120 days (MSSQL)
		# this is hardcoded and needs to be changed in stg and prod accordingly	
		'''
		query1="""select 
					distinct (tp1.userid)
					FROM Transactions.Transactions (Nolock) 
					join transactions.transactionpayments tp1 (Nolock)
					on tp1.transactionid = Transactions.Transactions.ID  
					where Transactions.Transactions.retailerID = 'F68C89D4-8476-4386-A976-D5069ED3590F'
					and DATEDIFF(DAY,Transactions.Transactions.SMTransactionprocessDate,GETUTCDATE()) >= 120 
					and 
					not exists 
					(
					SELECT * FROM Transactions.Transactions (Nolock) 
					join transactions.transactionpayments tp2 
					on tp2.transactionid = Transactions.Transactions.ID  
					and tp1.UserID=tp2.userID
					where Transactions.Transactions.retailerID = 'F68C89D4-8476-4386-A976-D5069ED3590F'
					and DATEDIFF(DAY,Transactions.Transactions.SMTransactionprocessDate,GETUTCDATE()) < 120)
					and userid is not null
					OPTION (USE HINT('ENABLE_PARALLEL_PLAN_PREFERENCE'));
					"""
		'''


		# The below query is used for testing and commented out the actual query1 
		# this needs to be changed to original query
		#query1=""" select 'b27c7756-57dd-11ea-820d-1a01b5b649bd' as userid union select 'a97ce220-57de-11ea-860f-f5d87e4046b9' as userid union select 'xxx' as userid""" 
		
		# the below if condition decides the query to be executed in case of date passed to the script
		if sys.argv[1] != "nodate":
			query1="""select 
					distinct (tp1.userid)
				FROM Transactions.Transactions (Nolock) 
				join transactions.transactionpayments tp1 (Nolock)
				on tp1.transactionid = Transactions.Transactions.ID  
				where Transactions.Transactions.retailerID = 'F68C89D4-8476-4386-A976-D5069ED3590F'
				and DATEDIFF(DAY,Transactions.Transactions.SMTransactionprocessDate,{0}) >= 120
				and 
				not exists 
				(
				SELECT * FROM Transactions.Transactions (Nolock) 
				join transactions.transactionpayments tp2 
				on tp2.transactionid = Transactions.Transactions.ID  
				and tp1.UserID=tp2.userID
				where Transactions.Transactions.retailerID = 'F68C89D4-8476-4386-A976-D5069ED3590F'
				and DATEDIFF(DAY,Transactions.Transactions.SMTransactionprocessDate,{0}) < 120)
				and userid is not null
				OPTION (USE HINT('ENABLE_PARALLEL_PLAN_PREFERENCE'));
				""".format("'"+rundate+"'")
		else:
			query1="""select 
					distinct (tp1.userid)
				FROM Transactions.Transactions (Nolock) 
				join transactions.transactionpayments tp1 (Nolock)
				on tp1.transactionid = Transactions.Transactions.ID  
				where Transactions.Transactions.retailerID = 'F68C89D4-8476-4386-A976-D5069ED3590F'
				and DATEDIFF(DAY,Transactions.Transactions.SMTransactionprocessDate,GETUTCDATE()) >= 120
				and 
				not exists 
				(
				SELECT * FROM Transactions.Transactions (Nolock) 
				join transactions.transactionpayments tp2 
				on tp2.transactionid = Transactions.Transactions.ID  
				and tp1.UserID=tp2.userID
				where Transactions.Transactions.retailerID = 'F68C89D4-8476-4386-A976-D5069ED3590F'
				and DATEDIFF(DAY,Transactions.Transactions.SMTransactionprocessDate,GETUTCDATE()) < 120)
				and userid is not null
				OPTION (USE HINT('ENABLE_PARALLEL_PLAN_PREFERENCE'));"""


		print('Query to be executed to get users:\n',query1,'\n')	
		
		# trancates the table before loading data pepsi user data in Mysql (MYSQL) 
		query2="""TRUNCATE TABLE temp_120days_no_purchase_users"""

		# drops index on the table for bulk load (MYSQL)
		query3="""drop index idx_userid1 ON greyhound_integration_pepsi_addon_point_expiration.temp_120days_no_purchase_users"""
		query4="""drop index idx_insertdate1 ON greyhound_integration_pepsi_addon_point_expiration.temp_120days_no_purchase_users"""

		# creates index on the table to speed up the select query firing on the table (MYSQL)
		query5="""create index idx_userid1 ON greyhound_integration_pepsi_addon_point_expiration.temp_120days_no_purchase_users (userid)"""
		query6="""create index idx_insertdate1 ON greyhound_integration_pepsi_addon_point_expiration.temp_120days_no_purchase_users (InsertDateTime)"""

		# deletes the data for the users whose points are already deducted and are older than 31 days (MYSQL)
		query7="""delete from greyhound_integration_pepsi_addon_point_expiration.temp_30days_already_debited_users where datediff(now(),insertdatetime) >=31"""

		# getting users which have not made transaction in last 120 days and whose points are not deducted in last 31 days (MYSQL)
		query8="""select userid from greyhound_integration_pepsi_addon_point_expiration.temp_120days_no_purchase_users t1 where not exists (select * from greyhound_integration_pepsi_addon_point_expiration.temp_30days_already_debited_users t2 where t1.userid = t2.userid)"""

		query9="""delete from greyhound_integration_pepsi_addon_point_expiration.temp_point_deduction_failure where datediff(insertdatetime,now()) > 0"""

		''' Query block ends '''

		# creating mssql connection
		mssqlcon=create_mssql_connection(mssqlserver,mssqlport,mssqluser,mssqlpassword,mssqldatabase)

		print('Step1: SQL SERVER Connection created')
		logger.info('Step1: SQL SERVER Connection created')

		print('Step2: Writing data to dataframe started')
		logger.info('Step2: Writing data to dataframe started')

		# the below dataframe created to store the appended results from the chunck returned by read_sql_query function
		df_userid=pd.DataFrame(columns=['userid'])

		for df_user in pd.read_sql_query(query1, mssqlcon,chunksize=20000):
			df_userid=df_userid.append(df_user)
			print('      -->Chunk Completed')
			logger.info('      -->Chunk Completed')


		print('Step3: Data written in dataframe')
		logger.info('Step3: Data written in dataframe')

		mssqlcon.close()

		print('Step4: SQL SERVER Connection closed')
		logger.info('Step4: SQL SERVER Connection closed')

		# creating mysql connection
		mysqlconn=create_mysql_connection(mysqlhost,mysqluser,mysqlpassword,mysqldb)

		print('Step5: MY SQL Connection created')
		logger.info('Step5: MY SQL Connection created')

		cursor=mysqlconn.cursor()

		cols = "`,`".join([str(i) for i in df_userid.columns.tolist()])

		print('Step6: Data insertion in temp_120days_no_purchase_users table started')
		logger.info('Step6: Data insertion in temp_120days_no_purchase_users table started')

		cursor.execute(query2)
		cursor.execute(query3)
		cursor.execute(query4)

		for i,row in df_userid.iterrows():
			sql = "INSERT INTO `temp_120days_no_purchase_users` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
			cursor.execute(sql, tuple(row))

		cursor.execute(query5)
		cursor.execute(query6)

		print('Step7: Data insertion completed')
		logger.info('Step7: Data insertion completed')

		print('Step8: Deleting data from temp_30days_already_debited_users table which is older than 31 days')
		logger.info('Step8: Deleting data from temp_30days_already_debited_users table which is older than 31 days')

		cursor.execute(query7)

		# deleting older data from failure table and keeping today's data
		cursor.execute(query9)

		mysqlconn.commit()

		print('Step9: Writing data to users points deduct dataframe started')
		logger.info('Step9: Writing data to users points deduct dataframe started')

		# the below dataframe created to store the appended results from the chunck returned by read_sql_query function
		df_userid_point_deduct=pd.DataFrame(columns=['userid'])

		for df_users_point_deduct in pd.read_sql_query(query8, mysqlconn,chunksize=20000):
			df_userid_point_deduct=df_userid_point_deduct.append(df_users_point_deduct)
			print('      -->Chunk Completed')
			logger.info('      -->Chunk Completed')

		print('Step10: Data written to users points deduct dataframe')
		logger.info('Step10: Data written to users points deduct dataframe')

		cursor.close()
		mysqlconn.close()

		################## API block start ####################

		# the below code is used for calling API , deducting points and inserting data into the table when point deduction is done

		print('Step11: Calling API to deduct points for the users')
		logger.info('Step11: Calling API to deduct points for the users')

		if not df_userid_point_deduct['userid'].empty:

			df_response_data=df_userid_point_deduct['userid'].apply(deduct_point_api,args=(url,headers,mssqlserver,mssqlport,mssqluser,mssqlpassword,mssqldatabase))

			# creating a csv file which stores users with all the response from API
			df_response_data.to_csv(log_dir+'/'+'response_from_api_{}.csv'.format(datetime.now().strftime("%Y%m%d_%H%M%S")), encoding='utf-8', index=False)


			print('Step12: Point deduction completed from the API')
			logger.info('Step12: Point deduction completed from the API')

			df_final_data=pd.DataFrame(columns=['userid','response','pointsdeducted'])
			
			#print('debugging',df_response_data)

			#print('debugging',df_response_data.userid_response_pointsdeducted.str.split("_",expand=True,))			

			df_final_data[['userid','response','pointsdeducted']] = df_response_data.userid_response_pointsdeducted.str.split("_",expand=True,)

			# connecting using sqlalchemy to database (MYSQL)
			mysql_conn_string='mysql://'+mysqluser+':'+mysqlpassword+'@'+mysqlhost+'/'+mysqldb

			engine = create_engine(mysql_conn_string)

			with engine.connect() as conn, conn.begin():

				df_final_data[df_final_data['response']=='200'][['userid','pointsdeducted']].to_sql('temp_30days_already_debited_users', conn, if_exists='append',index=False,schema=mysqldb)

				# checking the dataframe for the users whose points are not deducted from API due to some error
				if df_final_data[df_final_data['response']!='200'].empty is False:
					
					logger.error('For the below list of users points are not deducted.Below is the json response from the API\n{0}'.format(df_final_data[df_final_data['response']!='200']))
					print('ERROR: For few users the points are not deducted. Failures are inserted in temp_point_deduction_failure table. Proceeding for the rest of the users')
					
					# inserting failures in temp_point_deduction_failure table with response code except the records whose points are 0.

					df_error_data=df_final_data[df_final_data['pointsdeducted']!='0']

					df_error_data[df_error_data['response']!='200'][['userid','response']].to_sql('temp_point_deduction_failure', conn, if_exists='append',index=False,schema=mysqldb)
					
					print('Step13: Insert completed in temp_30days_already_debited_users table after point deduction for remaining users')
					logger.info('Step13: Insert completed in temp_30days_already_debited_users table after point deduction for remaining users')
				
				else:
					print('Step13: Insert completed in temp_30days_already_debited_users table after point deduction')
					logger.info('Step13: Insert completed in temp_30days_already_debited_users table after point deduction')

			################## API block close #####################

			print('Step14: MY SQL Connection closed')
			logger.info('Step14: MY SQL Connection closed')
		else:
			print('Step12: No users available for point deduction.Points are already deducted for the users in the last 31 days')
			logger.info('Step12: No users available for point deduction as the points are already deducted for the user in the last 31 days hence API not called. Check the below query for more details:\n{0}'.format(query8))


	except Exception as e:
		logger.error('Program failed with the below exception while performing data processing.\n',e)
		print('Program failed with the below exception while performing data processing :',e)



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
		log_dir=values[11]
		deletion_days=values[12]
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

		print('-'*20,'Pepcoin inactive users program started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*20)
		logger.info('Pepcoin Inactive Users program logs')

		# calling data processing function
		data_processing(mssqlserver,mssqlport,mssqluser,mssqlpassword,mssqldatabase,mysqlhost,mysqluser,mysqlpassword,mysqldb,url,headers)

		logger.info('Program completed successfully!')

		# calling create_csv_dump fuction for creating csv file containing details of the users whose points are deducted today
		create_csv_dump(mysqlhost,mysqluser,mysqlpassword,mysqldb)

		# calling logfile removal function to delete the logs older than 7 days
		logfile_removal()
		logger.info('Log files older than 7 days are removed')

		print('-'*20,'Pepcoin inactive users program ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*20)

	except Exception as e:
		logger.error('Program failed with the below exception.\n',e)
		print('Program failed with the error :',e)
		sys.exit(1)




""" Creating logger for program """
log_file_name='pepcoin_inactive_users'
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

