
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect, url_for
from twilio import twiml
import time

account_sid = 'AC3fa9c5554eef72095a9c8686f6e481c2'
auth_token = 'ed42f5ebf4b96a9029422f56f7f7fb0a'
client = Client(account_sid, auth_token)


#message = client.messages.create(
#                    body=('you matched with '),
 #                   from_='+12565688191',
 #                   to='+18054504569'
 #              )

from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if '1' in incoming_msg:
        # return a quote
        print('it worked jebus')
        responded = True
    if '2' in incoming_msg:
        print('number 2 worked')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)

#if __name__=='__main__':
#    app.run()



