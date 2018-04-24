# The below code is for subprocess in python
import subprocess as sp
sp.call(['ls -ltr'],shell=True)
sp.call(['df -k .'],shell=True)

# the below code stores the output of shell in a variable
output= sp.check_output(['df -k .'],shell=True)

# the below print statement prints the disk space of a server on which program is running
print('Disk space is:',str(str(output).split('%')[1])[-3:],'%')


# ###############################################################################

# The below code is for configparser in python

import configparser
cf=configparser.SafeConfigParser()
cf.read('sbx_config_file.ini') # passing the configuration file name
d1= 'DB'
d2= 'EOD_marker_config'

print('\n',cf,'\n')

print(cf.sections(),'\n') # this will display the names of various sections in config file

print(list(cf['DB'].keys()),'\n') # this will display all the keys in a config file by passing section name
print(list(cf['DB'].values())) # this will display all the values of keys in a config file by passing section name

print('\n'+cf['DB']['db_name']) 
print('\n'+cf['DB']['db_tech'])
print('\n'+cf['DB']['db_usage'])


# below is the standard method to get the values for a key from Config file.

dbname = cf.get(d1,'db_add')
db_app= cf.get(d1,'db_usage')

queue_name=cf.get(d2,'queue_name')
queue_add=cf.get(d2,'queue_usage')

print('\nDB_NAME is :'+dbname)
print('\nDB_APP is :'+db_app)

print('\nQueue_name is :'+queue_name)
print('\nQueue_addr is :'+queue_add)
