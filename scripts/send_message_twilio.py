from twilio.rest import Client

account_sid = "AC5f7105e77afb27aca765f58d94b5dd00"
auth_token  = "57db7134c9575912c06d79e8730ad18b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918982778914", 
    from_="+12565634518",
    body="TEST1234")

print(message.sid)