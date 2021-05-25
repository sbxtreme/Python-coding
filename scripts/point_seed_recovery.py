#==============================================================================
# Title             : point_recovery.py
# Author            : Shobhit Bhatnagar
# Date              : 2020-12-14
# Version           : 1.0
# Python version    : 3.6
# Command line      : python3 point_recovery.py <mismatch file absolute path>
#===============================================================================

import sys
import csv
import os.path
import pandas as pd
from pathlib import Path

mismatch_file=sys.argv[1]

def recovery_logic():
	try:
		appended_data = []
		files = [f for f in Path.cwd().iterdir() if f.match("new_finnair_points*.csv")]
		df_mismatch=pd.read_csv(mismatch_file,usecols = ['external_id'])

		for i in files:
			df_orig_file=pd.read_csv(os.path.basename(i))
			final_df=pd.merge(df_orig_file,df_mismatch,on='external_id')
			appended_data.append(final_df)

		combined_df = pd.concat(appended_data)

		# replacing content for csv creation
		combined_df.replace('nan',"",inplace=True)
		combined_df.replace(False,'false',inplace=True)
		combined_df.replace(True,'true',inplace=True)

		# writing data to csv
		combined_df.to_csv("recovered_pointseeding_records.csv", index=False,na_rep='',quoting=csv.QUOTE_NONE)

		print("Recovery File Generated!")

	except Exception as e:
		print("An error occured in recovery_logic function:",e)
		raise e
		sys.exit(1)

if __name__=="__main__":
	recovery_logic()