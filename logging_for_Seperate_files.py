'''
__name__ == "__main__" if script is running directly
__name__== "<script name>" if it is imported by other module.
'''
import logging
logger=logging.getLogger(__name__) # getting the getLogger method from logging module and logger object is created for it.
logger.setLevel(logging.DEBUG) # setting the logging level of logger
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s') # creating an object which will set the format of log file
file_handler=logging.FileHandler('newlogfile.txt') # log file name
file_handler.setFormatter(formatter) # setting the format of log file using formatter object created above
logger.addHandler(file_handler) # adding handler for log file

'''
a stream handler is also required if we want to cappture both error and result of 2 different functions
'''

# stream_handler=logging.StreamHandler()
# stream_handler.setFormatter(formatter)

# logger.addHadler(file_handler)
# logger.addHadler(stream_handler)


def divx(x,y):
	try:
		result = x/y
		logger.debug(result)
	except ZeroDivisionError:
		#logger.error('Divide by zero not possible') # output: 2018-01-15 23:16:03,934:ERROR:Divide by zero not possible
		logger.exception('Divide by zero not possible') 
		'''
		output of above logger.exception with trace on :
				2018-01-15 23:17:30,460:ERROR:Divide by zero not possible
				Traceback (most recent call last):
				  File "X:\TechSkills\DataScience using Python\Python programs\logging_for_Seperate_files.py", line 15, in divx
				    result = x/y
				ZeroDivisionError: division by ZeroDivisionError
		'''
	else:
		return result

def addx(x,y):
	return x+y

a=1
b=0

result=divx(a,b)

logger.debug('{}/{}={}'.format(a,b,result))