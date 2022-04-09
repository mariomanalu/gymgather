# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

class SMS:
    def __init__(self):
        pass

    def send_SMS(self):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = 'REDACTED'
        auth_token = 'REDACTED'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="See you at the gym fellas! We are building our leg muscle today!",
                            from_='+17409088086',
                            to='+16415101376'
                        )

        print(message.sid)