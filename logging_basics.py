import logging

'''below code to change the logging level to debug and then use logging.debug() 
 method to print the output on console. Previously it was not printing as the default level 
 was set to warnings which print warnings if any.'''

''' There are 5 important levels of logging
1) DEBUG  : detailed info typically of interest when diagnosing any problem.
2) INFO  : its a kind of conformation that things are working as expected
3) WARNING : it will throw some warning and gives an indication that something might break
			  ex: disk space low 
4) ERROR :  Helps to provide information about some problem which stops execution of code. 
5) CRITICAL : a serious error stating that program will terminate.
'''

''' default level of logging is set to warning which means untill any warning comes 
statement 1,2,3,4 will not print anything.

statement 11,22,33,44 are printing the results as warning on the console.

statement 111,222,333,444 are printing the result using logging.debug() method as
the logging method is changed to DEBUG

statement 1111,2222,3333,4444 are used for information and the same is written
in the log file hence used logging.info() method
'''

#logging.basicConfig(level=logging.DEBUG)

''' to write logging details in a file use the below code''' 
#logging.basicConfig(filename='test_logfile.txt',level=logging.DEBUG)

''' to add more details and format in the logged data in a file use the below code:
'''
'''logging.basicConfig(filename='test_log.txt',level=logging.DEBUG,
					format='%(asctime)s:%(levelname)s:%(message)s')'''

'''another logging method which can be tried out is INFO.Below is the code'''

logging.basicConfig(filename='test1_log.txt',level=logging.INFO,
					format='%(asctime)s:%(levelname)s:%(message)s')

def add(x,y):
	return x+y

def mul(x,y):
	return x*y

def div(x,y):
	return x/y

def sub(x,y):
	return x-y

num1=8
num2=9

add_res=add(num1,num2)
#print('add result : {}+{}={}'.format(num1,num2,add_res))
#logging.debug('add result : {}+{}={}'.format(num1,num2,add_res)) #1
#logging.warning('add result : {}+{}={}'.format(num1,num2,add_res)) #11
#logging.debug('add result : {}+{}={}'.format(num1,num2,add_res)) #111
logging.info('add result : {}+{}={}'.format(num1,num2,add_res)) #1111

sub_res=sub(num1,num2)
#print('sub result : {}-{}={}'.format(num1,num2,sub_res))
#logging.debug('sub result : {}-{}={}'.format(num1,num2,sub_res)) #2
#logging.warning('sub result : {}-{}={}'.format(num1,num2,sub_res)) #22
#logging.debug('sub result : {}-{}={}'.format(num1,num2,sub_res)) #222
logging.info('sub result : {}-{}={}'.format(num1,num2,sub_res)) #2222

mul_res=mul(num1,num2)
#print('mul result : {}*{}={}'.format(num1,num2,mul_res)) 
#logging.debug('mul result : {}*{}={}'.format(num1,num2,mul_res)) #3
#logging.warning('mul result : {}*{}={}'.format(num1,num2,mul_res)) #33
#logging.debug('mul result : {}*{}={}'.format(num1,num2,mul_res)) #333
logging.info('mul result : {}*{}={}'.format(num1,num2,mul_res)) #3333

div_res=div(num1,num2)
#print('divide result : {}/{}={}'.format(num1,num2,div_res))
#logging.debug('divide result : {}/{}={}'.format(num1,num2,div_res)) #4
#logging.warning('divide result : {}/{}={}'.format(num1,num2,div_res)) #44
#logging.debug('divide result : {}/{}={}'.format(num1,num2,div_res)) #444
logging.info('divide result : {}/{}={}'.format(num1,num2,div_res)) #4444


''' the output in the log file generated would be something like DEBUG:root:add result : 10+20=30 . here root is the default logger.
there is a disadvantage of root logger if we are importing any module which already is using root logger.

ex: script 1-- uses root logger and logger.debug is used as DEBUG mode.
    script 2 -- uses same root logger but logger.info is used as INFO mode
    since both the above scripts are using same root logger with different mode due to which if i import script 2 in script 1
    then the logging level will be set to INFO and script 1 will not be able to generate log file with debug mode untill and unless
    it is set to info mode.

    so to solve this problem for each module a different logger should be used.
	to set specific loggers for each module the code is in logging_for_seperate_files.py script.
''' 

