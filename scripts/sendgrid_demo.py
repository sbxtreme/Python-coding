import os, ssl
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# The below code is used to prevent CERTIFICATE FAILURE error.
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
	ssl._create_default_https_context = ssl._create_unverified_context

# the from_email and the to_email must be verified via sendgrid UI before sending mail.
message = Mail(
    from_email='sbxtreme13@gmail.com',
    to_emails='sbxtreme13@gmail.com',
    subject='Sending Email via Sendgrid automation',
    html_content='<strong>TEST EMAIL</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print('response is : ',response)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)


'''
Below is the curl command to send email :

curl --request POST \
        --url https://api.sendgrid.com/v3/mail/send \
        --header "Authorization: Bearer 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" \
        --header 'Content-Type: application/json' \
        --data '{"personalizations": \
        [{"to": [{"email": "shobhit.a.bhatnagar@capgemini.com"}]}],"from": {"email": "shobhit.a.bhatnagar@capgemini.com"},\
        "subject": "Sending with SendGrid is Fun","content": [{"type": "text/plain", "value": "and easy to do anywhere, even with cURL"}]}'
'''