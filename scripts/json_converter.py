#=====================================================================================================================================
# Title			 : json_converter.py
# Description    : The program converts csv into nested json file
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-04-01
# Version        : 1.0
# Python version : 3.7.3
#=====================================================================================================================================

import pandas as pd
import json
import ast

# Hardcoding file names
input_filename='/Users/capgemini/Downloads/csc files/Catalog/catalogdata.csv'
output_filename='/Users/capgemini/Downloads/csc files/Catalog/catalogdata.json'

# To avoid warnings
pd.options.mode.chained_assignment = None

def create_json_from_csv(input_filename):
	''' This function will create json from csv file '''

	try:
		df=pd.read_csv(input_filename)

		# creating a dataframe to store distinct store id
		df_storeid= df['store_id'].unique()


		rec={} # this is for holding the complete json as a dictionary
		rec_hierarchy1={} # this is for holding group1 values as a dictionary
		rec_hierarchy2={} # this is for holding group2 values as a dictionary

		names_hierarchy1=[]
		names_hierarchy2=[]

		# looping through the storeid to create json array
		main_node=[]
		for stores in df_storeid:
			rec['store_id']=stores # ---1
			df_bystore=df.loc[df['store_id']==stores]
			df_hierarchy1=df_bystore.drop_duplicates(subset=['name','category_id','description'])

			nodes0=[]
			for _,values in df_hierarchy1.iterrows():
				rec_hierarchy1['name']=values['name']
				rec_hierarchy1['description']=str(values['description']).replace('nan','')
				rec_hierarchy1['category_id']=str(values['category_id'])
				rec_hierarchy1['subcategories']=[]

				#nodes.append(rec_hierarchy1.copy())
				names_hierarchy1.append(values['name'])

				df2=df_bystore.loc[df_bystore['name']==values['name']]	
				df_hierarchy2=df2.drop_duplicates(subset=['name1','category_id1','description1'])


				nodes1=[]
				for _,values in df_hierarchy2.iterrows():
					rec_hierarchy2['name']=values['name1']
					rec_hierarchy2['description']=str(values['description1']).replace('nan','')
					rec_hierarchy2['category_id']=str(values['category_id1'])
					rec_hierarchy2['children']=[]

					# creating child records array
					df3=df_bystore.loc[df_bystore['name1']==values['name1']]
					df3.fillna('', inplace=True)
					df3=df3.astype(str)

					nodes2=[]

					df_child=df3[['item_id','sku','name2']]
					df_child.rename(columns = {'item_id':'id','name2':'name'}, inplace = True) 

					nodes2=df_child[['id','sku','name']].to_dict(orient='records')
					# creating child records array

					rec_hierarchy2['children']=nodes2

					nodes1.append(rec_hierarchy2.copy()) # list of dictionaries
					names_hierarchy2.append(values['name1'])

				rec_hierarchy1['subcategories']=nodes1

				nodes0.append(rec_hierarchy1.copy()) # list of dictionaries

			rec['nodes']=nodes0 # ---2

			main_node.append(rec.copy()) # list of dictionaries

		main_node=ast.literal_eval(str(main_node).replace('.0',''))

		#print(main_node)

		# writing json data to an output file
		with open(output_filename, 'w', encoding='utf-8') as f:
			json.dump(main_node, f, ensure_ascii=False, indent=2)

	except Exception as e:
		raise(e)		

if __name__=="__main__":
	create_json_from_csv(input_filename)
	print('='*10,'JSON generated from CSV','='*10)

