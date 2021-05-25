#=====================================================================================================================================
# Title			 : split_json_array.py
# Description    : The program splits large json array into indivisual files
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-04-01
# Version        : 1.0
# Python version : 3.7.3
#=====================================================================================================================================

import json

filename='redemp_file_4529.json'
newfilename='redemp_file_4529_'


def split_json(filename):
	''' this function splits a big json array into seperate files '''
	try:
		with open(filename, 'r') as file:
			json_data = json.load(file)

		for i in range (0,len(json_data)):

			array_of_json=[]
			array_of_json.append(json_data[i])
			newfile=newfilename+str(i)+'.json'
			
			with open(newfile, 'w') as file:
				json.dump(array_of_json, file, indent=2)

		print('========= File splitting completed =========')

	except Exception as e:
		raise (e)



if __name__=='__main__':
	split_json(filename)