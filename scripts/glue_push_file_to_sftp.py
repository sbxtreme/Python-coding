#=======================================================================================================
# Description         : The below script does the following:
#						a) Get the export files from S3
#						b) Encrypt the file with the public key
#						c) Push the file to Client's SFTP
#                       d) Move the original file to processed directory with "file_pushed." prefix
# Author 		      : Shobhit Bhatnagar
# Date                : 2021-04-22
# Glue Version        : 1.0
# Python version 	  : 3.6
#========================================================================================================

import gnupg
import io
import sys
import boto3
import paramiko
import smtplib
import traceback
import s3fs
from typing import Any, cast
from email.mime.multipart import MIMEMultipart 
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email.header import Header
from datetime import datetime, timedelta
    
#========================================= Global Variables ======================================================
source_bucket="choicehotels-stg-sessionm-com"
source_bucket_key="etl/composer_report/"
processed_file_key="etl/composer_report/processed_files"
source_path="choicehotels-stg-sessionm-com/etl/composer_report"
dest_path="choicehotels-stg-sessionm-com/etl/composer_report/processed_files"
file_pattern="stg_reporting"
sftp_path="/SessionM_Outbound/reporting/stg/"
sftp_host="SFTP.choicehotels.com"
sftp_user="sessionmoutbound_user"
sftp_pwd="ZPrdAd5SzBWDnHMEjZcxznyT"
smtp_username = "AKIAJ2OA3SHLJHB3QC2Q"
smtp_password = "AjBS86U8gnza9O2RdbjbOj2csrW0zryI/Iotp8qAjq4P"
smtp_server = "email-smtp.us-east-1.amazonaws.com"
key_file="glue/keys/sessionm_public.asc"
smtp_port = 25
from_email="no_reply@sessionm.com"
to_email="sbhatnagar@sessionm.com"
s3_client = boto3.client('s3')
s3 = boto3.resource('s3')
#===================================================================================================================


class Capturer(object):
	def __init__(self, file_output, fs):
		self.fout = fs.open(file_output, 'wb')

	def __call__(self, data):
		if data:
			self.fout.write(data)
		else:
			self.fout.close()
		return False


def get_filenames_from_S3(source_bucket,source_bucket_key):
	""" This function reads file from S3 """
	try:
		
		source_bucket = s3.Bucket(source_bucket)
		source_files = [object.key for object in source_bucket.objects.filter(Prefix=source_bucket_key)]

		print("Getting file from S3")
		
		return source_files

	except Exception as e:
		print("An error occured in get_filenames_from_S3 function:",e)
		raise e
		sys.exit(1)


def open_sftp_connection(sftp_host, sftp_username, sftp_password, sftp_port=22):
	""" The below function connects to external SFTP """
	client = paramiko.SSHClient()
	client.load_system_host_keys()
	
	try:
		transport = paramiko.Transport(sftp_host, sftp_port)
	except Exception as e: 
		print("Connection error while connecting to choicehotels SFTP:",e)
		raise e
		sys.exit(1)
	
	try: 
		transport.connect(username=sftp_username, password=sftp_password)
	except Exception as e: 
		print("Authorization error while connecting to choicehotels SFTP:",e)
		raise e
		sys.exit(1)
	
	sftp_connection = paramiko.SFTPClient.from_transport(transport)
	print("SFTP connnection Established")
	
	return sftp_connection


def encrypt_files(input_file=None,output_file=None):
	""" The below function encrypts the file using public key """
	try:
		
		gpg = gnupg.GPG(gnupghome='./')
		gpg.encoding = 'utf-8'
		bytes_buffer = io.BytesIO()
		s3_client.download_fileobj(Bucket=source_bucket, Key=key_file, Fileobj=bytes_buffer)
		byte_value = bytes_buffer.getvalue()
		str_value = byte_value.decode()
		imported_keys = gpg.import_keys(str_value)

		file_input = 's3://choicehotels-stg-sessionm-com/etl/composer_report/test_stg_reporting_2018.csv'
		file_output = 's3://choicehotels-stg-sessionm-com/etl/composer_report/test_stg_reporting_2018.csv.gpg'

		fs = s3fs.S3FileSystem(anon=False)
		capturer = Capturer(file_output, fs)
		gpg.on_data = capturer

		with fs.open(file_input, 'rb') as fin:
			status = gpg.encrypt_file(fin,armor=False, always_trust=True, recipients = imported_keys.fingerprints)


		#print("File {} encrypted successfully".format(filename))

	except Exception as e:
		print("An error occured in encrypt_files function:",e)
		raise e
		sys.exit(1)


