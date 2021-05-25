#======================================================================================================
# Description         : The below script does the following:
#						a) Get the data from datalake and perform ETL
#						b) Generate a fullfilment file
#						c) Log all the details about the program
#						d) Delete the log files and processed files which are older than 7 days
# Author 		      : Shobhit Bhatnagar
# Date                : 2021-03-01
# Version        	  : 1.0
# Glue Python version : 3.6
#=======================================================================================================

import sys
import json
import boto3
import copy
import time
import requests
import pandas as pd
import awswrangler as wr
from datetime import datetime,timedelta


################################################# Global Setting / Variables #################################################
bucket="choicehotels-stg-sessionm-com"
key="glue"
database="choicehotels_mazu_std"
query_result_location="s3://teams-stg-sessionm-com/integration/athena/choicehotels/"
output_filename=key+'/Fulfillment_elite_points_v2_'+datetime.now().strftime("%Y%m%d%H%M%S")+'.csv'
log_filename='s3://choicehotels-stg-sessionm-com/glue/logs/fulfillment_job_logs'
glue_bucket_log_key="glue/logs"
msg_log="Log files older than 7 days are deleted from s3://choicehotels-stg-sessionm-com/glue/logs/fulfillment_job_logs/"
log_file_pattern='fulfillment_job_logs'
s3 = boto3.resource('s3')
###############################################################################################################################


def write_data_to_s3(output_df):
	""" This function writes data to s3 """
	try:
		pass

	except Exeception as e:
		print(e)
		raise e


def file_creation_logic(df_base_data,df_stay_id):
	""" The function is used for creation of output dataframe which can be written in a csv file """
	try:
		pass

	except Exeception as e:
		print(e)
		raise e


