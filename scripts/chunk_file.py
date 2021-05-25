#!/usr/bin/env python
#=====================================================================================================================================
# Title			 : chunk_file.py
# Description    : The program splits the json file based on chunk size
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-04-01
# Version        : 1.0
# Python version : 3.7.3
#======================================================================================================================================

import json
import sys
import os


# the below is the input params recieved from command line of this script
original_file=sys.argv[1]
new_file=sys.argv[2]
chunks=sys.argv[3]

try:
	# give the absoulute file path
	with open(original_file) as file_qc:
		data=json.loads(file_qc.read())

	# set the chunk size
	n = int(chunks)

	final = [data[i * n:(i + 1) * n] for i in range((len(data) + n - 1) // n )]

	count=1

	print('------- Chuncking the files: Process started! -------')

	for chunks in final:
		# the below path is the absolute file path for the new file created in chunks
		output_file=new_file+'-'+str(count)+'chunkfile_connect_transaction.json'
		print(output_file)
		with open(output_file,'w') as outfile:
			outfile.write(json.dumps(chunks))

		count+=1

	print('------- Chuncking the files: Process ended!-------')
except Exception as e:
	print('Error occured in the script:\n',e)