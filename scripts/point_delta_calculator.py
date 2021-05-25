#=========================================================================================================================================================================================
# Title         :point_delta_calculator.py
# Description   :The program get the points from database and calculate point delta
# Author        :Shobhit Bhatnagar
# Date          :2020-11-19
# Version       :1.0
# Python version:3.6
# Command line  :/opt/nifi/data/processor_input/pyenv/bin/python3 /opt/nifi/data/processor_input/scripts/point_delta_calculator.py --points_in_file <all values with spaces> --userid <userid>
# NIFI command line : /opt/nifi/data/processor_input/scripts/point_delta_calculator.py;--points_in_file;${auto_renewal};${award_points};${ay_lifetime_tier_points};${ay_qualifying_flights};${ay_qualifying_revenue};${ay_tier_qualifying_points};${gold_tier_counter};${platinum_tier_counter};${qualifying_flights};${silver_tier_counter};${status_hold_point};${tier_qualifying_points};--user_id;${user_id}

#get user_id for 100k users
#get the current point balance for all 12 point accounts at the same time for all 100k users
#delta between the file and w/e the query returns
#transform the structure to jsons
#split it into rows
#=========================================================================================================================================================================================

import json
import pandas as pd
import pyodbc
import argparse
import sys
from datetime import datetime


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


def delta(string_val):
    points=string_val.split('|')[0]
    account_id=string_val.split('|')[1]
    source_id=string_val.split('|')[2]
    if int(points) != 0:
        return {"point_value":int(points),"point_source_id":source_id,"point_account_id":account_id}



