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
                            body="Mario just reached his workout goal of 5 dumbbell curls! Congratulate him!",
                            from_='+17409088086',
                            to='REDACTED'
                        )

        print(message.sid)