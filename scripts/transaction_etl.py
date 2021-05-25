#===============================================================================================================================================
# Title          : transaction_etl.py
# Description    : The program gets does the etl on the transaction json file
# Author         : Shobhit Bhatnagar
# Date           : 2021-02-04
# Version        : 1.0
# Python version : 3.6
# Command line   : /opt/nifi/data/processor_input/pyenv/bin/python3 /opt/nifi/data/processor_input/scripts/transaction_etl.py <transaction_file>
#=================================================================================================================================================

import sys
from csv import DictReader
import json
from datetime import datetime

# input parameters
transaction_file=sys.argv[1]
transaction_file_path='/opt/nifi/scripts/transaction_files/'+transaction_file

new_json=[]


def etl_json(transaction_file):
	""" the function performs ETL on the passed json to create a new json file """
	try:
		with open(transaction_file) as f:
			data = json.load(f)
			for transactions in data:
				transactions["store_id"] = "19DE7784-01FD-44E6-A121-6E7C0F86029A"
				transactions["pos_employee_id"] = "AY_Historical"
				transactions["is_closed"]= True

				# adding modified json in a list
				new_json.append(transactions)

		# writing as a new json file
		#with open(transaction_file, 'w') as f:
		#	f.write(json.dumps(new_json,indent=4))


		with open(transaction_file, 'w') as f:
			f.write('[')

			for obj in new_json[:-1]:
				json.dump(obj, f)
				f.write(',')

			json.dump(new_json[-1], f)
			f.write(']')


	except Exception as e:
	    print("An error occured in etl_json function:",e)
	    raise e
	    sys.exit(1)


def main(argv=None):
  """ Program execution starts from here """
  try:
    # this function gets user_id from mapping file and convert that into dict
    etl_json(transaction_file_path)

    print("New Json file created!")
    
  except Exception as e:
    print("An error occured in main function:",e)
    raise e
    sys.exit(1)

if __name__=="__main__":
	print('Start time:',datetime.now().strftime("%b %d %Y %H:%M:%S"))
	main()
	print('End time:',datetime.now().strftime("%b %d %Y %H:%M:%S"))