def point_calculator():
  """ This function calculates the points based on the database and file """
  try:

    CLI=argparse.ArgumentParser()
    CLI.add_argument("--points_in_file",nargs="*",type=int,default=[])
    CLI.add_argument("--user_id")
    args = CLI.parse_args()

    # input args #
    point_list=args.points_in_file
    user_id=args.user_id

    # Getting values from list #
    auto_renewal_file=point_list[0]
    award_points_file=point_list[1]
    ay_lifetime_tier_points_file=point_list[2]
    ay_qualifying_flights_file=point_list[3]
    ay_qualifying_revenue_file=point_list[4]
    ay_tier_qualifying_points_file=point_list[5]
    gold_tier_counter_file=point_list[6]
    platinum_tier_counter_file=point_list[7]
    qualifying_flights_file=point_list[8]
    silver_tier_counter_file=point_list[9]
    status_hold_point_file=point_list[10]
    tier_qualifying_points_file=point_list[11]

    # this function creates connect db connection
    connect_con=create_connection_connectdb()


    # Query to get available points for all the point accounts ( 0 in case if available point is null in the database )
    sql_query="""
                select 
                (select isnull((select AvailableBalance
                from [finnair2-incentives].INCENT.UserPointAccounts 
                where UserID = '{0}'
                and pointaccountid='b617f4b9-6837-49d6-8f41-feb8050266dd'),0)) as auto_renewal_db,

                (select isnull((select AvailableBalance
                from [finnair2-incentives].INCENT.UserPointAccounts 
                where UserID = '{0}'
                and pointaccountid='eaf7d27b-5400-4f2d-825d-c27720d42edf'),0)) as award_points_db,

                (select isnull((select AvailableBalance
                from [finnair2-incentives].INCENT.UserPointAccounts 
                where UserID = '{0}'
                and pointaccountid='a4f8b9c7-3cd6-414b-b62f-cef79a5e3849'),0)) as ay_lifetime_tier_points_db,

                (select isnull((select AvailableBalance
                from [finnair2-incentives].INCENT.UserPointAccounts 
                where UserID = '{0}'
                and pointaccountid='95b23b22-3d21-4b2c-8c2e-f7506e2104ba'),0)) as ay_qualifying_flights_db,

                (select isnull((select AvailableBalance
                from [finnair2-incentives].INCENT.UserPointAccounts 
                where UserID = '{0}'
                and pointaccountid='82b9e1fd-9bc8-4d60-ad6b-d812e3572185'),0)) as ay_qualifying_revenue_db,

                (select isnull((select AvailableBalance
                from [finnair2-incentives].INCENT.UserPointAccounts 
                where UserID = '{0}'
                and pointaccountid='6a21d0f0-27eb-4d83-8712-de9d0cce6a25'),0)) as ay_tier_qualifying_points_db,

                (select isnull((select AvailableBalance
                from [finnair2-incentives].INCENT.UserPointAccounts 
                where UserID = '{0}'
                and pointaccountid='fa0979b3-f90d-4b4e-80f9-2a94c9c49feb'),0)) as gold_tier_counter_db,

                (select isnull((select AvailableBalance
                from [finnair2-incentives].INCENT.UserPointAccounts 
                where UserID = '{0}'
                and pointaccountid='c959dc21-6577-46ce-8c52-86b2b1edc8ad'),0)) as platinum_tier_counter_db,

                (select isnull((select AvailableBalance
                from [finnair2-incentives].INCENT.UserPointAccounts 
                where UserID = '{0}'
                and pointaccountid='987833d7-775d-47e8-93fb-dab044b0cb88'),0)) as qualifying_flights_db,

                (select isnull((select AvailableBalance
                from [finnair2-incentives].INCENT.UserPointAccounts 
                where UserID = '{0}'
                and pointaccountid='76c66cdb-6f03-48d4-91d8-a0ad793d403a'),0)) as silver_tier_counter_db,

                (select isnull((select AvailableBalance
                from [finnair2-incentives].INCENT.UserPointAccounts 
                where UserID = '{0}'
                and pointaccountid='ba7c3f50-e4b4-4e44-8008-ea7b31048662'),0)) as status_hold_point_db,
                
                (select isnull((select AvailableBalance
                from [finnair2-incentives].INCENT.UserPointAccounts 
                where UserID = '{0}'
                and pointaccountid='48c78887-5e7f-43ee-88eb-17b01800e06f'),0)) as tier_qualifying_points_db""".format((user_id))

    df_points=pd.read_sql_query(sql_query, connect_con)
    df_points=df_points.astype(int)

    # Substracting points from file - points from database
    auto_renewal_final= auto_renewal_file-df_points.at[0,'auto_renewal_db']
    award_points_final= award_points_file-df_points.at[0,'award_points_db']
    ay_lifetime_tier_points_final= ay_lifetime_tier_points_file-df_points.at[0,'ay_lifetime_tier_points_db']
    ay_qualifying_flights_final= ay_qualifying_flights_file-df_points.at[0,'ay_qualifying_flights_db']
    ay_qualifying_revenue_final= ay_qualifying_revenue_file-df_points.at[0,'ay_qualifying_revenue_db']
    ay_tier_qualifying_points_final= ay_tier_qualifying_points_file-df_points.at[0,'ay_tier_qualifying_points_db'] 
    gold_tier_counter_final= gold_tier_counter_file-df_points.at[0,'gold_tier_counter_db']
    platinum_tier_counter_final= platinum_tier_counter_file-df_points.at[0,'platinum_tier_counter_db']
    qualifying_flights_final= qualifying_flights_file-df_points.at[0,'qualifying_flights_db']
    silver_tier_counter_final= silver_tier_counter_file-df_points.at[0,'silver_tier_counter_db']
    status_hold_point_final= status_hold_point_file-df_points.at[0,'status_hold_point_db']
    tier_qualifying_points_final= tier_qualifying_points_file-df_points.at[0,'tier_qualifying_points_db']

    list_of_points_with_account_id=[ \
    str(auto_renewal_final)+'|'+'b617f4b9-6837-49d6-8f41-feb8050266dd'+'|'+'432aa0f2-ae15-42b1-bc53-897afaa786e2', \
    str(award_points_final)+'|'+'eaf7d27b-5400-4f2d-825d-c27720d42edf'+'|'+'584efe18-5f2a-4138-ac09-49a5787ae87c', \
    str(ay_lifetime_tier_points_final)+'|'+'a4f8b9c7-3cd6-414b-b62f-cef79a5e3849'+'|'+'1333f59a-1187-464c-9109-2a1d07f45e28', \
    str(ay_qualifying_flights_final)+'|'+'95b23b22-3d21-4b2c-8c2e-f7506e2104ba'+'|'+'3e4cc97b-bffb-4499-8284-310b78298d95', \
    str(ay_qualifying_revenue_final)+'|'+'82b9e1fd-9bc8-4d60-ad6b-d812e3572185'+'|'+'8a1deb52-1e2d-4e03-8aa3-ec5dd65aa046', \
    str(ay_tier_qualifying_points_final)+'|'+'6a21d0f0-27eb-4d83-8712-de9d0cce6a25'+'|'+'1333f59a-1187-464c-9109-2a1d07f45e28', \
    str(gold_tier_counter_final)+'|'+'fa0979b3-f90d-4b4e-80f9-2a94c9c49feb'+'|'+'2b7d3469-91f5-42db-8cc8-ea1ed60e4f3b', \
    str(platinum_tier_counter_final)+'|'+'c959dc21-6577-46ce-8c52-86b2b1edc8ad'+'|'+'2b7d3469-91f5-42db-8cc8-ea1ed60e4f3b', \
    str(qualifying_flights_final)+'|'+'987833d7-775d-47e8-93fb-dab044b0cb88'+'|'+'3e4cc97b-bffb-4499-8284-310b78298d95', \
    str(silver_tier_counter_final)+'|'+'76c66cdb-6f03-48d4-91d8-a0ad793d403a'+'|'+'2b7d3469-91f5-42db-8cc8-ea1ed60e4f3b', \
    str(status_hold_point_final)+'|'+'ba7c3f50-e4b4-4e44-8008-ea7b31048662'+'|'+'432aa0f2-ae15-42b1-bc53-897afaa786e2', \
    str(tier_qualifying_points_final)+'|'+'48c78887-5e7f-43ee-88eb-17b01800e06f'+'|'+'1333f59a-1187-464c-9109-2a1d07f45e28', \
    ]

    json_list=[]
    for data in list_of_points_with_account_id:
        json_list.append(delta(data))

    json_list = list(filter(None, json_list))

    json_object=json.dumps(json_list)

    print(json_object)

    
  except Exception as e:
    print("An error occured in point_calculator function:",e)
    raise e
    sys.exit(1)



if __name__=="__main__":
  point_calculator()