def push_files_to_sftp(sftp_connection,sftp_path,filename,s3_file):
	try:
		# Writing files to SFTP:
		with sftp_connection.open(sftp_path+filename, 'wb', 32768) as f:
			s3_client.download_fileobj(source_bucket, s3_file, f)

		print("File {} pushed successfully to SFTP".format(filename))

	except Exception as e:
		print("An error occured in push_files_to_sftp function:",e)
		raise e
		sys.exit(1)


def move_file_from_S3(source_bucket,processed_file_key,filename):
	""" This function moves the file from one directory of S3 to another """
	try:
		actual_file=filename.split("/")[-1]
		copy_source = {'Bucket': source_bucket, 'Key':filename}
		s3.meta.client.copy(copy_source, source_bucket, processed_file_key+'/'+'done.'+actual_file)
		
		print("File copied from {0} directory to {1} directory".format(source_path,dest_path))
		
		# Deleting file from existing directory
		s3.Object(source_bucket, filename).delete()

		print("File removed from {} directory".format(source_path))

	except Exception as e:
		print("An error occured in move_file_from_S3 function:",e)
		raise e
		sys.exit(1)


def sent_email(email_from,email_to,subject,body,attachment_list=None):
	""" The below function is used to send emails """

	contents = MIMEMultipart()
	contents.attach(MIMEText(cast(str, body), "html"))
	contents['From'] = email_from
	contents['To'] = email_to
	contents['Subject'] = Header(subject, "UTF-8")
	
	try:
		s = smtplib.SMTP(smtp_server, smtp_port) 
		s.starttls()
		s.login(smtp_username, smtp_password) 
		text = contents.as_string() 
		s.sendmail(email_from, email_to.split(","), text)
		s.quit()

		print("Email sent!")

	except Exception as e:
		print("Failed to send Email: {}".format(e))
		raise e
		sys.exit(1)


def main():
	""" Program execution starts from here """
	try:
		print('='*5,"Glue Job Execution Started on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)

		'''
		# Getting files from s3 bucket
		data=get_filenames_from_S3(source_bucket,source_bucket_key)
		
		# Opening SFTP connection
		sftp_connection=open_sftp_connection(sftp_host,sftp_user,sftp_pwd)
		
		files_to_process=[orig_filename for orig_filename in data if not ('done.' in orig_filename ) and (file_pattern in orig_filename )]

		# Logic to push multiple files in loop
		if not files_to_process:
			msg="No files found with the pattern *{0}* to push to ChoiceHotels SFTP".format(file_pattern)
			print(msg)
			
			# Send email if no files found to push to SFTP
			sent_email(from_email,to_email,msg,msg)
		else:
			for orig_filename in files_to_process:
				print("\nPushing {0} file to SFTP".format(orig_filename))

				# Getting actual filename and preparing email content
				filename=orig_filename.split('/')
				actual_file=[name for name in filename if file_pattern in name][0]
				email_content="File {} pushed to ChoiceHotels SFTP".format(actual_file)

				# Writing file to SFTP
				push_files_to_sftp(sftp_connection,sftp_path,actual_file,orig_filename)

				# Move the file to processed directory
				move_file_from_S3(source_bucket,processed_file_key,orig_filename)

				# Send email once file is pushed to SFTP
				sent_email(from_email,to_email,email_content,email_content)


		print('='*5,"Glue Job Execution Ended on:",datetime.now().strftime("%b %d %Y %H:%M:%S"),'='*5)
		'''

		encrypt_files()


	except Exception as e:
		
		# Send email in case of any failures in glue job
		sent_email(from_email,to_email,"An Error occured in Glue Push file job",str(traceback.format_exc()))
		print("An error occured in main function:",e)
		raise e
		sys.exit(1)



if __name__=="__main__":
	main()