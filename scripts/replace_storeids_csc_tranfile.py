#=====================================================================================================================================
# Title			 : replace_storeids_csc_tranfile.py
# Description    : The program replace the storeid in tran_json with the new ids from masterfile
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-04-01
# Version        : 1.0
# Python version : 3.7.3
#=====================================================================================================================================

import json
import pandas as pd

################################### Hardcoding ###############################################
filename='/Users/capgemini/Documents/new_17sep_transactions.json'
newfilename='/Users/capgemini/Documents/final/NEW_17sep_PROD_trans.json'
masterfile='/Users/capgemini/Desktop/SessionM/Work/csc/OLD_vs_NEW_storeids.csv'
##############################################################################################

def replace_data(filename,masterfile):
	''' This function reads json and masterfile and replace the value in json from masterfile '''
	try:

		df_master = pd.read_csv(masterfile)
		master_dict = dict(zip(df_master.Old_store_ids, df_master.New_store_ids))

		with open(filename, 'r') as file:
			json_data = json.load(file)
			for transactions in json_data:
				
				print('Old_store_ids:New_store_ids ---->',transactions['store_id'],":",master_dict[transactions['store_id']])

				transactions['store_id']=master_dict[transactions['store_id']]

		with open(newfilename, 'w') as file:
			json.dump(json_data, file, indent=2)

	except KeyError:
		print('{0} value not found in the masterdict'.format())

	except Exception as e:
		raise (e)

if __name__=="__main__":
	replace_data(filename,masterfile)