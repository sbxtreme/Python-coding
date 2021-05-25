#=====================================================================================================================================
# Title			 : tier_qualifying.py
# Description    : The program qualifies users tiers
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-04-08
# Version        : 1.0
# Python version : 3.7.3
#=====================================================================================================================================

import requests
import pandas as pd
import csv
import json
from datetime import datetime
import sys

input_file = sys.argv[1]

############################################## Hardcodings ####################################################

log_file="/Users/capgemini/logs/tierqualifying_logs_postprod.csv"
api_auth_token="Basic U2Vzc2lvbk1fY3NjOmpkOU5mR1N0MFRoczdxbTFSQTZu"
headers={"Content-type": "application/json; charset=UTF-8","Authorization": api_auth_token}
retailer_id="97870248-AA40-4D69-9764-594CFC81FF1A"
url="https://domains-csc.ent-sessionm.com/incentives/api/1.0/movement/qualifying"

###############################################################################################################

def qualifying_tier(userid,headers):
	try:
		payload={
					"retailer_id":retailer_id,
					"user_id":userid,
					"culture":"en-US"
				}
		
		response = requests.post(url,data=json.dumps(payload),headers=headers)

		# getting status code and response
		status_code=response.status_code
		data= response.json()

		return status_code,data
	
	except Exception as e:
		print('Program failed while calling Tier Qualifying API:',e)

def main():
	try:
		df_customers=pd.read_csv(input_file)
		count=0
		for _,row in df_customers.iterrows():
			csv_writer_list=[]

			status,data=qualifying_tier(row['user_id'], headers)
			count+=1

			print("Customer record {} Tier qualified".format(count))
			
			csv_writer_list.extend([status,data])

			# Writing each record in log file
			with open(log_file, 'a') as f:
				writer = csv.writer(f)
				writer.writerow(csv_writer_list)

			#break

	except Exception as e:
		print(e)
		raise e


if __name__=="__main__":
	print('='*10,'Tier Qualifying process started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*10)
	main()
	print('='*10,'Tier Qualifying process ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*10)