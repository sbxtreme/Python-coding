############################# Exception Handling ################################

try:
	a=1  # catching exception at no.2 in case of any
	#open('file1.txt') # catching exception at no.1
except FileNotFoundError as e1: #exceptions to catch file not found --1
	print(e1)
except Exception as e2: # --2
	print(e2)
else:
	print('program executed successfully!\n') # This will execute if code written under try does not throw error
finally:
	print("This will execute regardless of any exeception occurs in the code.It will always execute\n")
'''
The finally block is used to close database connection /file / free any resource once execution
of code is done regardless of any exception raised in code.
'''

############################### Lambda expressions ############################
'''
The functions which does not have any name are called Lambda expressions
or anonymous functions
'''
# syntax: lambda < input variable >: <logic of function to return result>
# lambda function with 1 input
g=lambda x: 3*x+1
print(g(3))

fn=lambda x,y: 3*x+4*y
print (fn(4,-2))

############################## Map,filter & reduce functions for functional programming ####################

## Map function:

'''
this func consists of lambda function to calc result for each element
present in list l and returns result in list
'''

l=[1,2,3,4]
print(list(map(lambda x: 3+x-1,l)))

# function to convert degrees to Ferinheit

input=[("delhi",10),("goa",12),("mumbai",13),("satna",17),("doon",11)]
op=lambda data: (data[0],(9/5*data[1]+32))
print('\n',list(map(op,input)))

## filter function
''' this function filters data if the function called in filter function is true
    syntax filter(<fucname>,<list of values which will acts as i/p to function)
    display those values which are true by function(lamba)
'''
l=[5,6,10,12,35]
print('\nThese are the values greater than 10\n',list(filter(lambda x:x>10,l)))

## reduce functions
'''
This function is not used generally and its less profered over loop but the function is fast 
in terms of performance. The function is like 
l=[x1,x2,x3,x4,x5]
f=(x1,x2)=op
f=(op,x3)=op1
f=(op1,x4)=op2
f=(op2,x5)= final output
'''
# multiply all numbers present in a list

lst=[9,8,6,4,3,2,4,6,2,3]
from functools import reduce
print('\n',reduce(lambda x,y:x*y,lst))
