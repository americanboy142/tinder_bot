
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


app = Flask(__name__)

account_sid = 'AC3fa9c5554eef72095a9c8686f6e481c2'
auth_token = 'ed42f5ebf4b96a9029422f56f7f7fb0a'
client = Client(account_sid, auth_token)

canSwipe = True
while canSwipe:
    persons = tinder_api_sms.get_recs_v2()["results"]
    for person in persons:
        person_id = person['_id']
        person_bio = person['bio']
        person_name = person['name']
        photos = []
        photos = person['photos']
        gender = person['gender']

        person_photo = []
        person_photo = photos

        birth_year = maya.parse(person['birth_date']).datetime().year
        person_age = date.today().year - birth_year



        if (canSwipe and person_age <= 22 and gender == 1):
            result = tinder_api_sms.like(person_id)
            print(person_name, person_bio, person_age)
            canSwipe = result.get('likes_remaining')

            if requests.get('match'):
                # match

                #features.get_match_id_by_name(person_name)
                features.get_match_info()
                global match_info
                list_of_ids = []
                for match in match_info:
                    if match_info[match]['_id'] == person_id:
                        list_of_ids.append(match_info[match]['match_id'])
                new_match_id = list_of_ids[0]
                message = client.messages.create(
                    MediaUrl=(person.images[0]),
                    body=('you matched with ' + person_name + "\n" + "bio: " + person_bio +
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
                        tinder_api_sms.send_msg(new_match_id, msg_out)
                        print('1')
                        responded = True
                    if '2' in incoming_msg:
                        # unmatch
                        tinder_api_sms.unmatch(new_match_id)
                        print('2')
                        responded = True
                    if '3' in incoming_msg:
                        #nothing
                        print('3')
                        responded = True

                    if not responded:
                        msg.body('I only know about famous quotes and cats, sorry!')
                    return str(resp)

                if canSwipe <= 50:
                    break

            else:
                time.sleep(2)


if __name__ == '__main__':
    app.run()
