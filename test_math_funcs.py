# the name of the unitest file should be test_<name of script> ex: test_math_funcs.py
import unittest # importing standard unit test module of python
import math_funcs # importing the script which needs to be tested

'''
for testing all the functions present in math_funcs.py script we'll create a class 
and different methods of class for testing different functions of script math_funcs.py
'''
class test_math_funcs(unittest.TestCase): 
	
	def setUp(self): # this func executes some code before running testcases
		pass
		''' example: connecting to database and create some data for testing functions or update some dates which func uses'''

	def tearDown(self): # this func executes some code after running testcases
		pass
		'''example: once testcases are run we can remove some data from database or reverting some dates which we updated before test
		   cases runs
		'''
	def test_sum(self):
		self.assertEqual(math_funcs.sum(10,7),17)
		self.assertEqual(math_funcs.sum(1,-1),0)
		self.assertEqual(math_funcs.sum(-1,-4),-5)
		
	def test_sub(self):
		self.assertEqual(math_funcs.subs(10,7),3)
		self.assertEqual(math_funcs.subs(1,-1),2)
		self.assertEqual(math_funcs.subs(-1,-4),3)

	def test_mul(self):
		self.assertEqual(math_funcs.mul(10,7),70)
		self.assertEqual(math_funcs.mul(1,-1),-1)
		self.assertEqual(math_funcs.mul(-1,-4),4)

	def test_div(self):
		self.assertEqual(math_funcs.div(10,2),5)
		self.assertEqual(math_funcs.div(1,-1),-1)
		self.assertEqual(math_funcs.div(-4,-2),2)
		'''
		to test the exceptions whether it is raised correctly or not we can write the code given below
		the below code uses context manager to test the exceptions
		'''
		with self.assertRaises(ValueError): # the same ValueError exception is used in math_funcs.py which we are testing
			math_funcs.div(10,0)

'''
to run the unit test script directly by writing python Unit_test_module.py in cmd
OR
to run from the editor use the below code
'''
if __name__=='__main__':
	unittest.main()