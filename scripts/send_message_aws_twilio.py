import json

from twilio.rest import Client

account_sid = "AC5f7105e77afb27aca765f58d94b5dd00"
auth_token  = "57db7134c9575912c06d79e8730ad18b"
to_number = "+919958766250"
from_number = "+12565634518"

def twilio_message(account_sid,auth_token,message_to_send,to_number,from_number):
	client = Client(account_sid, auth_token)
	message = client.messages.create(
	    to=to_number, 
	    from_=from_number,
	    body=message_to_send)
	    
def lambda_handler(event, context):
	#1. Parse out query string params
	message_to_send =event["queryStringParameters"]["message_to_send"]
	twilio_message(account_sid,auth_token,message_to_send,to_number,from_number)

	print("message sent")

	#2. Construct the body of the response object
	api_response = {}
	api_response['message_to_send'] = message_to_send
	
	print(api_response)

	#3. Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(api_response)

	print(responseObject)

	#4. Return the response object
	return responseObject

#https://f69qvvoe0d.execute-api.us-east-2.amazonaws.com/teststage123/messages?message_to_send=%22hex12345%22