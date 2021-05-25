#=====================================================================================================================================================================
# Title			 : stores_insert_v3.py
# Description    : The program does the following:
#					1.Check the stores using poskey , if found update in stores and address table.
#					2.If not found, call a stored proc to insert the store details in stores,address and storehours table.
# NOTE			 : Run on NIFI econ stg box ( for staging )
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-04-08
# Version        : 1.0
# Python version : 3.7.3
# Command line 	 : sudo /opt/nifi/data/processor_input/pepcoin/pepcoin_venv/bin/python3.6 stores_insert_v3.py --file CSC_Stores_through_Sept_2020.csv
#=====================================================================================================================================================================
import pandas as pd
import pyodbc
import argparse
import sys
import logging
from datetime import datetime

# hardcoding 
Retailer_id='97870248-AA40-4D69-9764-594CFC81FF1A'

def create_parser():
	""" This function will return command line parser """
	try:
		parser=argparse.ArgumentParser(description='Script to perform stores ingestion and update the existing stores based on poskey',prog='stores_insert_v3.py')
		parser.add_argument('--file', dest='file', help='pass store filename with full path')
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
		if not args.file:
			parser.error('Incorrect number of arguments passed: file required')
		return args

	except Exception as e:
		print(e)
		raise e


def create_conn():
	""" This function creates connection to database """
	try:
		# creating connection to sql server from nifi econ stg box
		# hardcoding 
		con = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};\
			  SERVER='+'lt-app-beta-db.ent.local'+';DATABASE='+'csc'+';UID='+'loyaltree'+';PWD='+'tdYNIoC3!paMyUQV')

		return con

	except Exception as e:
		print(e)
		raise e


def update_stores_poskey(filename,con):
	""" This function checks for the existing stores in database from the supplied file and if found update """
	try:
		df_stores=pd.read_csv(filename)
		sql_to_check_data="select POSStoreKey from csc.dbo.retailerstores where retailerID={0}".format("'"+Retailer_id+"'")
		df_database=pd.read_sql(sql=sql_to_check_data,con=con)
		df_stores['is_update'] = df_stores.posstorekey.astype(str).isin(df_database.POSStoreKey).astype(int)
		
		data_to_update=df_stores.loc[(df_stores['is_update']==1)]
		data_to_insert=df_stores.loc[(df_stores['is_update']==0)]
		
		print("Data to insert:\n",data_to_insert)
		print("Data to update:\n",data_to_update)

		logger.info("****** Data to insert ******")
		logger.info(data_to_insert)
		logger.info("\n")
		logger.info("****** Data to update ******")
		logger.info(data_to_update)

		get_id_addressid="select id,addressid,posstorekey from csc.dbo.retailerstores where retailerID={0}".format("'"+Retailer_id+"'")
		df_get_det=pd.read_sql(sql=get_id_addressid,con=con)
		
		logger.info("****** Update statements ******")
		logger.info('\n')
		

		count=0
		cur= con.cursor()
		for row in data_to_update.itertuples():
			
			add_id=df_get_det.loc[df_get_det['posstorekey'] == str(row.posstorekey), 'addressid'].item()
			
			# retailerstores table
			sql_update_stores='''update csc.dbo.retailerstores set \
			storeName={0},contactemail={1},phone={2},posid={3},lastupdated={4} where retailerid={5} and posstorekey={6}'''.\
			format("'"+row.name+"'","'"+row.ContactEmail+"'","'"+row.phone_number+"'","'"+row.external_id+"'",'GETUTCDATE()',"'"+Retailer_id+"'","'"+str(row.posstorekey)+"'")

			# address table
			sql_update_stores_address='''update csc.dbo.addresses set \
			AddressLine1={0},AddressLine2={1},city={2},state={3},zip={4},country={5},Lat={6},Lon={7},name={8},timezoneid={9},lastupdated={10} where id ={11}'''.\
			format("'"+row.address+"'",'null',"'"+row.city+"'","'"+row.state+"'","'"+str(row.zip)+"'","'"+row.country+"'","'"+str(row.lat)+"'","'"+str(row.lng)+"'","'"+row.name+"'",\
					"'"+row.time_zone+"'",'GETUTCDATE()',"'"+add_id+"'")

			cur.execute(sql_update_stores)
			cur.execute(sql_update_stores_address)

			logger.info(sql_update_stores)
			logger.info(sql_update_stores_address)

			count+=1
			print("{0} row updated".format(count))

		# commiting data , closing cursor and connection
		con.commit()
		cur.close()

		return data_to_insert

	except Exception as e:
		print(e)
		raise e

