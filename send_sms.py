# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC5c29e5fa23bf92283ea8d4310b067bb1'
auth_token = '11498b679b9f7ad7a0d4657f8687370b'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="See you at the gym fellas! We are building our leg muscle today!",
                     from_='+17409088086',
                     to='+16415101376'
                 )

print(message.sid)