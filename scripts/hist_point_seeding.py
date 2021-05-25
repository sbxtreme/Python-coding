#==================================================================================================================================================
# Title          :hist_point_seeding.py
# Description    :The program does the following:
#                 Read the points file from nifi server and run update on database
# Author         :Shobhit Bhatnagar
# Date           :2020-11-19
# Version        :1.0
# Python version :3.6
# Command line   :/opt/nifi/data/processor_input/pyenv/bin/python3 /opt/nifi/data/processor_input/scripts/hist_point_seeding.py --file <filename>
#===================================================================================================================================================

import pandas as pd
import pyodbc
import argparse
import sys
from datetime import datetime


def create_parser():
  """ This function will return command line parser """
  try:
    parser=argparse.ArgumentParser(description='Historical point seeding script',prog='hist_point_seeding.py')
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
    con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
      SERVER=''lt-app-db.stg.local'';DATABASE=''finnair2'';UID=''loyaltree'';PWD=''B4h5lhsl3_Kqit8AF3RoIxuLeMs4aRqQ')

    return con

  except Exception as e:
    print("An error occured in create_connection_connectdb function:",e)
    raise e
    sys.exit(1)


def point_seeding(point,connect_con):
  """ This function reads the file and run updates on 12 point accounts for each user """
  try:

    df_point=pd.read_csv(point,skipinitialspace=True)

    column_names = ["user_id","external_id","auto_renewal","award_points","ay_lifetime_tier_points"\
                    ,"ay_qualifying_flights","ay_qualifying_revenue","ay_tier_qualifying_points",\
                    "gold_tier_counter","platinum_tier_counter","qualifying_flights","silver_tier_counter",\
                    "status_hold_point","tier_qualifying_points"]

    df_user_not_found = pd.DataFrame(columns = column_names)
    new_rows = []

    count=0
    cur= connect_con.cursor()

    for _,rows in df_point.iterrows():

        get_user_count_sql="""select count(*) from [finnair2-incentives].INCENT.UserPointAccounts where userid={0}""".format("'"+rows["user_id"]+"'")

        cur.execute(get_user_count_sql)
        result = cur.fetchone()[0]

        if result != 0:
        
            # list of updates
            update_sql1="""update [finnair2-incentives].INCENT.UserPointAccounts set availablebalance={0}, lifetimevalue={0} where  pointaccountid='b617f4b9-6837-49d6-8f41-feb8050266dd' and userid={1}""".format(rows["auto_renewal"],"'"+rows["user_id"]+"'")
            update_sql2="""update [finnair2-incentives].INCENT.UserPointAccounts set availablebalance={0}, lifetimevalue={0} where  pointaccountid='eaf7d27b-5400-4f2d-825d-c27720d42edf' and userid={1}""".format(rows["award_points"],"'"+rows["user_id"]+"'")
            update_sql3="""update [finnair2-incentives].INCENT.UserPointAccounts set availablebalance={0}, lifetimevalue={0} where  pointaccountid='a4f8b9c7-3cd6-414b-b62f-cef79a5e3849' and userid={1}""".format(rows["ay_lifetime_tier_points"],"'"+rows["user_id"]+"'")
            update_sql4="""update [finnair2-incentives].INCENT.UserPointAccounts set availablebalance={0}, lifetimevalue={0} where  pointaccountid='95b23b22-3d21-4b2c-8c2e-f7506e2104ba' and userid={1}""".format(rows["ay_qualifying_flights"],"'"+rows["user_id"]+"'")
            update_sql5="""update [finnair2-incentives].INCENT.UserPointAccounts set availablebalance={0}, lifetimevalue={0} where  pointaccountid='82b9e1fd-9bc8-4d60-ad6b-d812e3572185' and userid={1}""".format(rows["ay_qualifying_revenue"],"'"+rows["user_id"]+"'")
            update_sql6="""update [finnair2-incentives].INCENT.UserPointAccounts set availablebalance={0}, lifetimevalue={0} where  pointaccountid='6a21d0f0-27eb-4d83-8712-de9d0cce6a25' and userid={1}""".format(rows["ay_tier_qualifying_points"],"'"+rows["user_id"]+"'")
            update_sql7="""update [finnair2-incentives].INCENT.UserPointAccounts set availablebalance={0}, lifetimevalue={0} where  pointaccountid='fa0979b3-f90d-4b4e-80f9-2a94c9c49feb' and userid={1}""".format(rows["gold_tier_counter"],"'"+rows["user_id"]+"'")
            update_sql8="""update [finnair2-incentives].INCENT.UserPointAccounts set availablebalance={0}, lifetimevalue={0} where  pointaccountid='c959dc21-6577-46ce-8c52-86b2b1edc8ad' and userid={1}""".format(rows["platinum_tier_counter"],"'"+rows["user_id"]+"'")
            update_sql9="""update [finnair2-incentives].INCENT.UserPointAccounts set availablebalance={0}, lifetimevalue={0} where  pointaccountid='987833d7-775d-47e8-93fb-dab044b0cb88' and userid={1}""".format(rows["qualifying_flights"],"'"+rows["user_id"]+"'")
            update_sql10="""update [finnair2-incentives].INCENT.UserPointAccounts set availablebalance={0}, lifetimevalue={0} where  pointaccountid='76c66cdb-6f03-48d4-91d8-a0ad793d403a' and userid={1}""".format(rows["silver_tier_counter"],"'"+rows["user_id"]+"'")
            update_sql11="""update [finnair2-incentives].INCENT.UserPointAccounts set availablebalance={0}, lifetimevalue={0} where  pointaccountid='ba7c3f50-e4b4-4e44-8008-ea7b31048662' and userid={1}""".format(rows["status_hold_point"],"'"+rows["user_id"]+"'")
            update_sql12="""update [finnair2-incentives].INCENT.UserPointAccounts set availablebalance={0}, lifetimevalue={0} where  pointaccountid='48c78887-5e7f-43ee-88eb-17b01800e06f' and userid={1}""".format(rows["tier_qualifying_points"],"'"+rows["user_id"]+"'")
            
            count+=1

            print("user count:",count)

            # Execute sqls #
            cur.execute(update_sql1)
            cur.execute(update_sql2)
            cur.execute(update_sql3)
            cur.execute(update_sql4)
            cur.execute(update_sql5)
            cur.execute(update_sql6)
            cur.execute(update_sql7)
            cur.execute(update_sql8)
            cur.execute(update_sql9)
            cur.execute(update_sql10)
            cur.execute(update_sql11)
            cur.execute(update_sql12)

        else:
            new_rows.append(rows.values)

    df_user_not_found = df_user_not_found.append(pd.DataFrame(new_rows, columns=df_user_not_found.columns)).reset_index()
    df_user_not_found.drop(['index'], axis = 1, inplace=True)
    df_user_not_found.to_csv(point+'_USERNOTFOUND.csv', encoding='utf-8', index=False)

    print("All updates completed! Commiting the changes")

    
    #connect_con.commit()
    cur.close()
    
  except Exception as e:
    print("An error occured in point_seeding function:",e)
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
    
    # this function validates the loaded data with input file
    point_seeding(args.file,connect_con)
    
  except Exception as e:
    print("An error occured in main function:",e)
    raise e
    sys.exit(1)


if __name__=="__main__":
  print('-'*10,'Points Seeding script Started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*10)
  main()
  print('-'*10,'Points Seeding script Ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'-'*10)