def main():
	""" Program execution starts from here """
	try:
		print('='*5,"Glue Job Execution Started on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)
		query_for_base_data="""with subquery1 as (
						with campaign_activity_data as (                                  
						  with temp as 
						   (select distinct
						    ca.user_id,
						    ca.campaign_id,
						    cach.external_id,
						    th.pos_transaction_key,
						    tp.payment_source,
						    ca.time_stamp
						    from campaign_activity ca
						    join transaction_headers th
						      on upper(ca.transaction_id)=upper(th.transaction_id)
						    join campaign_achievements cach
						      on ca.campaign_id = cach.ad_campaign_id
						    join transaction_payments tp
						      on lower(tp.transaction_id) = lower(th.transaction_id)
						    where ca.action in ('composite:achievement:event','goal:achievement:event')
						    and ca.user_id in
						     (select user_id
						      from user_point_transactions
						      where date(created_at) >= current_date - interval '2' day
						      and reference_type = 'Behavior') )
						select user_id, external_id, pos_transaction_key, campaign_id, payment_source, time_stamp
						from temp
						)
						select distinct cad.user_id,
						cach.achievement_id,
						array_agg(cad.payment_source) as trans_ids,
						count(cad.pos_transaction_key) as trans_ids_count,
						upt.point_transaction_id,
						upt.point_modification,
						upt.time_of_occurrence,
						cad.external_id,
						upt.reference_id,
						upt.transaction_id,
						cad.campaign_id
						from campaign_activity_data cad
						join user_point_transactions upt
						  on cad.user_id=upt.user_id
						  and cad.external_id = upt.reference_id
						  and upt.audit_type_bitmask <> 4
						join campaign_achievements cach
						  on lower(upt.reference_id) = cach.external_id
						join campaign_attributes catt
						  on catt.campaign_id = cad.campaign_id
						group by cad.user_id, cach.achievement_id, upt.point_transaction_id, upt.point_modification, 
						upt.time_of_occurrence, cad.external_id, upt.reference_id, upt.transaction_id, 
						cad.campaign_id
						),
						registered_timestamps as 
						  (
						    select 
						    user_id,
						    campaign_id,
						    created_at
						    from campaign_activity
						    where action = 'achievement:opt_in'
						    ),  
						extracted_behavior_datetimes as (
						  with extracted_date_data as (
						    select
						      regexp_extract_all(data, '[0-9][^\s'']*') as datetime_array,
						      achievement_id
						    FROM
						      event_filters ef_in
						    where
						      ef_in.filter_handler = 'event/filter/date'
						    )
						  select
						    edd.datetime_array [1] as behavior_start_datetime,
						    edd.datetime_array [2] as behavior_end_datetime,
						    edd.achievement_id,
						    cach_in.ad_campaign_id
						  from
						    extracted_date_data edd
						    join campaign_achievements cach_in on cach_in.achievement_id = edd.achievement_id
						)
						/* ##### main query with the complete logic EXCEPT WINDOW FUNCTIONS ##### */ 
						select distinct 
						eum.external_user_id AS account_number,
						eum.external_user_id_type AS account_type,
						upt.point_modification,
						upt.point_transaction_id,
						date_format(upt.time_of_occurrence, '%Y-%m-%dT%H:%i:%sZ') AS created_at,
						COALESCE(date_format(rt.created_at, '%Y-%m-%dT%H:%i:%sZ'), date_format(catt.starts_at, '%Y-%m-%dT%H:%i:%sZ')) AS registered_at,
						sq1.campaign_id,
						COALESCE(json_extract_scalar(catt.custom_payload,'$.description'), 'Description Not Found') as campaign_desc,
						sq1.external_id AS promo_id,
						cach.name AS promo_name,
						COALESCE(date_format(from_iso8601_timestamp(ebd.behavior_start_datetime), '%Y-%m-%dT%H:%i:%sZ'), date_format(catt.starts_at, '%Y-%m-%dT%H:%i:%sZ')) AS promo_start_date,
						COALESCE(date_format(from_iso8601_timestamp(ebd.behavior_end_datetime), '%Y-%m-%dT%H:%i:%sZ'), date_format(catt.ends_at, '%Y-%m-%dT%H:%i:%sZ')) AS promo_end_date,
						date_format(catt.starts_at, '%Y-%m-%dT%H:%i:%sZ') AS campaign_start_date,
						date_format(catt.ends_at, '%Y-%m-%dT%H:%i:%sZ') AS campaign_end_date
						from subquery1 sq1
						join transaction_payments tp
						  on lower(tp.transaction_id) = lower(sq1.transaction_id)
						join user_point_transactions upt 
						  on contains(sq1.trans_ids, lower(tp.payment_source))
						  and lower(sq1.user_id) = lower(upt.user_id)
						  and lower(sq1.reference_id) = lower(upt.reference_id)
						  and upt.time_of_occurrence = sq1.time_of_occurrence
						join campaign_achievements cach on cach.achievement_id = sq1.achievement_id
						join campaign_attributes catt on catt.campaign_id = sq1.campaign_id 
						left join registered_timestamps rt on rt.campaign_id = sq1.campaign_id and rt.user_id = sq1.user_id
						left outer join extracted_behavior_datetimes ebd on ebd.ad_campaign_id = cach.ad_campaign_id
						join external_user_mappings eum 
						  on lower(eum.user_id) = lower(sq1.user_id)
						     and eum.external_user_id_type = 'customer_id'"""

		query_for_stay_id="""with subquery as (
								SELECT transaction_id,achievement_id FROM campaign_activity WHERE achievement_id IN
								(
									SELECT DISTINCT(ca.achievement_id)
									FROM user_point_transactions upt INNER JOIN campaign_achievements ca
									ON upt.reference_id=ca.external_id
									WHERE upt.reference_type='Behavior'
									AND upt.data_date = Date('2020-12-14') -- this is used for testing. It should be below commented conditon
									-- AND date(created_at) = current_date - interval '1' day 
									) AND action IN ('composite:achievement:event','goal:achievement:event')
								)
								select distinct(request_id) as request_id,user_id,time_stamp from subquery sb 
								inner join campaign_event ce on upper(ce.transaction_id)= upper(sb.transaction_id)
								order by user_id,time_stamp"""

		df_base_data = wr.athena.read_sql_query(sql=query_for_base_data,database=database,s3_output=query_result_location)
		df_stay_id = wr.athena.read_sql_query(sql=query_for_stay_id,database=database,s3_output=query_result_location)
		
		print(df_base_data.shape[0])
		print(df_stay_id.shape[0])
		
		print('='*5,"Glue Job Execution Ended on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)


	except Exception as e:
		print(e)
		raise e


if __name__== "__main__":
	main()