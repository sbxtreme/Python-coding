#=====================================================================================================================================
# Title			 : insert_data.py
# Description    : The program inserts the data in core table by reading the supplied csv file.
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-10-14
# Version        : 1.0
# Python version : 3.4
#=====================================================================================================================================

import pymysql
import csv

##################### hardcodings: ############################################################################
filename='userids_from_tiertable_connect.csv'
host='core-db-csc.ent.local'
user='sessionm'
password='xYTgh8Gy6juLCd66'
db='greyhound_csc'
#command_line : sudo /opt/nifi/data/processor_input/pepcoin/env_python3.4/bin/python3.4 insert_data.py
###############################################################################################################

def create_mysql_connection(host,user,password,db):
	try:
		con = pymysql.connect(host=host,user=user,password=password,db=db)
		return con

	except Exception as e:
		print('Program failed with the below exception while creating connection to mysql database :',e)


def insert_data(con):
	try:
		cursor=con.cursor()
		csv_data = csv.reader(open(filename))
		next(csv_data)
		count=0
		for row in csv_data:
			cursor.execute('INSERT INTO tierqualified_users(external_id) VALUES(%s)',row)
			count+=1
			print("Records inserted:",count)

		con.commit()
		cursor.close()

	except Exception as e:
		print(e)
		raise e


def main():
	try:
		con=create_mysql_connection(host,user,password,db)
		print("Connection created!")
		insert_data(con)

	except Exception as e:
		print(e)
		raise e


if __name__=="__main__":
	main()