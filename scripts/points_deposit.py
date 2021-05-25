#====================================================================================
# Title			 : points_deposit.py
# Description    : The program reads a csv file and calls points deposit api
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-10-15
# Version        : 1.0
# Python version : 3.7.3
#=====================================================================================

import pandas as pd
import json
import requests
from datetime import datetime
import sys
import uuid
import time
import os
import csv

# Reading input csv file
input_file=sys.argv[1]

############################################ Hardcodings ########################################
log_file="/Users/capgemini/logs/pointdeposit_logs.csv"
api_auth_token="Basic U2Vzc2lvbk1fY3NjOmpkOU5mR1N0MFRoczdxbTFSQTZu"
headers={"Content-type": "application/json; charset=UTF-8","Authorization": api_auth_token}
retailer_id="97870248-AA40-4D69-9764-594CFC81FF1A"
url="https://domains-csc.ent-sessionm.com/incentives/api/1.0/user_points/deposit"
point_source_id="A7170E7F-DD97-4A84-AAF6-08F70E682DE2"
point_account_id="503AC641-06DC-4229-8863-01DC2831FE4F"
reference_type="CampaignID124-MakeGood"
##################################################################################################

def points_deposit_api(userid,points,headers):
	""" The below function calls the API for point deposit """
	try:
		guid=str(uuid.uuid4())
		payload={
				  "retailer_id":retailer_id,
				  "user_id":userid,
				  "deposit_details":[
				    {
				      "point_source_id":point_source_id,
				      "amount":points,
				      "point_account_id":point_account_id,
				      "reference_id":guid,
				      "reference_type":reference_type,
				      "rank":0
				    }
				  ],
				  "allow_partial_success":False,
				  "disable_event_publishing":False,
				  "culture":"en-US"
				}

		response = requests.post(url,data=json.dumps(payload),headers=headers)

		# getting status code and response json
		status_code=response.status_code
		data= response.json()

		return userid,points,status_code,data
	
	except Exception as e:
		print('Program failed while calling Point Deposit API: ',e)
		raise e


def main(argv=None):
	""" Program execution starts from this function """
	try:

		df=pd.read_csv(input_file)

		userid_list=[]
		points_list=[]
		status_code_list=[]
		response_data_list=[]

		# Calling the below function for point deposit for eligible customers
		count=0
		for _,row in df.iterrows():
			csv_writer_list=[]
			userid,points,status_code,data=points_deposit_api(row["user_id"], row["point_deposit"],headers)
			userid_list.append(userid)
			points_list.append(points)
			status_code_list.append(status_code)
			response_data_list.append(data)
			count+=1
			print("Point Deposit Completed for {} customer".format(count))

			csv_writer_list.extend([userid,points,status_code,data])

			# Writing each record in log file
			with open(log_file, 'a') as f:
				writer = csv.writer(f)
				writer.writerow(csv_writer_list)

	except Exception as e:
		print('Program failed while calling the main function with the error: ',e)
		raise e


if __name__=="__main__":
	print('='*10,'Point Deposit process started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*10)
	main()
	print('='*10,'Point Deposit process ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*10)
