from datetime import timedelta, date
import os


# hardcoded values
#start_dt = date(2020, 1,7 ) # this needs to be uncommented
start_dt=date.today() # this needs to be commented
end_dt = date.today()
datelist=[]
command="sudo /opt/nifi/data/processor_input/pepcoin/pepcoin_venv/bin/python3.6 /opt/nifi/data/processor_input/pepcoin/script/pepcoin_inactive_users.py"

def date_range(date1, date2):
	""" The below function get the dates from range passed """
	for n in range(int ((date2 - date1).days)+1):
		yield date1 + timedelta(n)

# creating datelist to store all the dates
for dt in date_range(start_dt, end_dt):
    datelist.append(dt.strftime("%Y-%m-%d"))


def calling_script(datelist):
	""" The below function calls the script in loop with an interval of 10 mins """
	for rundate in datelist:
		print('----------------- Running script for:',rundate,'-----------------')
		print('Command line to execute: ',command+' '+rundate)
		os.system(command+' '+rundate)


if __name__=="__main__":
	""" Function to call the scrtipt for point deduction """
	calling_script(datelist)