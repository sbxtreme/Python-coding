#!/usr/bin/env python
#========================================================================================================================
# Title			 : pwd_decrypt.py
# Description    : The program decrypts the password by accepting encrypted text and key
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-02-05
# Version        : 1.0
# Python version : 3.7.3
#========================================================================================================================

import sys
import argparse
from cryptography.fernet import Fernet

def create_parser():
	""" This function will return command line parser """
	parser=argparse.ArgumentParser(description='Script to decrypt the encrypted text',prog='pwd_decrypt.py')
	parser.add_argument('--enctext', dest='enctext', help='encrypted text')
	parser.add_argument('--key', dest='key', help='key')
	parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
	return parser

def parse_args(arguments):
	""" This function will parse the command line arguments """
	parser=create_parser()
	args=parser.parse_args(arguments)

	''' check for mandatory parameters '''
	if not args.enctext or not args.key:
		parser.error('Incorrect number of arguments passed')
	return args

def decrypt_pwd(enc_text,key):
	""" This function is used for password decryption """
	try:
		key=key.encode('utf-8')
		enc_text=enc_text.encode('utf-8')
		f = Fernet(key)

		decrypted_text=f.decrypt(enc_text).decode('utf-8')
		return decrypted_text
	except Exception as e:
		print(e)
		raise e

def main(argv=None):
	""" Program execution starts from here """
	try:
		if argv is None:
			argv=sys.argv
		args= parse_args(argv[1:])
		decrypted_text=decrypt_pwd(args.enctext,args.key)
		print("Decrypted_text: ",decrypted_text)
	except Exception as e:
		print(e)
		raise e

if __name__=="__main__":
	sys.exit(main())