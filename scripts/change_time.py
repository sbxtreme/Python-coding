import json
import os

filename = 'redemp_file_10000.json'

with open(filename, 'r') as f:
    data = json.load(f)
    for i in data:
    	i['modified_time']='2021-03-26T08:00:00.000000Z'

with open(filename, 'w') as f:
    json.dump(data, f, indent=4)