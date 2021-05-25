#=============================================================================================================================================
# Description         : The below script does the following:
#						a) Get the files from S3
#						b) Read the files and post the data to external endpoint
#						c) Log all the details about the program
#						d) Move the processed files to processed directory
#						e) Delete the log files and processed files which are older than 7 days
# Author 		      : Shobhit Bhatnagar
# Date                : 2020-11-05
# Version        	  : 1.0
# Glue Python version : 3
#=============================================================================================================================================


import sys
import json
import boto3
import copy
import requests
import pandas as pd
import awswrangler as wr
from datetime import datetime,timedelta

############################################################# Global Initialization #############################################################

# Bucket and file details
csc_bucket="sftp-enterprise-production"
csc_bucket_key="csc/downloads/api_publishing"
csc_bucket_processedfile_key="csc/downloads/api_publishing/processed_files"
glue_bucket="teams-ent-sessionm-com"
glue_bucket_log_key="integration/glue/csc/logs"
log_filename='s3://teams-ent-sessionm-com/integration/glue/csc/logs/api_publishing_'

# API details
api_auth_token="Basic ZjYwODZjNzYtOGVjMmNjZjktMDIyNzgxOGEtMWE4NzllZjc6ODljZWJhZDUtNDlmYS00YmEyLWI1ZTMtNTg1NWQxMTEwMDcx"
headers={"Content-type": "application/json; charset=UTF-8","Authorization": api_auth_token}
api_endpoint_createuser="https://csc-loyaltyapi.azurewebsites.net/api/1.0/users/created"
api_endpoint_updateuser="https://csc-loyaltyapi.azurewebsites.net/api/1.0/users/updated"
api_endpoint_transactions="https://csc-loyaltyapi.azurewebsites.net/api/1.0/users/scan"
api_endpoint_offerredemptions="https://csc-loyaltyapi.azurewebsites.net/api/1.0/users/redemption"
payload_json={
  "TotalPoints":None,
  "AvailablePoints":None,
  "Latitude":None,
  "Longitude":None,
  "TransactionID":None,
  "TransactionPoints":None,
  "TransactionKey":None,
  "RedemptionPointsSpent":None,
  "RedeemedDealID":None,
  "RedemptionDiscountAmount":None,
  "StoreID":None,
  "StoreKey":None,
  "ProfileFields":[
    {
      "AttributeName":"link",
      "Definition":None,
      "Value":None
    },
    {
      "AttributeName":"id",
      "Definition":None,
      "Value":None
    },
    {
      "AttributeName":"first_name",
      "Definition":None,
      "Value":None
    },
    {
      "AttributeName":"name",
      "Definition":None,
      "Value":None
    },
    {
      "AttributeName":"gender",
      "Definition":None,
      "Value":None
    },
    {
      "AttributeName":"last_name",
      "Definition":None,
      "Value":None
    },
    {
      "AttributeName":"email",
      "Definition":None,
      "Value":None
    },
    {
      "AttributeName":"locale",
      "Definition":None,
      "Value":"en_US"
    },
    {
      "AttributeName":"timezone",
      "Definition":None,
      "Value":None
    },
    {
      "AttributeName":"verified",
      "Definition":None,
      "Value":"1"
    }
  ],
  "ID":None,
  "UserName":None,
  "LastLoginDate":None,
  "IsEmailVerified":True,
  "EmailVerifiedDate":None,
  "IsSuspended":False,
  "SuspendedDate":None,
  "SuspensionReason":None
}

s3 = boto3.resource('s3')
log_file_pattern='api_publishing_logs'
csc_file_pattern='csc_latest'
msg_log="Log files older than 7 days are deleted from s3://teams-ent-sessionm-com/integration/glue/csc/logs/"
msg_csc_files="CSC files older than 7 days are deleted from s3://sftp-enterprise-production/csc/downloads/api_publishing/processed_files/"

###############################################################################################################################################



def get_filenames_from_S3(csc_bucket,csc_bucket_key):
	""" This function reads file from S3 """
	try:
		csc_bucket = s3.Bucket(csc_bucket)
		csc_files = [object.key for object in csc_bucket.objects.filter(Prefix=csc_bucket_key)]
		
		return csc_files

	except Exception as e:
		print("An error occured in get_filenames_from_S3 function:",e)
		raise e
		sys.exit(1)
		
		
def read_file_contents(bucket,filename):
	""" This function opens and reads the file content """
	try:
		obj = s3.Object(bucket, filename)
		data = obj.get()['Body'].read().decode('utf-8')
		json_data = json.loads(data)
		
		return json_data

	except Exception as e:
		print("An error occured in read_file_contents function:",e)
		raise e
		sys.exit(1)


