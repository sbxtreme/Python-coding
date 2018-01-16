# basic math functions 

def sum(x,y):
	return x+y

def subs(x,y):
	return x-y

def mul(x,y):
	return x*y

def div(x,y):
	if y==0:
		raise ValueError('Cannot divide by zero')
	return x/y