def call_proc(df,con):
	try:
		# creating cursor to hold data for query execution
		cur= con.cursor()
		count=0

		for _,j in df.iterrows():

		# hardcoding of retailer id
			sql='''
					declare @retailerid uniqueidentifier
					declare @storeid uniqueidentifier
					declare @addressid uniqueidentifier
					declare @posid uniqueidentifier

					set @retailerid=convert(uniqueidentifier, '97870248-AA40-4D69-9764-594CFC81FF1A')
					set @posid=convert(uniqueidentifier, {16})
					set @storeid=newid()
					set @addressid=newid()

					exec csc.dbo.Setup_RegisterStore
				    @ScanExpiration=10080,
				    @RetailerID=@retailerid,
				    @StoreID=@storeid,
				    @AddressID=@addressid,
				    @AddressLine1={0},
				    @AddressLine2={1},
				    @City={2},
				    @State={3},
				    @Zip={4},
				    @Country={5},
				    @Latitude={6},
				    @Longitude={7},
				    @TimeZoneID={8},
				    @StoreName={9},
				    @Email={10},
				    @Phone={11},
				    @OpenFrom={12},
				    @OpenTo={13},
				    @DaysOfWeek={14},
				    @PosStoreKey={15},
				    @POSID=@posid
				'''.format( \
			    	"'"+j['address']+"'",\
			    	'null',"'"+j['city']+"'",\
			    	"'"+j['state']+"'",\
			    	"'"+str(j['zip'])+"'", \
			    	"'"+j['country']+"'",\
			    	"'"+str(j['lat'])+"'",\
			    	"'"+str(j['lng'])+"'",\
			    	"'"+j['time_zone']+"'",\
			    	"'"+j['name']+"'",\
			    	"'"+j['ContactEmail']+"'",\
			    	"'"+j['phone_number']+"'",\
			    	'0',\
			    	'0',\
			    	'126',\
			    	"'"+str(j['posstorekey'])+"'",\
			    	"'"+j['external_id']+"'"\
			    	)

			print(sql)
			
			logger.info("****** Inserts using stored proc ******")
			logger.info("\n")
			logger.info(sql)  

			#*************** IMPORTANT : cur.execute (the process to insert the data is commented.Uncomment CAREFULLY!!) ******************#
			#cur.execute(sql)
			count+=1
			print('{0} Record Inserted'.format(count))

			#break

		con.commit()
		cur.close()
		con.close()

	except Exception as e:
		raise (e)

def main(argv=None):
	""" Program execution starts from here """
	try:
		if argv is None:
			argv=sys.argv
		args= parse_args(argv[1:])

		# this function creates db connection
		con=create_conn()

		# check for updates if any based on poskey
		data_to_insert=update_stores_poskey(args.file,con)

		# run the stored proc for fresh inserts
		call_proc(data_to_insert,con)
		
	except Exception as e:
		print(e)
		raise e


""" Creating logger for program (hardcoding) """
log_file_name='stores_ingestion_prd'
log_file_name +='_'+datetime.now().strftime("%Y%m%d_%H%M%S")+'.log'

file_path="/opt/nifi/data/processor_input/pepcoin/script/log/"+log_file_name
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler=logging.FileHandler(file_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


if __name__ == '__main__':
	sys.exit(main())