def post_data_csc_api(payload,api_endpoint,headers):
	""" This function post data to CSC external endpoint """
	try:

		converted_payload=json.dumps(payload)
		#print(converted_payload)
		
		response = requests.post(api_endpoint,data=converted_payload,headers=headers)

		# getting status code and response json
		status_code=response.status_code
		api_response= json.dumps(response.json())

		return status_code,api_response,converted_payload
		
	except Exception as e:
		print("An error occured in post_data_csc_api function:",e)
		raise e
		sys.exit(1)


def write_log_data_to_S3(log_data,data_entity):
	""" This function writes data to json file and uploads on S3 bucket """
	try:
		wr.s3.to_csv(df=log_data,path=log_filename+data_entity+'_'+datetime.now().strftime("%Y%m%d%H%M%S")+'.csv',index=False)
		
	except Exception as e:
		print("An error occured in write_log_data_to_S3 function:",e)
		raise e
		sys.exit(1)


def move_file_from_S3(source_bucket,destination_key,filename):
	""" This function moves the file from one directory of S3 to another """
	try:
		actual_file=filename.split("/")[-1]
		copy_source = {'Bucket': source_bucket, 'Key':filename}
		s3.meta.client.copy(copy_source, source_bucket, destination_key+'/'+'done.'+actual_file)

		print("File copied from api_publishing directory to processed directory")

		# Deleting file from existing directory
		s3.Object(source_bucket, filename).delete()

		print("File removed from api_publishing directory")

	except Exception as e:
		print("An error occured in move_file_from_S3 function:",e)
		raise e
		sys.exit(1)


def delete_older_file(bucket_name,keys,pattern,msg):
	""" This function is used to delete files older than 7 days """
	try:
		s3 = boto3.client('s3')
		files = s3.list_objects_v2(Bucket=bucket_name,Prefix=keys)['Contents']
		old_files = [{'Key': file['Key']} for file in files if file['LastModified'] < datetime.now().astimezone() - timedelta(days=7) and pattern in file['Key']]
		#print(old_files)

		if old_files:
			s3.delete_objects(Bucket=bucket_name, Delete={'Objects': old_files})
			print("\n",msg)
		else:
			print("\nNo Older Files to delete")

	except Exception as e:
		print("An error occured in delete_older_file function:",e)
		raise e


