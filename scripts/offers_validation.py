#=====================================================================================================================================================
# Title             : offers_validation.py
# Description       : The program does the following:
#                     Get the count of offers from connect based on the timestamp and compare the count from the file
# Author            : Shobhit Bhatnagar
# Date              : 2020-12-14
# Version           : 1.0
# Python version    : 3.6
# Command line      : /opt/nifi/data/processor_input/pyenv/bin/python3 /opt/nifi/data/processor_input/scripts/offers_validation.py --file <filename>
#======================================================================================================================================================

import numpy as np
import pandas as pd
import pyodbc
import pymysql
import argparse
import sys
import logging
from tabulate import tabulate
from datetime import datetime


def create_parser():
  """ This function will return command line parser """
  try:
    parser=argparse.ArgumentParser(description='offers data validation script',prog='offers_validation.py')
    parser.add_argument('--file', dest='file', help='pass offers filename with absolute path')
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
      SERVER='+'lt-app-beta-db.ent-ie.local'+';DATABASE='+'finnair'+';UID='+'loyaltree'+';PWD='+'6Wa52LBROUR3d7bd')

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
    con=pymysql.connect(host="core-db-finnair.ent-ie.local",user="sessionm",password="Chywt19e9yyyV9FhEsAERd7N",db="greyhound_finnair")
    
    return con

  except Exception as e:
    print("An error occured in create_connection_coredb function:",e)
    raise e
    sys.exit(1)

def offer_validation(offer_file,core_con,connect_con):
  """ This function compare the offers file with the already loaded data in database and generate report """
  try:
    count=0
    appended_data=[]
    for df_offer_file in pd.read_csv(offer_file,skipinitialspace=True,chunksize=10000):
      count=count+1
      print("Processing for chunk:{}".format(count))
      """ Reading a file with a chunk of 10000 to avoid out of memory error from SQL server """

      df_offer_file=pd.read_csv(offer_file,skipinitialspace=True,usecols=['EXTERNAL_ID'])
      df_offer_file['external_id_quotes']=df_offer_file['EXTERNAL_ID'].apply(lambda x: "'" + str(x) + "'")
      external_id_list=list(df_offer_file['external_id_quotes'])
      external_id_list=list(set(external_id_list))
      
      # Sql to get userid from core based on the externalid present in the file
      sql_on_core="""select 
              p.user_id as user_id,
              ou.external_id as external_id
              from organization_users ou 
              left join players p on ou.player_id = p.id
              where ou.organization_id = (select id from organizations where name='finnair')
              and ou.external_id in ({})""".format(",".join([str(i) for i in external_id_list]))

      # creating dataframe to hold userids and externalids from core
      df_userid_extid_core=pd.DataFrame(columns=['user_id','external_id'])

      for df_userid_extid_list in pd.read_sql_query(sql_on_core, core_con,chunksize=20000):
        df_userid_extid_core=df_userid_extid_core.append(df_userid_extid_list)


      #print(df_userid_extid_core)

      df_userid_extid_core['user_id_quotes']=df_userid_extid_core['user_id'].apply(lambda x: "'" + str(x) + "'")
      user_id_list=list(df_userid_extid_core['user_id_quotes'])


      # Sql to get userid and offer count from connect based on the last updated column
      sql_on_connect="""select userid as user_id,count(1) as offer_count_from_database from [finnair-offers].offers.UserOffers 
                          where retailerid in (select id from retailers where name='finnair')
                          -- and cast(lastupdated as date)=cast( getdate() as date )
                          and cast(lastupdated as date) in ('2021-03-10','2021-03-11')
                          and userid in ({}) group by userid""".format(",".join([str(i) for i in user_id_list]))


      # creating dataframe to hold userids and offers from connect
      df_userid_offerscount_connect=pd.DataFrame(columns=['user_id','offer_count_from_database'])

      for df_userid_offerscount_list in pd.read_sql_query(sql_on_connect, connect_con,chunksize=20000):
        df_userid_offerscount_connect=df_userid_offerscount_connect.append(df_userid_offerscount_list)

      #print(df_userid_offerscount_connect)

      # merge both the dataframes mentioned above to get master dataframe for comparision with the input file (inner join)
      master_df = pd.merge(left=df_userid_extid_core, right=df_userid_offerscount_connect, left_on='user_id', right_on='user_id')
      master_df.drop('user_id_quotes', inplace=True, axis=1)

      #print(master_df)

      # Input file dataframe
      df_offer_file.drop('external_id_quotes',inplace=True, axis=1)
      df_offer_file=df_offer_file.pivot_table(index = ['EXTERNAL_ID'], aggfunc ='size')
      df_offer_file_final = df_offer_file.to_frame('offer_count_from_file').reset_index()
      
      master_df=master_df.astype(str)
      df_offer_file_final=df_offer_file_final.astype(str)

      # creating dataframe for report
      report_df = pd.merge(left=master_df, right=df_offer_file_final, left_on='external_id', right_on='EXTERNAL_ID')
      report_df.drop('EXTERNAL_ID',inplace=True, axis=1)

      match_msg="Record Count Match between the database and the file"
      mismatch_msg="Record Count Mismatch between the database and the file"

      report_df['message'] = np.where(report_df['offer_count_from_database'] == report_df['offer_count_from_file'], match_msg, mismatch_msg)

      #print(report_df)
      appended_data.append(report_df)

      # Creating report contents
      logger.info("\t\t\t\t****************************** User Offers Data Validation Report ******************************\n\n")
      logger.info(tabulate(report_df, headers='keys', tablefmt='psql',showindex=False))

      #break

    combined_df = pd.concat(appended_data)

    combined_df.to_csv('offer_validation_report_'+datetime.now().strftime("%Y%m%d_%H%M%S")+'.csv', encoding='utf-8',index=False)
      
  except Exception as e:
    print("An error occured in offer_validation function:",e)
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
    offer_validation(args.file,core_con,connect_con)

    print("Data Validation Report Generated")
    
  except Exception as e:
    print("An error occured in main function:",e)
    raise e
    sys.exit(1)

""" creating logger for report """
log_file_name='offer_validation_report'
log_file_name +='_'+datetime.now().strftime("%Y%m%d_%H%M%S")+'.log'

file_path="/opt/nifi/data/processor_input/validation_report/offers/"+log_file_name
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(message)s')
file_handler=logging.FileHandler(file_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

if __name__=="__main__":
  print('-'*10,'Offers validation script Started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*10)
  main()
  print('-'*10,'Offers validation script Ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*10)

