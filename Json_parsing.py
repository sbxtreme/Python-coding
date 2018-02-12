import json

# json.load(f): loads json data from a file
# json.loads(s): loads json data from a string
# json.dump(j,f): write json data to a file
# json.dumps(j): o/p string in json format


#open a file and read json data
json_file = open("data.txt",'r',encoding='utf-8')

# details will contain data in key value format of python dictionary 
details = json.load(json_file)

# closing a file
json_file.close()

print('\n',details)

####################### If we get json data in string format then use json.loads(string) to convert into python dictonaries #######################

# example:
json_string="""
{
	"name": "Shobhit",
	"age": 26,
	"geek":true,
	"alcoholic":false,
	"otherdetails":null,
	"address": {
		"street": "MGROAD",
		"city": "Gurgaon",
		"state": "Haryana",
		"pin": 122001
	},
	"organization": "ITC",
	"technology": ["Mongodb", "Machine Learning", "Python", "SQL", "Informatica", "UNIX"]
} 
"""

# here json_data stored in string is converted into python dictionary with key values
value=json.loads(json_string)

print('\n',value)


#################### to write the data in json format in a file using python dictionary ##################

data={"name":"shobhit","age":27,"alcoholic":False,"others":None}
file2= open('json_file.json','w',encoding='utf-8')
json.dump(data,file2,ensure_ascii=False,indent=2)

#################### to write the json data in a string in python #####################
json_string=json.dumps(data,file2,ensure_ascii=False,indent=2,sort_keys=True)
print(type(json_string)) # <class 'str'>
print('\n',json_string)

####################### convert json data into Python pandas dataframes ###################
