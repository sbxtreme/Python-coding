#=============================================================================================================================================
# Title          : add_userids.py
# Description    : The program adds the userids in the file
# Author         : Shobhit Bhatnagar
# Date           : 2020-11-19
# Version        : 1.0
# Python version : 3.6
# Command line   : /opt/nifi/data/processor_input/pyenv/bin/python3 /opt/nifi/data/processor_input/scripts/add_userids.py --file <filename>
#=============================================================================================================================================

import pandas as pd
import pymysql
import argparse
import sys
import uuid
from datetime import datetime
import csv

def create_parser():
  """ This function will return command line parser """
  try:
    parser=argparse.ArgumentParser(description='Add userids in the file',prog='add_userids.py')
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


def add_userids(cust_file,core_con):
  """ This function replaces external_id with user_id """
  try:

    df_cust_file=pd.read_csv(cust_file,skipinitialspace=True)
    df_cust_file['external_id_quotes']=df_cust_file['external_id'].apply(lambda x: "'" + str(x) + "'")
    external_id_list=list(df_cust_file['external_id_quotes'])
    
    # Sql to get userid from core based on the externalid present in the file
    sql_on_core="""select 
                  p.user_id as user_id,
                  ou.external_id as external_id
                  from organization_users ou 
                  left join players p on ou.player_id = p.id
                  where ou.organization_id = (select id from organizations where name='finnair')
                  and ou.external_id in ({})""".format(",".join([str(i) for i in external_id_list]))

    
    df_userids_externalids=pd.read_sql(sql_on_core, core_con)
    df_cust_file=df_cust_file.applymap(str)
    df_final_data = pd.merge(left=df_cust_file, right=df_userids_externalids, how='left', left_on='external_id', right_on='external_id')
    df_final_data.drop(['external_id_quotes'], inplace=True, axis=1)

    print("User_id column addition process completed! Generating a new file ...")
    col = df_final_data.pop("user_id")
    df_final_data.insert(0, col.name, col)

    # replacing valuues as per required csv
    df_final_data.replace('nan',"",inplace=True)
    #df_final_data.replace('False','false',inplace=True)
    #df_final_data.replace('True','true',inplace=True)

    df_final_data.replace('False',0,inplace=True)
    df_final_data.replace('True',1,inplace=True)


    # writing data in a csv file
    #df_final_data.update(df_final_data[['auto_renewal', 'status_hold_point']].applymap('"{}"'.format))
    df_final_data.to_csv(cust_file, index=False,na_rep='',quoting=csv.QUOTE_NONE)

    print("New File Generated!")

  except Exception as e:
    print("An error occured in add_userids function:",e)
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

    # this function replaces external_id with user_id
    add_userids(args.file,core_con)
    
  except Exception as e:
    print("An error occured in main function:",e)
    raise e
    sys.exit(1)


if __name__=="__main__":
  main()