def json_to_csv(data):
	''' This function is used to get the data from json and write it in a csv file '''
	try:
		
		data=eval(data)
		
		final_data=[[data["user"]["external_id"],data["user"]["email"],data["user"]["first_name"], \
					data["user"]["last_name"],data["user"]["address"],data["user"]["city"],data["user"]["state"],\
					data["user"]["zip"],data['user']['phone_numbers'][0]['phone_number']]]

		df_final = pd.DataFrame(final_data, columns = ['external_id', 'email','first_name','last_name','address','city','state','zip','phone_numbers'])

		print(df_final)

		df_final.to_csv(log_dir+'/'+'user_data_blains_{}.csv'.format(datetime.now().strftime("%Y%m%d_%H%M%S")), encoding='utf-8', index=False, mode='a', header=False) 
		
	except Exception as e:
		print('An error occured in json_to_csv function:',e)
		raise e


		# Json to csv conversion from response file
		#df_response.apply(lambda x: json_to_csv(x.response_from_api),axis=1)