#========================================================================================================
# Title			 : sendgrid_global_unsubscribe.py
# Description    : The program add email ids to Sendgrid global unsubscribe list
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-11-11
# Version        : 1.0
# Python version : 3.7.3
#========================================================================================================

import sys
import csv
import requests
import json
import pandas as pd

############################################## Global Initialization ####################################################
BearerAuth="Bearer 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"
headers={"Content-type": "application/json; charset=UTF-8","Authorization": BearerAuth}
endpoint="https://api.sendgrid.com/v3/asm/suppressions/global"
filename = sys.argv[1]
log_file="/Users/capgemini/logs/sendgrid_global_unsubscribe.csv"
##########################################################################################################################


def add_in_exclusion_list(endpoint,headers,list_of_email_ids):
	try:
		payload={
                  "recipient_emails": list_of_email_ids
                }

		response = requests.post(endpoint,data=json.dumps(payload),headers=headers)

		# getting status code and response
		status_code=response.status_code
		data= response.json()

		return status_code,data
		
	except Exception as e:
		print('An error occured in add_in_exclusion_list function:',e)
		raise e

	
def main():
	try:
		log_file_list=[]

		count=0
		for df_chunk in pd.read_csv(filename,chunksize=500):
			count+=1
			email_list = list(df_chunk['email_ids'])
			status_code,response_data=add_in_exclusion_list(endpoint,headers,email_list)

			print("{} Slot of Users added in Sendgrid Exclusion list (Slot can be of 500 users or less)".format(count))
			
			log_file_list.extend([status_code,json.dumps(response_data,indent=4)])

			# Writing data in log file
			with open(log_file, 'a') as f:
				writer = csv.writer(f)
				writer.writerow(log_file_list)			
		
	except Exception as e:
		print("An error occured in main function:",e)
		raise e


if __name__=='__main__':
	main()