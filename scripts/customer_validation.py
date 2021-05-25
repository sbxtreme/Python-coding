#===================================================================================================================================================
# Title          : customer_validation.py
# Description    : The program does the following:
#                   Get the count from core players tables and compare the count with the customer file.
# Author         : Shobhit Bhatnagar
# Date           : 2020-11-19
# Version        : 1.0
# Python version : 3.6
# Command line   : /opt/nifi/data/processor_input/pyenv/bin/python3 /opt/nifi/data/processor_input/scripts/customer_validation.py --file <filename>
#=====================================================================================================================================================

import pandas as pd
import pymysql
import argparse
import sys
from datetime import datetime
import logging
from tabulate import tabulate

def create_parser():
  """ This function will return command line parser """
  try:
    parser=argparse.ArgumentParser(description='Customer data validation script',prog='Customer_validation.py')
    parser.add_argument('--file', dest='file', help='pass Customer filename with absolute path')
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

    # check for mandatory parameters
    if not args.file:
      parser.error('Incorrect number of arguments passed: filename required')
    return args

  except Exception as e:
    print("An error occured in parse_args function:",e)
    raise e

def create_connection_coredb():
  """ This function creates connection to Core database """
  try:
    # creating connection to mysql from finnair nifi box
    # hardcoding
    con=pymysql.connect(host="core-db-finnair2.stg.local",user="sessionm",password="8DXookKpQBBxEBJnQi2A8aJV",db="greyhound_integration_finnair2")
    
    return con

  except Exception as e:
    print("An error occured in create_connection_coredb function:",e)
    raise e
    sys.exit(1)


def customer_validation(cust_file,core_con):
  """ This function compare the count between core database and recent file loaded """
  try:

    df_cust_file=pd.read_csv(cust_file,skipinitialspace=True, usecols=['external_id'])
    df_cust_file['external_id_quotes']=df_cust_file['external_id'].apply(lambda x: "'" + str(x) + "'")
    external_id_list=list(df_cust_file['external_id_quotes'])
    
    # Sql to get userid from core based on the externalid present in the file
    sql_on_core="""select 
                    count(1) as no_of_users_in_database 
                    from organization_users where organization_id = (select id from organizations where name='finnair2')
                    and external_id in ({})""".format(",".join([str(i) for i in external_id_list]))

    
    # creating dataframe to hold count from core
    df_user_count=pd.read_sql(sql_on_core, core_con)

    # Getting record count from file and adding a column in existing dataframe
    index = df_cust_file.index
    number_of_users_in_file = len(index)
    df_user_count['no_of_users_in_file']=number_of_users_in_file

    #### Logic to get missing external ids which are missing in database but present in the file ####
    sql_to_get_externalids_from_core="""select 
                                          p.user_id as user_id,
                                          ou.external_id as external_id
                                          from organization_users ou 
                                          left join players p on ou.player_id = p.id
                                          where ou.organization_id = (select id from organizations where name='finnair2')
                                          and ou.external_id in ({})""".format(",".join([str(i) for i in external_id_list]))

    # creating dataframe to hold external_id from core
    df_user_extid_core=pd.read_sql(sql_to_get_externalids_from_core, core_con)

    df_cust_file=df_cust_file.applymap(str)

    # mismatch data between file and connect database
    df_missing_data_in_db = pd.merge(left=df_cust_file, right=df_user_extid_core, how='left', left_on='external_id', right_on='external_id')

    # to get list of external ids which are in file but not present in database
    df_final_missing_data=df_missing_data_in_db[df_missing_data_in_db['user_id'].isnull()]
    df_external_id_not_found = df_final_missing_data[['external_id']].copy()

    # Message for match and mismatch
    if str(number_of_users_in_file) == str(df_user_count['no_of_users_in_database'].item()):
      msg="No Record count mismatch found between the database and the file."

    else:
      msg="Record count mismatch found between the database and the file. Possible reason could be failures in SMSync."
      
    df_user_count['message']=msg

    # Creating report contents
    logger.info("\t\t\t\t****************************** Customer Data Validation Report ******************************\n\n")

    logger.info("\nList of External ids missing in the database:")
    logger.info("=============================================\n")
    logger.info(tabulate(df_external_id_not_found, headers='keys', tablefmt='psql',showindex=False))

    logger.info("\nRecord count details:")
    logger.info("=====================\n")
    logger.info(tabulate(df_user_count, headers='keys', tablefmt='psql',showindex=False))

  except Exception as e:
    print("An error occured in Customer_validation function:",e)
    raise e
    sys.exit(1)


def main(argv=None):
  """ Program execution starts from here """
  try:
    if argv is None:
      argv=sys.argv
    args= parse_args(argv[1:])

    # this function creates core db connection
    core_con=create_connection_coredb()

    # this function validates the loaded data with input file
    customer_validation(args.file,core_con)

    print("Data Validation Report Generated:\n",file_path)
    
  except Exception as e:
    print("An error occured in main function:",e)
    raise e
    sys.exit(1)


""" Creating logger for program (hardcoding) """
log_file_name='customer_validation_report'
log_file_name +='_'+datetime.now().strftime("%Y%m%d_%H%M%S")+'.log'
file_path="/opt/nifi/data/processor_input/validation_report/customers/"+log_file_name
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(message)s')
file_handler=logging.FileHandler(file_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


if __name__=="__main__":
  print('-'*10,'Customer validation script Started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*10)
  main()
  print('-'*10,'Customer validation script Ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*10)

