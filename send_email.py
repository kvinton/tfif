# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

# get these from the database
admiree_name = "Jeanna" 
admiree_email = "jagindi@gmail.com"

with open('email_body.txt') as fp:
    # Create a text/plain message
    message_template = fp.read()


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("thefutureisfemale.sf@gmail.com")
to_email = Email(admiree_email)
subject = "A woman in tech admires you, pass it on!"
content_string = message_template.format(PERSON_NAME=admiree_name)
print(content_string)
content = Content("text/plain", content_string)

mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)