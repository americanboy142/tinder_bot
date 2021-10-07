import tinder_api
import tinder_api_sms
import config
import maya
from datetime import date,time
import features
import time


canSwipe = True
while canSwipe:
    persons = tinder_api_sms.get_recs_v2()['data']['results']
    for person in persons:
        person = person['user']
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
            print(canSwipe)

        time.sleep(3)
        break
    break

