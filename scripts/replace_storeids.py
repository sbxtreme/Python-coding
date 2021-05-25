#=============================================================================================================================
# Title          : replace_storeids.py
# Description    : The program replaces the external storeids with internalids in transaction file using a csv store file
# Author         : Shobhit Bhatnagar
# Date           : 2020-09-14
# Version        : 1.0
# Python version : 3.7.3
#============================================================================================================================

import os
import sys
import json
import glob
import argparse
import logging
import pandas as pd
from datetime import datetime

################  global settings and executions  ###################
store_tran_dir='/opt/nifi/data/processor_input/storeIds'
script_dir='/opt/nifi/data/processor_input/scripts'
final_tranfilepath='/opt/nifi/data/processor_input/transactions/'

os.chdir(store_tran_dir)

transaction_file=glob.glob('*connect_transaction*')[0]
store_file=glob.glob('*storeids*')[0]

tran_filepath=store_tran_dir+'/'+transaction_file
store_filepath=store_tran_dir+'/'+store_file

os.chdir(script_dir)

#print(tran_filepath)
#print(store_filepath)
######################################################################


def handle_storeids(posstorekey,df_stores):
	""" This function uses external id in the transaction file and get its corresponding internal id. 
		In case of internal id not found , it simply returns the external id which is passed to lookup internal id """
	try:
		internal_storeids=df_stores.loc[df_stores['external_storeids'] == posstorekey, 'internal_storeids'].iloc[0]
		return internal_storeids

	except IndexError as e:
		return posstorekey

	except Exception as e:
		print(e)


def replace_storeids(storefile,tranfile):
	try:
		tran_list=[]
		count=0

		logger.info("Step 2: Reading stores file")

		df_stores=pd.read_csv(storefile)

		logger.info("Step 3: Reading transactions file")

		with open(tranfile) as f:
			data = json.load(f)

			logger.info("Step 4: Store id replacement process started")

			for transactions in data:
				count+=1
				posstorekey=transactions['store_id']
				internal_storeids=handle_storeids(posstorekey,df_stores)
				transactions['store_id']=internal_storeids

				logger.info("Replacing {0} posstorekey with {1} internal id".format(posstorekey,internal_storeids))

				tran_list.append(transactions)

		logger.info("Step 5: Store id replacement process completed. Creating a new transaction file ...")

		# getting the path without basename and creating a new file with new_{existing_filename}
		path=os.path.dirname(tranfile)
		new_tran_file=os.path.basename(tranfile)

		new_file_name=final_tranfilepath+new_tran_file

		# creating new transaction file from tran_list
		with open(new_file_name, 'w') as output_file:
			json.dump(tran_list,output_file,indent=4)

		logger.info("Step 6: New transaction file {0} created".format(new_file_name))

		return new_file_name

	except Exception as e:
		logger.error("An error occured in the script inside replace_storeids function on record {0}:{1}".format(count,e))
		print(e)
		raise e


def main(argv=None):
	""" Program execution starts from here """
	try:

		logger.info("******** NOTE: If posstorekey == internal id in the log file , it means posstorekey is not present in SessionM platform. ********")
		logger.info("Step 1: Script execution Started")

		new_tran_file=replace_storeids(store_filepath,tran_filepath)
		print("New transaction file {0} generated".format(new_tran_file))

		os.remove(store_filepath)
		os.remove(tran_filepath)

		logger.info("Step 7: Storefile and Transactionfile deleted")
		logger.info("Step 8: Script execution completed Successfully!")

	except Exception as e:
		logger.error("An error occured in the script inside main function:{0}. Program TERMINATED!".format(e))
		print(e)
		raise e



############################### creating logger for the program (hardcoding) ###############################

log_file_name='storeid_replacement_process_'+datetime.now().strftime("%Y%m%d%H%M%S")+'.log'
log_file_path='/opt/nifi/data/processor_input/logs/'
file_path=log_file_path+log_file_name
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler=logging.FileHandler(file_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


if __name__ == '__main__':
	print('======== Storeid replacement process started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'========')
	main()
	print('======== Storeid replacement process ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'========')
