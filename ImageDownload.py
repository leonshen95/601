# author: Leyang Shen
import tweepy  # https://github.com/tweepy/tweepy
import json
from tweepy import OAuthHandler
import wget
import io
import urllib
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import mysql.connector
from pymongo import MongoClient

    # Twitter API credentials
consumer_key = "Enter your consumer key here"
consumer_secret = "Enter your consumer secret here"
access_key = "Enter your access key here"
access_secret = "Enter your access secret here"

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
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
    # get tweets from a user
name = input("Please Enter a Twitter username(eg: @AvrilLavigne. Enter the characters after @: ")
num = input("Please Enter how many images you would like to download: ")
tweets = api.user_timeline(screen_name=name,
                           count=num, include_rts=False,
                           exclude_replies=True)
    # obtain the urls of images
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

    # download the images

    n = 0
    imagepaths=[]
    if not os.path.exists('images'):
        os.mkdir('images')

for media_file in media_files:
    imagepath = 'images/image' + str(n)+'.jpg'
    imagepaths.append(imagepath)
    wget.download(media_file, imagepath)
    n = n + 1
cnx = mysql.connector.connect(user='root', password='leon950417', database='twitter')
cursor = cnx.cursor()

add_transaction = ("INSERT INTO transactions "
                       "(usrid, num, image_name, description) "
                       "VALUES (%s, %s, %s, %s)")
data_transaction = (name, num, '', '')
cursor.execute(add_transaction,data_transaction)
emp_no = cursor.lastrowid

cnx.commit()

cursor.close()
cnx.close()





