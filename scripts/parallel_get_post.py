#=====================================================================================================================================
# Title          : parallel_get_post.py
# Description    : The program calls api in async mode which decreases the execution time by 10X. Its a demo code and can be reused.
# Author         : Shobhit Bhatnagar
# Date           : 2020-04-08
# Version        : 1.0
# Python version : 3.7.3
#=====================================================================================================================================


import requests
import asyncio
import json
import pandas as pd
from datetime import datetime

################################################################# Hardcodings ##################################################################

getid_api_auth_token="Basic ZGI2ZGM3NjM5OGIyMTYwYzBmNzlhODYxMjMyODI4NDc3YTk4YTM1NjpkMmVlNTNjMzliNGY2YmQzOTgzMTA4YTU2ZWVlN2Y0NGZhZmRhMTkx"
get_id_header={"Accept":"application/json","Content-type": "application/json","Authorization": getid_api_auth_token}
get_id_url="https://api-lowes.ent-sessionm.com/priv/v1/apps/db6dc76398b2160c0f79a861232828477a98a356/external/users/"
get_id_header={"Accept":"application/json","Content-type": "application/json","Authorization": getid_api_auth_token}
datafile="/Users/capgemini/Downloads/customer_data.xlsx"

#################################################################################################################################################

def read_xls(input_file):
    '''This function reads the xls file and converts it into Pandas dataframe'''
    df=pd.read_excel(input_file)
    return df


def get_internal_id(get_id_url,ext_id,get_id_header):
    '''This function gets the internal sessionm id from the customer external id'''
    try:
        url=get_id_url+ext_id
        response=requests.get(url=url, headers=get_id_header) 
        userid=response.json()['user']['id']
        return response , userid

    except Exception as e:
        print('Error! Program failed while calling get_internal_id API :',e)

'''  
# this is the slowest approach 
def main():
    df=read_xls(datafile)
    output=df.apply(lambda x: get_internal_id(get_id_url,x.PRO_LOY_ID,get_id_header), axis=1)
    print(output)
'''

# this is the fastest approach
def main():  
    coroutine=[]
    df=read_xls(datafile)
    loop = asyncio.get_event_loop()
    for _,row in df.iterrows():
        coroutine.append(loop.run_in_executor(None, get_internal_id, get_id_url,row["PRO_LOY_ID"],get_id_header))

    output = loop.run_until_complete(asyncio.gather(*coroutine))
    print(output)


if __name__=="__main__":
    print(datetime.now().strftime("%b %d %Y %H:%M:%S"))
    main()
    print(datetime.now().strftime("%b %d %Y %H:%M:%S"))