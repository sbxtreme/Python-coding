####################################################################
# This Script breaks the big csv file into smaller csvs			   #
####################################################################

import pandas as pd 
rows = pd.read_csv("/Users/capgemini/Downloads/CSC.CW.Campaign.DoublePoints.Issue.ReceiptScan.10152020.final_2.csv", chunksize=687)
for i, chuck in enumerate(rows):
    chuck.to_csv('/Users/capgemini/scripts/pointdeposit_{}.csv'.format(i),index=False)