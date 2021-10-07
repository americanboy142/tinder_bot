import tinder_api
import tinder_api_sms
import config
import maya
from datetime import date,time
import features
import time
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from python_TinderAPI_master.tinder_api


app = Flask(__name__)

account_sid = 'AC3fa9c5554eef72095a9c8686f6e481c2'
auth_token = 'ed42f5ebf4b96a9029422f56f7f7fb0a'
client = Client(account_sid, auth_token)


matches = tinder_api_sms.all_matches()
for match in matches['matches']:
    # match
    new_match_id = match['_id']
    match_inf = features.match_info(match['_id'])
    match_name = match_inf(['name'])
    match_photo = match_inf(['photos'])
    match_bio = match_inf(['bio'])
    message = client.messages.create(
        MediaUrl=(match_photo[0]),
        body=('you matched with ' + match_name + "\n" + "bio: " + match_bio +
              " press 1) to send a default message" + "\n" + "2) to unmatch" + "\n" + "3) i got this"),
        from_='+12565688191',
        to='+18054504569'
    )


    @app.route('/bot', methods=['POST'])
    def bot():
        incoming_msg = request.values.get('Body', '').lower()
        resp = MessagingResponse()
        msg = resp.message()
        msg_out = (
                "press 1) for very aggressive pickup line " + "\n" + "2) for a joke " + "\n" + "3) pictures of my dog "
                + "\n" + "(option 3 requires snap)")
        responded = False
        if '1' in incoming_msg:
            # message match
            tinder_api.send_msg(new_match_id, msg_out)
            print('1')
            responded = True
        if '2' in incoming_msg:
            # unmatch
            tinder_api.unmatch(new_match_id)
            print('2')
            responded = True
        if '3' in incoming_msg:
            # nothing
            print('3')
            responded = True

        if not responded:
            msg.body('I only know about famous quotes and cats, sorry!')
        return str(resp)