####################################################################
# This Script generates the actual file required for point seeding #
####################################################################


import pandas as pd
import csv


path ='/Users/capgemini/Desktop/SessionM/Work/csc/csc_files/customerpoints/prod'
core_users_filename='Data_from_core_prod.csv'
connect_userspoints_from_loyaltree='Older_customers_segment2_PROD.csv'

'''
-- core users:  query to get all the users with external_ids and userids
select external_id,user_id from organization_users ou inner join players p 
on ou.player_id= p.id where ou.organization_id='2' and p.rewards_system_id='227'
'''

df_core_users= pd.read_csv(path+'/'+core_users_filename)

df_connect_users= pd.read_csv(path+'/'+connect_userspoints_from_loyaltree,usecols=["external_id", "point_balance"])

df_merged = pd.merge(df_core_users, df_connect_users, on='external_id')

df_merged.to_csv(path+'/'+'Actual_point_seeding_segment2_PROD.csv', index=False)

