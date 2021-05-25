#=====================================================================================================================================
# Title			 : replace_jsondata.py
# Description    : The program replace the storeid in json with the new ids from masterfile
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-04-01
# Version        : 1.0
# Python version : 3.7.3
#=====================================================================================================================================

import json
import pandas as pd

################################### Hardcoding ###############################################
filename='/Users/capgemini/Downloads/csc files/Catalog/catalogdata.json'
#filename='/Users/capgemini/Downloads/csc files/transactions/transaction_90days.json'
newfilename='/Users/capgemini/Downloads/csc files/Catalog/new_replacedstore_catalogdata.json'
#newfilename='/Users/capgemini/Downloads/csc files/transactions/new_transaction_90days.json'
masterfile='/Users/capgemini/Downloads/csc files/Catalog/masterfile.xlsx'
##############################################################################################

def replace_data(filename,masterfile):
	''' This function reads json and masterfile and replace the value in json from masterfile '''
	try:

		df_master = pd.read_excel(masterfile, sheet_name=0)
		master_dict = dict(zip(df_master.prod_id, df_master.stage_id))
		#print(master_dict)

		with open(filename, 'r') as file:
			json_data = json.load(file)
			for item in json_data:
				
				print('Old:New---->',item['store_id'],":",master_dict[item['store_id']])

				item['store_id']=master_dict[item['store_id']]

		with open(newfilename, 'w') as file:
			json.dump(json_data, file, indent=2)

	except KeyError:
		print('{0} value not found in the masterdict'.format())

	except Exception as e:
		raise (e)

if __name__=="__main__":
	replace_data(filename,masterfile)