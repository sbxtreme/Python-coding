#!/usr/bin/env python
#========================================================================================================================
# Title			 : pwd_encrypt.py
# Description    : The program encrypts the password and generates a key using which the password can be decrypted
# Author 		 : Shobhit Bhatnagar
# Date           : 2020-02-05
# Version        : 1.0
# Python version : 3.7.3
#========================================================================================================================

import sys
import argparse
from cryptography.fernet import Fernet
import socket

def create_parser():
	""" This function will return command line parser """
	parser=argparse.ArgumentParser(description='Script to generate the encrypted text and key',prog='pwd_encrypt.py')
	parser.add_argument('--text', dest='text', help='text to encrypt')
	parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
	return parser

def parse_args(arguments):
	""" This function will parse the command line arguments """
	parser=create_parser()
	args=parser.parse_args(arguments)

	''' check for mandatory parameters '''
	if not args.text:
		parser.error('Incorrect number of arguments: text required')
	return args

def get_ipaddress():
	""" This function will get ip address of server """
	try:
		hostname = socket.gethostname()
		ip_address = socket.gethostbyname(hostname)
		return ip_address
	except Exception as e:
		print(e)
		raise e

def pass_enc(text):
	try:
		""" This function encrypts the text and generates a key """
		text=text.encode()
		key=Fernet.generate_key()
		f=Fernet(key+get_ipaddress().encode('utf-8'))
		encrypted_text=f.encrypt(text)
		return encrypted_text,key
	except Exception as e:
		print(e)
		raise e

def main(argv=None):
	""" Program execution starts from here """
	try:
		if argv is None:
			argv=sys.argv
		args= parse_args(argv[1:])
		normaltext = args.text
		print("Plain text:",normaltext)
		encrypted_text,key=pass_enc(normaltext)
		print('Encrypted text:',encrypted_text)
		print('Key:',key)
	except Exception as e:
		print(e)
		raise e

if __name__=="__main__":
	sys.exit(main())
