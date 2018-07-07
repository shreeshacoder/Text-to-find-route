# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACe8f8094a119c72caa4a6d66504a70a74'
auth_token = '217bc76245848a5a009143500b784cef'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='+12893012434',
                              to='+14165208391'
                          )

print(message.sid)

