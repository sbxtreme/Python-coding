#====================================================================================================================================================================
# Title          : csc_stores_etl.py
# Description    : The program converts the ticks into hours in am/pm and converts bitmasking of days into human readable days
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-09-01
# Version        : 1.0
# Python version : 3.7.3
# Command line   : python csc_stores_etl.py --file /Users/capgemini/scripts/test/stores_data_opendaystime.csv --output_location /Users/capgemini/scripts/test/
#======================================================================================================================================================================

import sys
import argparse
import datetime as dt
from datetime import datetime
import pandas as pd

def create_parser():
	""" This function will return command line parser """
	try:
		parser=argparse.ArgumentParser(description='Script converts the ticks into hours in am/pm and converts bitmasking of days into human readable days',prog='csc_stores_etl.py')
		parser.add_argument('--file', dest='file', help='pass stores filename with full path')
		parser.add_argument('--output_location', dest='output_location', help='output_location')
		parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
		return parser

	except Exception as e:
		print(e)
		raise e

def parse_args(arguments):
	""" This function will parse the command line arguments """
	try:
		parser=create_parser()
		args=parser.parse_args(arguments)

		''' check for mandatory parameters '''
		if not args.file or not args.output_location:
			parser.error('Incorrect number of arguments passed: file_name and output_location required')
		return args

	except Exception as e:
		print(e)
		raise e

def convert_tick_into_time(input_data):
	""" This function converts tick into time """
	try:
		converted_ticks=dt.datetime(2020, 9, 1, 00, 00, 00, 000000)+dt.timedelta(microseconds=input_data/10)
		conv_ticks_time=converted_ticks.strftime("%H:%M")
		d=datetime.strptime(conv_ticks_time, "%H:%M")
		output_data =d.strftime("%I:%M %p")
		return output_data

	except Exception as e:
		print(e)
		raise e

