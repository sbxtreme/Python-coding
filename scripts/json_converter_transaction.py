#=====================================================================================================================================
# Title			 : json_converter_transaction.py
# Description    : The program converts csv into nested json file for transactions
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-04-08
# Version        : 1.0
# Python version : 3.7.3
#=====================================================================================================================================

import pandas as pd
import numpy as np
import json
import time
from datetime import datetime
import sys

anonymous_flag=sys.argv[1]
input_file=sys.argv[2]



# Hardcoding file names
#input_filename='/Users/capgemini/Documents/anonymous_trans.csv'
output_filename=input_file+'.json'

def create_json_from_csv(input_filename):
	''' This function will create json from csv file '''
	try:
		df=pd.read_csv(input_filename)
		df.fillna('',inplace=True)
		
		# creating a dataframe to store distinct transaction_ids
		df_tranid= df['transaction_id'].unique()
		
		rec={} # this is for holding the complete json as a dictionary based on transactions
		rec_items={} # this is for holding items as a dictionary
		rec_payments={} # this is for holding payments as a dictionary
		rec_discounts={} # this is for holding discounts as a dictionary
		main_node=[] # this is for holding complete json as an array


		# looping through the transactionids to create json array
		for tran_id in df_tranid:
			df_tran=df.loc[df['transaction_id']==tran_id]


			df_main=df_tran.drop_duplicates(subset=['transaction_id','user_id','store_id'])

			nodes1=[]
			nodes2=[]
			nodes3=[]
			for _,values in df_main.iterrows():
				# creating root level dict
				rec['store_id']=str(values['store_id'])
				
				# user_id not required for anonymous transactions (29-sep changes)
				if anonymous_flag=='N':
					rec['user_id']=str(values['user_id'])
				else:
					pass

				rec['pos_employee_id']=str(values['pos_employee_id'])
				rec['table_id']=str(values['table_id'])
				rec['guest_count']=values['guest_count']
				rec['is_closed']=bool(values['is_closed'])
				rec['is_voided']=bool(values['is_voided'])
				rec['transaction_id']=str(values['transaction_id'])
				rec['from_transaction_id']=str(values['from_transaction_id'])
				rec['subtotal']=values['subtotal']
				rec['tax_total']=values['tax_total']
				rec['open_time']=str(values['open_time']).replace(' ','T')+'Z'
				rec['modified_time']=str(values['modified_time']).replace(' ','T')+'Z'
				rec['guest_receipt_code']=str(values['guest_reception_code'])
				rec['channel']=values['channel']
				rec['items']=[]
				rec['payments']=[]
				rec['discounts']=[]

				df2=df_tran.loc[df_tran['transaction_id']==values['transaction_id']]	
				df_items=df2.drop_duplicates(subset=['line_id'])

				# changes for anonymous transactions (29-sep changes)
				if anonymous_flag=='N':
					df_payments=df2.drop_duplicates(subset=['payment_id','userid1','receipt_code'])
				else:
					df_payments=df2.drop_duplicates(subset=['payment_id','userid1','receipt_code'],keep=False)

				df_discounts=df2.drop_duplicates(subset=['reference_id'])
				# adding stack_order as autoincremental column in discount dataframe
				df_discounts.insert(0, 'stack_order', range(1, 1 + len(df_discounts))) 
				
				for _,values in df_items.iterrows():
					rec_items['line_id']=str(values['line_id'])
					rec_items['item_id']=str(values['item_id'])
					rec_items['quantity']=values['quantity']
					rec_items['unit_price']=values['unit_price']
					rec_items['subtotal']=values['subtotal1']
					rec_items['tax_included']=values['tax_included']
					nodes1.append(rec_items.copy())

				rec['items']=nodes1

				for _,values in df_payments.iterrows():
					rec_payments['payment_id']=str(values['payment_id'])
					rec_payments['amount']=values['amount']
					rec_payments['type']=str(values['type'])
					rec_payments['payment_time']=str(values['payment_time']).replace(' ','T')+'Z'

					# user_id and user_id_type not required for anonymous transactions (29-sep changes)
					if anonymous_flag=='N':
						rec_payments['user_id']=str(values['userid1'])
						rec_payments['user_id_type']=str(values['user_id_type'])
					else:
						pass

					rec_payments['receipt_code']=str(values['receipt_code'])
					nodes2.append(rec_payments.copy())

				rec['payments']=nodes2

				for _,values in df_discounts.iterrows():
					rec_discounts['reference_id']=str(values['reference_id'])
					rec_discounts['reference_id_type']=str(values['reference_id_type'])
					rec_discounts['pos_discount_id']=str(values['pos_discount_id'])
					rec_discounts['status']=str(values['status'])
					rec_discounts['display_name']=str(values['display_name'])
					rec_discounts['discount_source']=str(values['discount_source'])
					rec_discounts['amount']=values['amount1']

					# Below changes are done on 17-sep-2020

					if values['applied_time'] == '':
						rec_discounts['applied_time']= ''
					else:
						rec_discounts['applied_time']=str(values['applied_time']).replace(' ','T')+'Z'


					rec_discounts['user_id']=str(values['user_id2'])

					if values['amount1'] == '':
						rec_discounts['stack_order']=''
					else:
						rec_discounts['stack_order']=values['stack_order']
					
					# checking the dict rec_discounts for all the keys with ''. If yes True else False 
					dict_chk_flag=all(value == '' for value in rec_discounts.values())

					if dict_chk_flag == True:
						pass
					else:
						nodes3.append(rec_discounts.copy())


					# Above changes are done on 17-sep-2020


				rec['discounts']=nodes3


				main_node.append(rec.copy())
		#print(main_node)

		# writing json data to an output file
		with open(output_filename, 'w', encoding='utf-8') as f:
			json.dump(main_node, f, ensure_ascii=False, indent=2)

	except Exception as e:
		raise (e)


if __name__ == "__main__":
	#print("IMPORTANT MESSAGE: Once json file is generated, replace 'NOVAL' with nothing in text editor") 29-sep changes
	print('='*10,'Json converter process started on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*10)
	create_json_from_csv(input_filename)
	print('>>>> Transaction JSON generated from CSV <<<<',)
	print('='*10,'Json converter process ended on:',datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*10)


