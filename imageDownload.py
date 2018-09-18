
# import tweepy  # https://github.com/tweepy/tweepy
# import json
# import random
# import urllib
# import os
#
# def download(url):
#     name = random.randrange(1, 1000)
#     full_name = str(name) + ".jpg"
#     urllib(url, full_name)
#
# download("https://pbs.twimg.com/media/DnXvLpcUAAIDt1G.jpg")

import tweepy
from tweepy import OAuthHandler
import json
import wget

# Tweepy credentials
consumer_key = 'Enter you consumer_key here'
consumer_secret = 'Enter you consumer_secret here'
access_token = 'Enter you consumer_key here'
access_secret = 'Enter you consumer_secret here'

# Tweepy config
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
lic = OAuthHandler(consumer_key, consumer_secret)
lic.set_access_token(access_token, access_secret)

api = tweepy.API(lic)


# get tweets from a user

tweets = api.user_timeline(screen_name='Enter the target twitter username',
                           count=10, include_rts=False,
                           exclude_replies=True)

# obtain the urls of images
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

# download the images
for media_file in media_files:
    wget.download(media_file)