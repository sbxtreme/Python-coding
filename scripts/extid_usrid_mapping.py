#===================================================================================================================================
# Title          : extid_usrid_mapping.py
# Description    : The program creates a mapping file with external and internal userids
# Author         : Shobhit Bhatnagar
# Date           : 2021-02-04
# Version        : 1.0
# Python version : 3.6
# Command line   : /opt/nifi/data/processor_input/pyenv/bin/python3 /opt/nifi/data/processor_input/scripts/extid_usrid_mapping.py
#====================================================================================================================================

import pandas as pd
import pymysql
import sys
from datetime import datetime


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


def create_mapping(core_con):
  """ This function creates a mapping file """
  try:

    df_final=pd.DataFrame(columns=['user_id','external_id'])

    sql_query="""select 
    p.user_id as user_id,
    ou.external_id as external_id
    from organization_users ou 
    left join players p on ou.player_id = p.id
    where ou.organization_id = (select id from organizations where name='finnair2')"""

    for df_extid_intid in pd.read_sql_query(sql_query, core_con,chunksize=20000):
      df_final=df_final.append(df_extid_intid)

    df_final.to_csv('/opt/nifi/data/processor_input/files/customer_id_mapping.csv', index=False,na_rep='')

  except Exception as e:
    print("An error occured in create_mapping function:",e)
    raise e
    sys.exit(1)


def main(argv=None):
  """ Program execution starts from here """
  try:

    # this function creates core db connection
    core_con=create_connection_coredb()

    # this function creates the mapping file
    create_mapping(core_con)

    print("Mapping file generated!")
    
  except Exception as e:
    print("An error occured in main function:",e)
    raise e
    sys.exit(1)


if __name__=="__main__":
  main()

