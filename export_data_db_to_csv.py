import os
import cx_Oracle
import csv
import time
import sys

dates=sys.argv[1]
dptno=sys.argv[2]
print(dates)

SQL='''select * from sbxtreme.emp_read where hiredate=to_date(:d,'YYYYMMDD') and deptno=:dno'''

#timestamp
timestr = time.strftime("%d%m%Y")

filename='emp_read_file_'+timestr+'.csv'
print(filename)
FILE=open(filename,"w",newline='');
output=csv.writer(FILE, dialect='excel')

#setting system variables
#os.putenv('ORACLE_HOME', '/u01/app/oracle/product/12.1.0/dbhome_1')
#os.putenv('LD_LIBRARY_PATH', '/u01/app/oracle/product/12.1.0/dbhome_1/lib')

#connection with Oracle DB
connection= cx_Oracle.connect("sbxtreme", "sbxtreme","localhost/xe")
cursor = connection.cursor()
cursor.execute(SQL,{"d":dates,"dno":dptno})
columns = [i[0] for i in cursor.description]
output.writerow(columns)

for row in cursor:
	output.writerow(row)
cursor.close()
connection.close()
FILE.close()
