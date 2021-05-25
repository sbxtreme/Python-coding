#=====================================================================================================================================================================
# Title         :points_validation.py
# Description   :The program does the following:
#                   Read the points file from nifi server , compare with the already loaded data and generate a comparision report.
# Author        :Shobhit Bhatnagar
# Date          :2020-11-19
# Version       :1.0
# Python version:3.6
# Command line  :/opt/nifi/data/processor_input/pyenv/bin/python3 /opt/nifi/data/processor_input/scripts/points_validation.py --file <filename>
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
    parser=argparse.ArgumentParser(description='Points data validation script',prog='points_validation.py')
    parser.add_argument('--file', dest='file', help='pass points filename with absolute path')
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

def point_validation(point_file,core_con,connect_con):
  """ This function compare the Points file with the already loaded data in database and generate report """
  try:
    count=0
    for df_point_file in pd.read_csv(point_file,skipinitialspace=True,chunksize=5000):
        count=count+1
        print("Processing for chunk:{}".format(count))
        """ Reading a file with a chunk of 10000 to avoid out of memory error from SQL server """

        df_point_file.drop(['auto_renewal','status_hold_point'], inplace=True, axis=1)

        """ drop all the rows whose all point accounts are 0 """
        indexNames = df_point_file[(df_point_file['award_points'] == 0) & (df_point_file['ay_lifetime_tier_points'] == 0) & \
            (df_point_file['ay_qualifying_flights'] == 0) & (df_point_file['ay_tier_qualifying_points'] == 0) & \
            (df_point_file['gold_tier_counter'] == 0) & (df_point_file['platinum_tier_counter'] == 0) & (df_point_file['qualifying_flights'] == 0) & \
            (df_point_file['silver_tier_counter'] == 0) & (df_point_file['tier_qualifying_points'] == 0) ].index

        df_point_file.drop(indexNames , inplace=True)


        df_point_file['external_id_quotes']=df_point_file['external_id'].apply(lambda x: "'" + str(x) + "'")
        external_id_list=list(df_point_file['external_id_quotes'])
        
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

        df_userid_extid_core['user_id_quotes']=df_userid_extid_core['user_id'].apply(lambda x: "'" + str(x) + "'")
        user_id_list=list(df_userid_extid_core['user_id_quotes'])

        # reading external sql file into the program
        fd = open('/opt/nifi/data/processor_input/scripts/points.sql', 'r')
        sqlFile = fd.read()
        fd.close()

        # Sql to get point details from connect based on the userids
        sql_on_connect=sqlFile.format(",".join([str(i) for i in user_id_list]))

        # creating dataframe to hold userids and points from connect
        df_userid_Pointsname_connect=pd.DataFrame(columns=['user_id','award_points','ay_lifetime_tier_points',\
                                                        'ay_qualifying_flights','ay_qualifying_revenue','ay_tier_qualifying_points',\
                                                        'gold_tier_counter','platinum_tier_counter','qualifying_flights',\
                                                        'silver_tier_counter','tier_qualifying_points'])

        for df_userid_Pointsname_list in pd.read_sql_query(sql_on_connect, connect_con,chunksize=20000):
          df_userid_Pointsname_connect=df_userid_Pointsname_connect.append(df_userid_Pointsname_list)

        #print(df_userid_extid_core)
        #print(df_userid_Pointsname_connect)

        # merge both the dataframes mentioned above to get master dataframe for comparision with the input file (inner join)
        master_df = pd.merge(left=df_userid_extid_core, right=df_userid_Pointsname_connect, left_on='user_id', right_on='user_id')
        master_df.drop('user_id_quotes', inplace=True, axis=1)

        # Input file dataframe
        df_point_file.drop('external_id_quotes',inplace=True, axis=1)
        df_point_file=df_point_file.applymap(str)

        # mismatch data between file and connect database
        df_missing_data_in_db = pd.merge(left=df_point_file, right=master_df, how='left', left_on='external_id', right_on='external_id')

        # to get list of external ids which are in file but not present in database
        df_final_missing_data=df_missing_data_in_db[df_missing_data_in_db['user_id'].isnull()]

        #print(df_final_missing_data)
        df_external_id_not_found = df_final_missing_data[['external_id']].copy()

        logger.info("\t\t\t\t****************************** Points Data Validation Report ******************************\n\n")

        logger.info("\n\nExternal_ids in input file which are not present in connect database:")
        logger.info("=====================================================================\n")
        logger.info(df_external_id_not_found.to_string(index=False))
      
        # converting the dtype to str for both the dataframes for comparision
        master_df=master_df.astype(str).replace('\.0', '', regex=True)
        df_point_file=df_point_file.astype(str)

        # to get records whose file Points does not match with database Points
        df_mismatch=df_point_file.merge(master_df, on='external_id').query('(award_points_x != award_points_y) or \
                                                                            (ay_lifetime_tier_points_x != ay_lifetime_tier_points_y) or \
                                                                            (ay_qualifying_flights_x != ay_qualifying_flights_y) or \
                                                                            (ay_qualifying_revenue_x != ay_qualifying_revenue_y) or \
                                                                            (ay_tier_qualifying_points_x != ay_tier_qualifying_points_y) or \
                                                                            (gold_tier_counter_x != gold_tier_counter_y) or \
                                                                            (platinum_tier_counter_x != platinum_tier_counter_y) or \
                                                                            (qualifying_flights_x != qualifying_flights_y) or \
                                                                            (silver_tier_counter_x != silver_tier_counter_y) or \
                                                                            (tier_qualifying_points_x != tier_qualifying_points_y)')

        # renaming the columns in report
        df_mismatch.rename(columns={'award_points_x':'award_points_in_file', 'award_points_y':'award_points_in_database', \
                                    'ay_lifetime_tier_points_x':'ay_lifetime_tier_points_in_file', 'ay_lifetime_tier_points_y':'ay_lifetime_tier_points_in_database', \
                                    'ay_qualifying_flights_x':'ay_qualifying_flights_in_file', 'ay_qualifying_flights_y':'ay_qualifying_flights_in_database', \
                                    'ay_qualifying_revenue_x':'ay_qualifying_revenue_in_file', 'ay_qualifying_revenue_y':'ay_qualifying_revenue_in_database', \
                                    'ay_tier_qualifying_points_x':'ay_tier_qualifying_points_in_file', 'ay_tier_qualifying_points_y':'ay_tier_qualifying_points_in_database', \
                                    'gold_tier_counter_x':'gold_tier_counter_in_file', 'gold_tier_counter_y':'gold_tier_counter_in_database', \
                                    'platinum_tier_counter_x':'platinum_tier_counter_in_file', 'platinum_tier_counter_y':'platinum_tier_counter_in_database', \
                                    'qualifying_flights_x':'qualifying_flights_in_file', 'qualifying_flights_y':'qualifying_flights_in_database', \
                                    'silver_tier_counter_x':'silver_tier_counter_in_file', 'silver_tier_counter_y':'silver_tier_counter_in_database', \
                                    'tier_qualifying_points_x':'tier_qualifying_points_in_file', 'tier_qualifying_points_y':'tier_qualifying_points_in_database', \
                                    }, inplace=True)

        # Rearranging the columns in report
        df_mismatch = df_mismatch[['external_id', 'user_id', 'award_points_in_file', 'award_points_in_database', \
                                    'ay_lifetime_tier_points_in_file', 'ay_lifetime_tier_points_in_database', 'ay_qualifying_flights_in_file', 'ay_qualifying_flights_in_database', \
                                    'ay_qualifying_revenue_in_file','ay_qualifying_revenue_in_database','ay_tier_qualifying_points_in_file','ay_tier_qualifying_points_in_database', \
                                    'gold_tier_counter_in_file','gold_tier_counter_in_database','platinum_tier_counter_in_file','platinum_tier_counter_in_database', \
                                    'qualifying_flights_in_file','qualifying_flights_in_database','silver_tier_counter_in_file','silver_tier_counter_in_database', \
                                    'tier_qualifying_points_in_file','tier_qualifying_points_in_database']]

        # creating report name
        report_name="userpoints_mismatch_report_{}.csv".format(datetime.now().strftime("%Y%m%d_%H%M%S"))
        report_path="/opt/nifi/data/processor_input/validation_report/points/"+report_name

        df_mismatch.to_csv(report_path, index=False)

        logger.info("\n\nRecords with Points mismatch:")
        logger.info("==============================\n")
        logger.info("Report Available in CSV format in the below location:")
        logger.info(report_path)

    
  except Exception as e:
    print("An error occured in point_validation function:",e)
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
    point_validation(args.file,core_con,connect_con)

    print("Data Validation Report Generated on the below location:\n",report_path)
    
  except Exception as e:
    print("An error occured in main function:",e)
    raise e
    sys.exit(1)


""" Creating logger for program (hardcoding) """
log_file_name='point_validation_report'
log_file_name +='_'+datetime.now().strftime("%Y%m%d_%H%M%S")+'.log'

file_path="/opt/nifi/data/processor_input/validation_report/points/"+log_file_name
report_path="/opt/nifi/data/processor_input/validation_report/points/"
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(message)s')
file_handler=logging.FileHandler(file_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


if __name__=="__main__":
  print('-'*10,'Points validation script Started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*10)
  main()
  print('-'*10,'Points validation script Ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*10)

