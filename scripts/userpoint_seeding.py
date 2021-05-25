#=====================================================================================================================================
# Title			 : userpoint_seeding.py
# Description    : The program calls the API for userpoints seeding for CSC retailer
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-04-08
# Version        : 1.0
# Python version : 3.7.3
#=====================================================================================================================================

import pandas as pd
import json
import requests
from datetime import datetime
import sys
import uuid
import time
import os
import csv




############################################ The below values are hardcoded and will be changed in prod ########################################

# Please Change the log directory #
log_dir="/Users/capgemini/logs"

api_auth_token="Basic U2Vzc2lvbk1JbnRlcm5hbDo4MGNmZmM1MTNhZGM4NzFkZDQyYzJmMDVmY2NmNTcxMQ=="
headers={"Content-type": "application/json; charset=UTF-8","Authorization": api_auth_token}
retailer_id="97870248-AA40-4D69-9764-594CFC81FF1A"
url_standupmode_on="https://domains-csc.ent-sessionm.com/incentives/api/1.0/retailer_standup/enable_standup_mode"
url_standupmode_off="https://domains-csc.ent-sessionm.com/incentives/api/1.0/retailer_standup/set_standup_mode_expiration_for_retailer"
url_userpoints_seeding="https://domains-csc.ent-sessionm.com/incentives/api/1.0/retailer_standup/seed_point_issuance_logs"
point_source_id="A7170E7F-DD97-4A84-AAF6-08F70E682DE2"
point_account_id="503AC641-06DC-4229-8863-01DC2831FE4F"
input_file=sys.argv[1]
##################################################################################################################################################

def api_call_standup_mode_on(url_standupmode_on,retailer_id,headers):
	""" This function will call API to switch on the standup mode for CSC client """
	try:
		payload= {
				    "requesting_retailer_id": retailer_id,
					"target_retailer_id": retailer_id
			     }
		
		response = requests.post(url_standupmode_on,data=json.dumps(payload),headers=headers)

		# getting status code and response json for applying further logic
		status_code=response.status_code
		data= response.json()

		return status_code,data

	except Exception as e:
		print('Program failed while calling API to switch on standup mode :',e)


def api_call_standup_mode_off(url_standupmode_off,retailer_id,headers):
	""" This function will call API to switch off the standup mode for CSC client """
	try:
		now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
		now=now[:-3].replace(' ','T')+'Z'
		payload={
					"requesting_retailer_id": retailer_id,
					"target_retailer_id": retailer_id,
					"expiration_date_utc": now
				}

		response = requests.post(url_standupmode_off,data=json.dumps(payload),headers=headers)

		# getting status code and response json for applying further logic
		status_code=response.status_code
		data= response.json()

		return status_code,data

	except Exception as e:
		print('Program failed while calling API to switch off standup mode :',e)


def api_call_user_points(userid,points,headers):
	""" The below function calls the API for seeding userpoints as part of one-off """
	try:
		guid=str(uuid.uuid4())
		guid_mod_ent_id=str(uuid.uuid4())
		now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
		now=now[:-3].replace(' ','T')+'Z'

		payload={
				  "requesting_retailer_id":retailer_id,
				  "request_id":guid,
				  "point_issuance_logs_batch":[
				    {
				      "retailer_id":retailer_id,
				      "user_id":userid,
				      "amount":points,
				      "time_of_occurrence":now,
				      "point_source_id":point_source_id,
				      "point_account_id":point_account_id,
				      "modification_type":"User Point Balance Migration CSC",
				      "modification_entity_id": guid_mod_ent_id
				    }
				  ]
				}
		
		response = requests.post(url_userpoints_seeding,data=json.dumps(payload),headers=headers)

		# getting status code and response json for applying further logic
		status_code=response.status_code
		data= response.json()

		return userid,points,status_code,data
	
	except Exception as e:
		print('Program failed while calling Userpoints seeding API:',e)

def main(argv=None):
	""" Program execution starts from this function """
	try:

		df=pd.read_csv(input_file)

		file_name=os.path.basename(input_file)
		
		#df.drop(['external_id_secondary'], axis = 1,inplace=True)

		status_standupmode_on,data_standupmode_on=api_call_standup_mode_on(url_standupmode_on,retailer_id,headers)
		
		if status_standupmode_on==200 and data_standupmode_on['status']=='ok' and data_standupmode_on['payload']['success']==True:
			print('Standup mode switched ON successfully!')
			print('Executing the userpoints seeding ...')

			userid_list=[]
			points_list=[]
			status_code_list=[]
			response_data_list=[]

			# Calling the below function for point adjustment for eligible customers
			count=0
			for _,row in df.iterrows():
				csv_writer_list=[]
				userid,points,status_code,data=api_call_user_points(row["user_id"], row["point_balance"],headers)
				userid_list.append(userid)
				points_list.append(points)
				status_code_list.append(status_code)
				response_data_list.append(data)
				count+=1
				print("Customer record {} processed".format(count))

				csv_writer_list.extend([userid,points,status_code,data])

				# Writing each record in log file

				# Please Change the log directory #
				with open(r'/Users/capgemini/logs/pointseeding_logs.csv', 'a') as f:
				    writer = csv.writer(f)
				    writer.writerow(csv_writer_list)

		else:
			print('Standup mode not switched ON. Check the below response from API:\n',status_standupmode_on,data_standupmode_on)
			sys.exit(1)

		status_standupmode_off,data_standupmode_off=api_call_standup_mode_off(url_standupmode_off,retailer_id,headers)
		
		if status_standupmode_off==200 and data_standupmode_off['status']=='ok' and data_standupmode_off['payload']['success']==True:
			print('Standup mode switched OFF successfully!')
		else:
			print('Standup mode not switched OFF. Check the below response from API:\n',status_standupmode_off,data_standupmode_off)
		
	except Exception as e:
		print('Program failed with the error :',e)


if __name__=="__main__":
	print('='*10,'Userpoints seeding process started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*10)
	main()
	print('='*10,'Userpoints seeding process ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*10)