def stores_etl(file_name,output_location):
	""" This function perfoms ETL on the store file """
	try:
		'''

		Bitmasking for days:
		Sunday:1
		Moday:2
		Tuesday:4
		Wednedsay:8
		Thursday:16
		Friday:32
		Saturday:64

		2-->   Monday 
		8-->   Wednesday
		30-->  Monday,Tuesday,Wednesday,Thursday
		32-->  Friday
		62-->  Monday,Tuesday,Wednesday,Thursday,Friday
		64-->  Saturday
		118--> Monday,Tuesday,Thursday,Friday,Saturday
		124--> Tuesday,Wednesday,Thursday,Friday,Saturday
		126--> Monday,Tuesday,Wednesday,Thursday,Friday,Saturday
		
		'''
		
		df_stores=pd.read_csv(file_name)

		cols_to_change=['posstorekey','zip','openfrom','opento','daysofweek']

		for cols in cols_to_change:
			df_stores[cols] = df_stores[cols].fillna(-9999)
			df_stores[cols] = df_stores[cols].astype(int)
		
		openfrom_list=[]
		opento_list=[]
		for row in df_stores.itertuples():
			
			if row.openfrom != -9999 and row.opento!= -9999:
				openfrom=convert_tick_into_time(row.openfrom)
				openfrom_list.append(openfrom)

				opento=convert_tick_into_time(row.opento)
				opento_list.append(opento)
			else:
				openfrom=''
				openfrom_list.append(openfrom)
				opento=''
				opento_list.append(opento)

		df_stores['new_openfrom'] = openfrom_list
		df_stores['new_opento'] = opento_list

		# logic for bitmap:
		sun_list,mon_list,tue_list,wed_list,thus_list,fri_list,sat_list=[],[],[],[],[],[],[]

		for row in df_stores.itertuples():
			if row.daysofweek != -9999 and row.daysofweek == 2:
				mon_list.append(row.new_openfrom+' - '+row.new_opento)
				tue_list.append('Closed')
				wed_list.append('Closed')
				thus_list.append('Closed')
				fri_list.append('Closed')
				sat_list.append('Closed')
				sun_list.append('Closed')
				
			elif row.daysofweek != -9999 and row.daysofweek == 8:
				mon_list.append('Closed')
				tue_list.append('Closed')
				wed_list.append(row.new_openfrom+' - '+row.new_opento)
				thus_list.append('Closed')
				fri_list.append('Closed')
				sat_list.append('Closed')
				sun_list.append('Closed')
				
			elif row.daysofweek != -9999 and row.daysofweek == 30:
				mon_list.append(row.new_openfrom+' - '+row.new_opento)
				tue_list.append(row.new_openfrom+' - '+row.new_opento)
				wed_list.append(row.new_openfrom+' - '+row.new_opento)
				thus_list.append(row.new_openfrom+' - '+row.new_opento)
				fri_list.append('Closed')
				sat_list.append('Closed')
				sun_list.append('Closed')

			elif row.daysofweek != -9999 and row.daysofweek == 32:
				mon_list.append('Closed')
				tue_list.append('Closed')
				wed_list.append('Closed')
				thus_list.append('Closed')
				fri_list.append(row.new_openfrom+' - '+row.new_opento)
				sat_list.append('Closed')
				sun_list.append('Closed')

			elif row.daysofweek != -9999 and row.daysofweek == 62:
				mon_list.append(row.new_openfrom+' - '+row.new_opento)
				tue_list.append(row.new_openfrom+' - '+row.new_opento)
				wed_list.append(row.new_openfrom+' - '+row.new_opento)
				thus_list.append(row.new_openfrom+' - '+row.new_opento)
				fri_list.append(row.new_openfrom+' - '+row.new_opento)
				sat_list.append('Closed')
				sun_list.append('Closed')

			elif row.daysofweek != -9999 and row.daysofweek == 64:
				mon_list.append('Closed')
				tue_list.append('Closed')
				wed_list.append('Closed')
				thus_list.append('Closed')
				fri_list.append('Closed')
				sat_list.append(row.new_openfrom+' - '+row.new_opento)
				sun_list.append('Closed')

			elif row.daysofweek != -9999 and row.daysofweek == 118:
				mon_list.append(row.new_openfrom+' - '+row.new_opento)
				tue_list.append(row.new_openfrom+' - '+row.new_opento)
				wed_list.append('Closed')
				thus_list.append(row.new_openfrom+' - '+row.new_opento)
				fri_list.append(row.new_openfrom+' - '+row.new_opento)
				sat_list.append(row.new_openfrom+' - '+row.new_opento)
				sun_list.append('Closed')

			elif row.daysofweek != -9999 and row.daysofweek == 124:
				mon_list.append('Closed')
				tue_list.append(row.new_openfrom+' - '+row.new_opento)
				wed_list.append(row.new_openfrom+' - '+row.new_opento)
				thus_list.append(row.new_openfrom+' - '+row.new_opento)
				fri_list.append(row.new_openfrom+' - '+row.new_opento)
				sat_list.append(row.new_openfrom+' - '+row.new_opento)
				sun_list.append('Closed')			

			elif row.daysofweek != -9999 and row.daysofweek == 126:
				mon_list.append(row.new_openfrom+' - '+row.new_opento)
				tue_list.append(row.new_openfrom+' - '+row.new_opento)
				wed_list.append(row.new_openfrom+' - '+row.new_opento)
				thus_list.append(row.new_openfrom+' - '+row.new_opento)
				fri_list.append(row.new_openfrom+' - '+row.new_opento)
				sat_list.append(row.new_openfrom+' - '+row.new_opento)
				sun_list.append('Closed')

			else:
				mon_list.append('')
				tue_list.append('')
				wed_list.append('')
				thus_list.append('')
				fri_list.append('')
				sat_list.append('')
				sun_list.append('')

		df_stores['Monday'],df_stores['Tuesday'],df_stores['Wednesday'],df_stores['Thursday'],df_stores['Friday'],df_stores['Saturday'],df_stores['Sunday'] =\
		mon_list,tue_list,wed_list,thus_list,fri_list,sat_list,sun_list

		df_stores['posstorekey'].replace(-9999,'',inplace=True)

		# the below 2 lines can be commented for dubugging and testing the this ETL script
		col_to_drop=['openfrom','opento','new_openfrom','new_opento','daysofweek']
		df_stores = df_stores[df_stores.columns.drop(col_to_drop)]
		
		# Creating filename
		file_name = 'CSC_stores_etl_outputfile.csv'

		df_stores.to_csv(output_location+file_name,index=False)

	except Exception as e:
		print(e)
		raise e

def main(argv=None):
	""" Program execution starts from here """
	try:
		if argv is None:
			argv=sys.argv
		args= parse_args(argv[1:])

		# The below function perform ETL and generate csv
		stores_etl(args.file,args.output_location)
		print('ETL completed and csv generated!')
		
	except Exception as e:
		print(e)
		raise e

if __name__=="__main__":
	print('---- CSC stores ETL process started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'----')
	main()
	print('---- CSC stores ETL process completed on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'----')

