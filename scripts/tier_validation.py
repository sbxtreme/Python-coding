#=====================================================================================================================================================================
# Title          : tier_validation.py
# Description    : The program does the following:
#                   Read the tier file from nifi server , compare with the already loaded data and generate a comparision report.
# Author         : Shobhit Bhatnagar
# Date           : 2020-11-19
# Version        : 1.0
# Python version : 3.6
# Command line   : /opt/nifi/data/processor_input/pyenv/bin/python3 /opt/nifi/data/processor_input/scripts/tier_validation.py --file <filename>
#=====================================================================================================================================================================

import pandas as pd
import pyodbc
import pymysql
import argparse
import sys
from datetime import datetime
import logging

def create_parser():
  """ This function will return command line parser """
  try:
    parser=argparse.ArgumentParser(description='Tier data validation script',prog='tier_validation.py')
    parser.add_argument('--file', dest='file', help='pass tier filename with absolute path')
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


def create_connection_connectdb():
  """ This function creates connection to Connect database """
  try:
    # creating connection to sql server from finnair nifi box
    # hardcoding 
    con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
      SERVER='+'lt-app-db.stg.local'+';DATABASE='+'finnair2'+';UID='+'loyaltree'+';PWD='+'B4h5lhsl3_Kqit8AF3RoIxuLeMs4aRqQ')

    return con

  except Exception as e:
    print("An error occured in create_connection_connectdb function:",e)
    raise e
    sys.exit(1)


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


def tier_validation(tier_file,core_con,connect_con):
  """ This function compare the tier file with the already loaded data in database and generate report """
  try:

    df_tier_=pd.read_csv(tier_file,skipinitialspace=True, usecols=['external_id','tier_name'], chunksize=1000)
    for df_tier_file in df_tier_:


        df_tier_file['external_id_quotes']=df_tier_file['external_id'].apply(lambda x: "'" + str(x) + "'")
        external_id_list=list(df_tier_file['external_id_quotes'])
    
        # Sql to get userid from core based on the externalid present in the file
        sql_on_core="""select 
                p.user_id as user_id,
                ou.external_id as external_id
                from organization_users ou 
                left join players p on ou.player_id = p.id
                where ou.organization_id = (select id from organizations where name='finnair2')
                and ou.external_id in ({})""".format(",".join([str(i) for i in external_id_list]))

        # creating dataframe to hold userids and externalids from core
        df_userid_extid_core=pd.DataFrame(columns=['user_id','external_id'])

        for df_userid_extid_list in pd.read_sql_query(sql_on_core, core_con,chunksize=20000):
          df_userid_extid_core=df_userid_extid_core.append(df_userid_extid_list)

        print("core list====>", df_userid_extid_core)

        df_userid_extid_core['user_id_quotes']=df_userid_extid_core['user_id'].apply(lambda x: "'" + str(x) + "'")
        user_id_list=list(df_userid_extid_core['user_id_quotes'])

        print("user id list",user_id_list)

        # Sql to get tier details from connect based on the userids
        sql_on_connect="""select 
                  tm.userid as user_id,
                  tl.name as tier_name
                  from [finnair2-incentives].incent.TierMembers tm 
                  inner join [finnair2-incentives].incent.TierSystems ts on tm.TierSystemID=ts.id
                  inner join [finnair2-incentives].incent.TierLevels tl on tl.TierSystemID= ts.id and tl.id=tm.tierlevelid
                  where ts.id= (select id from [finnair2-incentives].incent.TierSystems where name='Finnair NextGen')
                  and tm.RetailerID = (select id from retailers where name = 'finnair2')
                  and tm.userid in ({})""".format(",".join([str(i) for i in user_id_list]))

        # creating dataframe to hold userids and tier_name from connect
        df_userid_tiername_connect=pd.DataFrame(columns=['user_id','tier_name'])

        for df_userid_tiername_list in pd.read_sql_query(sql_on_connect, connect_con,chunksize=20000):
            df_userid_tiername_connect=df_userid_tiername_connect.append(df_userid_tiername_list)


        print("df_userid_tiername_list---->", df_userid_tiername_list)

        # merge both the dataframes mentioned above to get master dataframe for comparision with the input file (inner join)
        print("core", df_userid_extid_core)
        print("connect", df_userid_tiername_connect)
        master_df = pd.merge(left=df_userid_extid_core, right=df_userid_tiername_connect, left_on='user_id', right_on='user_id')
        #print(master_df[["user_id", "external_id"]])
        master_df.drop('user_id_quotes', inplace=True, axis=1)

        # Input file dataframe
        df_tier_file.drop('external_id_quotes',inplace=True, axis=1)
        df_tier_file=df_tier_file.applymap(str)

        # mismatch data between file and connect database
        print("master df", master_df)
        print("tier_file df", df_tier_file)
        df_missing_data_in_db = pd.merge(left=df_tier_file, right=master_df, how='left', left_on='external_id', right_on='external_id')

        # to get list of external ids which are in file but not present in database
        df_final_missing_data=df_missing_data_in_db[df_missing_data_in_db['user_id'].isnull()]
        df_external_id_not_found = df_final_missing_data[['external_id']].copy()

        logger.info("\t\t\t\t****************************** Tier Data Validation Report ******************************\n\n")

        logger.info("\n\nExternal_ids in input file which are not present in connect database:")
        logger.info("=====================================================================\n")
        logger.info(df_external_id_not_found.to_string(index=False))
      
        # to get records whose file tier does not match with database tier
        df_mismatch=df_tier_file.merge(master_df, on='external_id').query('tier_name_x != tier_name_y')
        df_mismatch.rename(columns={'tier_name_x':'tier_in_file','tier_name_y':'tier_in_database'}, inplace=True)
        df_mismatch = df_mismatch[['external_id', 'user_id', 'tier_in_file', 'tier_in_database']]

        logger.info("\n\nRecords with Tier mismatch:")
        logger.info("===========================\n")
        logger.info(df_mismatch.to_string(index=False))

  except Exception as e:
      print("An error occured in tier_validation function:",e)
      raise e
      sys.exit(1)


def main(argv=None):
  """ Program execution starts from here """
  try:
    if argv is None:
      argv=sys.argv
    args= parse_args(argv[1:])

    # this function creates connect db connection
    connect_con=create_connection_connectdb()

    # this function creates core db connection
    core_con=create_connection_coredb()

    # this function validates the loaded data with input file
    tier_validation(args.file,core_con,connect_con)

    print("Data Validation Report Generated:\n",file_path)
    
  except Exception as e:
    print("An error occured in main function:",e)
    raise e
    sys.exit(1)


""" Creating logger for program (hardcoding) """
log_file_name='tier_validation_report'
log_file_name +='_'+datetime.now().strftime("%Y%m%d_%H%M%S")+'.log'

file_path="/opt/nifi/data/processor_input/validation_report/tiers/"+log_file_name
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(message)s')
file_handler=logging.FileHandler(file_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


if __name__=="__main__":
  print('-'*10,'Tier validation script Started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*10)
  main()
  print('-'*10,'Tier validation script Ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*10)

