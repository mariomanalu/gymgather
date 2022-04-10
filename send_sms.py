# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

class SMS:
    def __init__(self):
        pass

    def send_SMS(self):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = 'AC5c29e5fa23bf92283ea8d4310b067bb1'
        auth_token = 'cca4ddf98da04422e7404492d7e7606e'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="Mario just did 5 dumbbell curl!",
                            from_='+17409088086',
                            to='+16502888269'
                        )

        print(message.sid)