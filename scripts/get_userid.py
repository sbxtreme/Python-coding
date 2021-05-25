#=======================================================================================================================================================
# Title          : get_userid.py
# Description    : The program gets user_id in the dict format using the mapping file
# Author         : Shobhit Bhatnagar
# Date           : 2021-02-04
# Version        : 1.0
# Python version : 3.6
# Command line   : /opt/nifi/data/processor_input/pyenv/bin/python3 /opt/nifi/data/processor_input/scripts/get_userid.py <json_payload> <mapping file>
#========================================================================================================================================================

import sys
from csv import DictReader
import json

# input parameters
json_payload=sys.argv[1]
mapping_file=sys.argv[2]

def get_userids(external_id,mapping_file):
  """ This function gets the userid from mapping file based on external_id """
  try:
    with open(mapping_file) as csvfile:
      reader = DictReader(csvfile)
      for row in reader:
        if (row['external_id'] == external_id):
          return dict(row)['user_id']

  except Exception as e:
    print("An error occured in get_userids function:",e)
    raise e
    sys.exit(1)

def main(argv=None):
  """ Program execution starts from here """
  try:

    print(json_payload)

    json_dict=json.loads(str(json_payload))
    external_id=json_dict['user_id']

    # this function gets user_id from mapping file and convert that into dict
    user_id=get_userids(external_id,mapping_file)
    json_dict['user_id']=user_id

    # convery dict to json object
    json_object = json.dumps(json_dict)
    print(json_object)

    
  except Exception as e:
    print("An error occured in main function:",e)
    raise e
    sys.exit(1)

if __name__=="__main__":
  main()