def main():
	""" Program execution starts from here """
	try:
		print('='*5,"Glue Job Execution Started on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)
		
		# File pattern
		subs="csc_latest"
		
		# Getting filenames from S3
		data = get_filenames_from_S3(csc_bucket,csc_bucket_key)
		csc_files = list(filter(lambda x: subs in x, data))
		
		# Logic to Iterate over each file , read the file content and replace in payload , post the data and write it in a log file
		for file in csc_files:
			
			print("\nFile to process: ----->",file)
			
			# Replacing payload content with file content and keeping the other attributes as null based on type of file

			if 'offerredemptions' in file and 'done' not in file:

				############################## Offer Redemption Block ##############################

				# Reading file content
				filedata_redm=read_file_contents(csc_bucket,file)

				if filedata_redm:

					print("Processing Offer Redemption File...")

					status_code_list=[]
					response_list=[]
					payload_list=[]

					for data in filedata_redm:

						
						payload_json_redm= copy.deepcopy(payload_json)
						
						payload_json_redm['ID']=data['ID'] if data['ID']!="" else None
						payload_json_redm['StoreID']=data['StoreID'] if data['StoreID']!="" else None
						payload_json_redm['RedemptionPointsSpent']=data['RedemptionPointsSpent'] if data['RedemptionPointsSpent']!="" else None
						payload_json_redm['TotalPoints']=int(float(data['TotalPoints'])) if data['TotalPoints']!="" else 0
						payload_json_redm['AvailablePoints']=int(float(data['AvailablePoints'])) if data['AvailablePoints']!="" else 0
						payload_json_redm['RedemptionDiscountAmount']=int(float(data['RedemptionDiscountAmount'])) if data['RedemptionDiscountAmount']!="" else 0
						payload_json_redm['StoreKey']=data['StoreKey'] if data['StoreKey']!="" else None
						payload_json_redm['RedeemedDealID']=data['RedeemedDealID'] if data['RedeemedDealID']!="" else None

						#print(payload_json_redm)

						# Posting data to external endpoint and capture the response
						status_code_redm,response_redm,payload_redm=post_data_csc_api(payload_json_redm,api_endpoint_offerredemptions,headers)

						# Appending api response to create final log data
						status_code_list.append(status_code_redm)
						response_list.append(response_redm)
						payload_list.append(payload_redm)

						response_df_redm = pd.DataFrame(list(zip(status_code_list, response_list, payload_list)), columns =['status_code', 'response', 'payload'])
						
					#print(response_df_redm)
						
					# Writing response in a log file
					write_log_data_to_S3(response_df_redm,'offerredemptions')
					
					# Move the file to processed directory testing
					move_file_from_S3(csc_bucket,csc_bucket_processedfile_key,file)

				else:
					print("No Data Found in Redemption File. File Skipped and moved to processed directory")

					# Move the file to processed directory
					move_file_from_S3(csc_bucket,csc_bucket_processedfile_key,file)


				

			elif 'usercreate' in file and 'done' not in file:

				############################## User Create Block ##############################

				# Reading file content
				filedata_uc=read_file_contents(csc_bucket,file)

				if filedata_uc:


					print("Processing Create User File...")
					
					status_code_list=[]
					response_list=[]
					payload_list=[]

					for data in filedata_uc:

						payload_json_usercreate=copy.deepcopy(payload_json)

						inner_array_uc=payload_json_usercreate['ProfileFields']
						attributes_list=[]

						# outer attributes assignments
						payload_json_usercreate['ID']=data['Id'] if data['Id']!="" else None
						payload_json_usercreate['UserName']=data['UserName'] if data['UserName']!="" else None
						payload_json_usercreate['RedemptionDiscountAmount']=0

						# inner attributes assignments
						for attributes in inner_array_uc:
							if (attributes['AttributeName']) == 'name':
								attributes['Value']=data['Name'] if data['Name']!="" else None
							elif (attributes['AttributeName']) == 'id':
								attributes['Value']=data['Id'] if data['Id']!="" else None
							elif (attributes['AttributeName']) == 'first_name':
								attributes['Value']=data['First_Name'] if data['First_Name']!="" else None
							elif (attributes['AttributeName']) == 'gender':
								attributes['Value']=data['Gender'] if data['Gender']!="" else None
							elif (attributes['AttributeName']) == 'last_name':
								attributes['Value']=data['Last_Name'] if data['Last_Name']!="" else None
							elif (attributes['AttributeName']) == 'email':
								attributes['Value']=data['UserName'] if data['UserName']!="" else None
							else:
								pass

							attributes_list.append(attributes)

						# reconstructing inner array
						payload_json_usercreate['ProfileFields']=attributes_list

						#print(payload_json_usercreate)

						# Posting data to external endpoint and capture the response
						status_code_uc,response_uc,payload_uc=post_data_csc_api(payload_json_usercreate,api_endpoint_createuser,headers)
						
						# Appending api response to create final log data
						status_code_list.append(status_code_uc)
						response_list.append(response_uc)
						payload_list.append(payload_uc)

						response_df_uc = pd.DataFrame(list(zip(status_code_list, response_list, payload_list)), columns =['status_code', 'response', 'payload'])
						
					#print(response_df_uc)
						
					# Writing response in a log file
					write_log_data_to_S3(response_df_uc,'usercreate')
					
					# Move the file to processed directory
					move_file_from_S3(csc_bucket,csc_bucket_processedfile_key,file)

				else:
					print("No Data Found in User Create File. File Skipped and moved to processed directory")

					# Move the file to processed directory
					move_file_from_S3(csc_bucket,csc_bucket_processedfile_key,file)

				
			elif 'userupdate' in file and 'done' not in file:

				############################## User Update Block ##############################

				# Reading file content
				filedata_uu=read_file_contents(csc_bucket,file)

				if filedata_uu:


					print("Processing Update User File...")

					status_code_list=[]
					response_list=[]
					payload_list=[]
					
					for data in filedata_uu:
								
						payload_json_userupdate= copy.deepcopy(payload_json)

						inner_array_uu=payload_json_userupdate['ProfileFields']
						attributes_list=[]

						# outer attributes assignments
						payload_json_userupdate['ID']=data['Id'] if data['Id']!="" else None
						payload_json_userupdate['UserName']=data['UserName'] if data['UserName']!="" else None
						payload_json_userupdate['RedemptionDiscountAmount']=0

						# inner attributes assignments
						for attributes in inner_array_uu:
							if (attributes['AttributeName']) == 'name':
								attributes['Value']=data['Name'] if data['Name']!="" else None
							elif (attributes['AttributeName']) == 'id':
								attributes['Value']=data['Id'] if data['Id']!="" else None
							elif (attributes['AttributeName']) == 'first_name':
								attributes['Value']=data['First_Name'] if data['First_Name']!="" else None
							elif (attributes['AttributeName']) == 'gender':
								attributes['Value']=data['Gender'] if data['Gender']!="" else None
							elif (attributes['AttributeName']) == 'last_name':
								attributes['Value']=data['Last_Name'] if data['Last_Name']!="" else None
							elif (attributes['AttributeName']) == 'email':
								attributes['Value']=data['UserName'] if data['UserName']!="" else None
							else:
								pass

							attributes_list.append(attributes)

						# reconstructing inner array
						payload_json_userupdate['ProfileFields']=attributes_list

						#print(payload_json_userupdate)

						# Posting data to external endpoint and capture the response
						status_code_uu,response_uu,payload_uu=post_data_csc_api(payload_json_userupdate,api_endpoint_updateuser,headers)
						
						# Appending api response to create final log data
						status_code_list.append(status_code_uu)
						response_list.append(response_uu)
						payload_list.append(payload_uu)

						response_df_uu = pd.DataFrame(list(zip(status_code_list, response_list, payload_list)), columns =['status_code', 'response', 'payload'])
						
					#print(response_df_uu)
					# Writing response in a log file
					write_log_data_to_S3(response_df_uu,'userupdate')
					
					# Move the file to processed directory
					move_file_from_S3(csc_bucket,csc_bucket_processedfile_key,file)

				else:
					print("No Data Found in User Update File. File Skipped and moved to processed directory")

					# Move the file to processed directory
					move_file_from_S3(csc_bucket,csc_bucket_processedfile_key,file)
				

			elif 'transactions' in file and 'done' not in file:

				############################## Transactions Block ##############################

				# Reading file content
				filedata_tran=read_file_contents(csc_bucket,file)

				if filedata_tran:


					print("Processing Transactions File...")

					status_code_list=[]
					response_list=[]
					payload_list=[]
					
					for data in filedata_tran:

						payload_json_tran= copy.deepcopy(payload_json)
						
						payload_json_tran['ID']=data['ID'] if data['ID']!="" else None
						payload_json_tran['TransactionID']=data['TransactionID'] if data['TransactionID']!="" else None
						payload_json_tran['StoreID']=data['StoreID'] if data['StoreID']!="" else None
						payload_json_tran['StoreKey']=data['StoreKey'] if data['StoreKey']!="" else None
						payload_json_tran['TransactionKey']=data['TransactionKey'] if data['TransactionKey']!="" else None
						payload_json_tran['TotalPoints']=int(float(data['TotalPoints'])) if data['TotalPoints']!="" else 0
						payload_json_tran['AvailablePoints']=int(float(data['AvailablePoints'])) if data['AvailablePoints']!="" else 0
						payload_json_tran['RedemptionDiscountAmount']=int(float(data['RedemptionDiscountAmount'])) if data['RedemptionDiscountAmount']!="" else 0

						#print(payload_json_tran)

						# Posting data to external endpoint and capture the response
						status_code_tran,response_tran,payload_tran=post_data_csc_api(payload_json_tran,api_endpoint_transactions,headers)
						
						# Appending api response to create final log data
						status_code_list.append(status_code_tran)
						response_list.append(response_tran)
						payload_list.append(payload_tran)

						response_df_tran = pd.DataFrame(list(zip(status_code_list, response_list, payload_list)), columns =['status_code', 'response', 'payload'])			

					# Writing response in a log file
					write_log_data_to_S3(response_df_tran,'transactions')
					
					# Move the file to processed directory
					move_file_from_S3(csc_bucket,csc_bucket_processedfile_key,file)

				else:
					print("No Data Found in Transactions File. File Skipped and moved to processed directory")

					# Move the file to processed directory
					move_file_from_S3(csc_bucket,csc_bucket_processedfile_key,file)
			
			else:
				
				############################## This is to ignore "done." files present in the processed directory ##############################
				print("Ignoring this file!")
			
			#break

		# Deleting the files older than 7 days from Log and Processed directories
		delete_older_file(glue_bucket,glue_bucket_log_key,log_file_pattern,msg_log)
		delete_older_file(csc_bucket,csc_bucket_processedfile_key,csc_file_pattern,msg_csc_files)
		
		print('='*5,"Glue Job Execution Completed on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)

	except Exception as e:
		print("An error occured in main function:",e)
		raise e
		sys.exit(1)
		

if __name__=='__main__':
	main()