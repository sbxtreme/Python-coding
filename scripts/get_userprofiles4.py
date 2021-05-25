#============================================================================================
# Title			 : get_userprofiles.py
# Description    : The program get the user profiles by hitting API and write in a csv file.
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-06-23
# Client		 : Blains
# Version        : 1.0
# Python version : 3.7.3
#=============================================================================================

import sys
import csv
import json
import requests
import pandas as pd
from datetime import datetime

############################################################## Hardcodings #################################################################

log_dir="/Users/capgemini/logs"
input_file="/Users/capgemini/Downloads/Blains.PROD.Additions4.csv"
#input_file="/Users/capgemini/Downloads/test.csv"
url="https://api-blains.ent-sessionm.com/priv/v1/apps/8ec64c35d0b067936457bcbbb263d41fe8098d0b/external/users/"
api_auth_token="Basic OGVjNjRjMzVkMGIwNjc5MzY0NTdiY2JiYjI2M2Q0MWZlODA5OGQwYjo4MDkxOTJlZjU5M2Q4NGVjZGJiZmQ3ODRkYmM0OGZhODc4NDExNjYz"
host="api-blains.ent-sessionm.com"
header={"Content-type": "application/json","Authorization": api_auth_token,"Host": host}

#############################################################################################################################################


count_get_user_profile=0

def read_csv(input_file):
	'''This function reads the csv file and converts it into Pandas dataframe'''
	try:
		df=pd.read_csv(input_file)
		df.drop(['email'], axis = 1,inplace=True)
		return df
	except Exception as e:
		print('An error occured in read_csv function:',e)
		raise e

def get_user_profiles(url,header,ext_id):
	''' This function calls api to get user data using external ids '''
	try:
		url=url+str(ext_id)
		response=requests.get(url=url, headers=header)
		status_code=response.status_code
		data = response.json()

		global count_get_user_profile
		count_get_user_profile=count_get_user_profile+1
		print(count_get_user_profile)

		get_data(data,ext_id)

	except Exception as e:
		print('An error occured in get_user_profiles function:',e)
		raise e

def get_data(data,ext_id):
	try:
		print('inside get_data')


######################################## checking the json keys , if not exists assign null #################################################################

		if 'user' not in data:
			external_id,email,first_name,last_name,address,city,state,zip,phone_number=ext_id,'','','','','','','',''
		
		else:
			external_id=data['user']['external_id']


			if 'email' not in data['user']:
				email = ''
			else:
				email=data['user']['email']

			if 'phone_numbers' not in data['user']:
				phone_number = ''
			else:
				phone_number=data['user']['phone_numbers'][0]['phone_number']

			if 'first_name' not in data['user']:
				first_name = ''
			else:
				first_name=data['user']['first_name']

			if 'last_name' not in data['user']:
				last_name = ''
			else:
				last_name=data['user']['last_name']

			if 'address' not in data['user']:
				address = ''
			else:
				address=data['user']['address']
			
			if 'city' not in data['user']:
				city = ''
			else:
				city=data['user']['city']

			if 'state' not in data['user']:
				state = ''
			else:
				state=data['user']['state']

			if 'zip' not in data['user']:
				zip = ''
			else:
				zip=data['user']['zip']

###################################################################################################################################################

		lst=[[external_id,email,first_name,last_name,address,city,state,zip,phone_number]]

		df = pd.DataFrame(lst, columns =['external_id', 'email','first_name','last_name','address','city','state','zip','phone_numbers'])
		df.to_csv(log_dir+'/'+'output4.csv', encoding='utf-8', index=False,header=False,mode='a')

	except Exception as e:
		print('An error occured in get_data function:',e)
		raise e


def main(argv=None):
	try:
		df=read_csv(input_file)

		for _,row in df.iterrows():
				get_user_profiles(url,header,row["external_id"])

	except Exception as e:
		print('An error occured in main function:',e)
		raise e


if __name__=="__main__":
	print('Script started on :',datetime.now().strftime("%b %d %Y %H:%M:%S"))
	main()
	print('Script completed on:',datetime.now().strftime("%b %d %Y %H:%M:%S"))

