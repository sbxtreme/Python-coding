#======================================================================================
# Title			 : adjust_points.py
# Description    : The program adjusts the customer points based on the spreadsheet.
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-05-11
# Version        : 1.0
# Python version : 3.7.3
#=======================================================================================

import sys
import json
import requests
import pandas as pd
from datetime import datetime

############################################################## Hardcodings #################################################################

log_dir="/Users/capgemini/logs"
input_file="/Users/capgemini/Downloads/customer_data.xlsx"
get_id_url="https://api-lowes.ent-sessionm.com/priv/v1/apps/db6dc76398b2160c0f79a861232828477a98a356/external/users/"
getid_api_auth_token="Basic ZGI2ZGM3NjM5OGIyMTYwYzBmNzlhODYxMjMyODI4NDc3YTk4YTM1NjpkMmVlNTNjMzliNGY2YmQzOTgzMTA4YTU2ZWVlN2Y0NGZhZmRhMTkx"
get_id_header={"Accept":"application/json","Content-type": "application/json","Authorization": getid_api_auth_token}
userpoint_url="https://domains-connecteast1.ent-sessionm.com/incentives/api/1.0/user_points/balance"
api_auth_token="Basic U2Vzc2lvbk1JbnRlcm5hbDo4MGNmZmM1MTNhZGM4NzFkZDQyYzJmMDVmY2NmNTcxMQ=="
header={"Content-type": "application/json","Authorization": api_auth_token}
point_deposit_url="https://domains-connecteast1.ent-sessionm.com/incentives/api/1.0/user_points/deposit"

#############################################################################################################################################


def read_xls(input_file):
	'''This function reads the xls file and converts it into Pandas dataframe'''
	df=pd.read_excel(input_file)
	return df


def get_internal_id(get_id_url,ext_id,get_id_header):
	'''This function gets the internal sessionm id from the customer external id'''
	try:
		url=get_id_url+ext_id
		response=requests.get(url=url, headers=get_id_header) 
		userid=response.json()['user']['id']
		
		# creating dict for creation of dataframe which needs to be returned
		data = {'internal_id': userid}

		# dataframe to be returned as series
		df_response_data=pd.Series(data)
		
		return df_response_data

	except Exception as e:
		print('Error! Program failed while calling get_internal_id API :',e)


def get_userpoint_balance(userpoint_url,internal_id,header):
	'''This function is used to get userpoint balance for customers based on internal id'''
	try:
		payload= {
				    "retailer_id": "A479D5ED-C164-445A-A3CC-0943E370FF8C",
				    "user_id": internal_id,
				    "point_account_ids": [
				        "C663EC2A-4BE8-44D9-9F49-84E47BD4E3CA"
				    ]
				  }

		response = requests.post(userpoint_url,data=json.dumps(payload),headers=header)

		available_points= response.json()['payload']['details'][0]['available_balance']

		# creating dict for creation of dataframe which needs to be returned
		data = {'internal_points': available_points}

		# dataframe to be returned as series
		df_response_data=pd.Series(data)
		
		return df_response_data

	except Exception as e:
		print('Error! Program failed while calling get_userpoint_balance API :',e)


def valid_customers_for_adjustment(df_customer_data):
	'''This function evaluates the customer data to get valid customers for point adjustments'''
	try:

		df_customer_data['point_diff']=df_customer_data['ptd'].astype(float) - df_customer_data['internal_points'].astype(float)
		
		df_customer_data['valid_customers'] = df_customer_data.apply(lambda x: 'Y' if x.point_diff > 0 else 'N', axis=1)
		
		return df_customer_data

	except Exception as e:
		print('Error! Program failed while calling valid_customers_for_adjustment function :',e)


def adjust_points(point_deposit_url,header,internal_id,points):
	'''This function is used to deposite points for customers'''
	try:

		payload={
				    "retailer_id": "A479D5ED-C164-445A-A3CC-0943E370FF8C",
				    "user_id": internal_id,
				    "deposit_details": [
				        {
				            "amount": points,
				            "point_account_id": "C663EC2A-4BE8-44D9-9F49-84E47BD4E3CA",
				            "point_source_id": "6CCF0918-311A-4460-8FCC-11CD7D52AB25",
				            "reference_id": "Adjusted Points Deposit",
				            "reference_type": "Adjusted Points Deposit"
				        }
				    ]
				}

		response = requests.post(point_deposit_url,data=json.dumps(payload),headers=header)

		# getting status code and response json for applying further logic
		status_code=response.status_code
		response_data=response.json()
		userid=response.json()['payload']['user_id']

		return userid,status_code,response_data

	except Exception as e:
		print('Error! Program failed while calling adjust_points function :',e)
		sys.exit(1)



def main(argv=None):
	""" Program execution starts from this function """
	try:

		# Calling the below function to read the file and convert the data into pandas dataframe
		df_customer_data=read_xls(input_file)
		df_customer_data=df_customer_data[['PRO_LOY_ID','ptd']]

		print('Step1: Reading customer details file: COMPLETED')

		# Calling the below function to get SessionM internal id based on the external id
		df_response_data=df_customer_data.apply(lambda x: get_internal_id(get_id_url,x.PRO_LOY_ID,get_id_header), axis=1)
		df_customer_data=df_customer_data.assign(internal_id=df_response_data.internal_id)

		print('Step2: Getting SessionM internal customer id from external id: COMPLETED')

		# Calling the below function to get SessionM points based on the internal id
		df_response_data=df_customer_data.apply(lambda x: get_userpoint_balance(userpoint_url,x.internal_id,header),axis=1)
		df_customer_data=df_customer_data.assign(internal_points=df_response_data.internal_points)

		print('Step3: Getting available point balance for each customer: COMPLETED')

		# Calling the below function to get valid customers for point adjustments
		df_customer_data=valid_customers_for_adjustment(df_customer_data)

		print('Step4: Evaluating Customers for point adjustment: COMPLETED')

		print('\n',df_customer_data,'\n')

		df_eligible_customers=df_customer_data.loc[df_customer_data['valid_customers'] == 'Y', ['internal_id','point_diff']]

		if not df_eligible_customers.empty:

			userid_list=[]
			status_code_list=[]
			response_data_list=[]

			# Calling the below function for point adjustment for eligible customers
			for _,row in df_eligible_customers.iterrows():
				userid,status_code,response_data=adjust_points(point_deposit_url,header,row["internal_id"], row["point_diff"])
				userid_list.append(userid)
				status_code_list.append(status_code)
				response_data_list.append(response_data)

			df_api_response = pd.DataFrame(list(zip(userid_list, status_code_list, response_data_list)), columns =['user_id', 'status_code','response']) 

			print('Step5: Points awarded for eligible customers: COMPLETED')
			
			final_df=pd.merge(left=df_customer_data,right=df_api_response,left_on='internal_id',right_on='user_id',how='left')
			final_df.rename(columns = {'PRO_LOY_ID':'loyality_id'}, inplace = True)

			# Writing result data into to_csv
			final_df.to_csv(log_dir+'/'+'userpoints_adjustment_lowes{}.csv'.format(datetime.now().strftime("%Y%m%d_%H%M%S")), encoding='utf-8', index=False)

			print('Step6: Writing point details in a csv file: COMPLETED')

		else:
			print('Step5: No Point Adjustment required for any customer')

	except Exception as e:
		print('Error! Program failed with the error :',e)


if __name__=="__main__":
	print('='*10,'Userpoints adjustment process started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*10)
	main()
	print('='*10,'Userpoints adjustment process ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*10)



