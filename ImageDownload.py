# import random
# import urllib.request
# import tweepy
#
#
# def download_web_image(url):
#     name = random.randrange(1,1000)
#     full_name = str(name) + ".jpg"
#     urllib.request.urlretrieve(url,full_name)
#
#     download_web_image("")
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

# os.system("ffmpeg -framerate 1/5 -i /Users/leon/PycharmProjects/untitled/images/image%d.png -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4")



# Instantiates a client
# client = vision.ImageAnnotatorClient()

# for newpath in imagepath:
#     # The name of the image file to annotate
#     file_name = os.path.join(
#         os.path.dirname(__file__),
#         newpath)
#
#     # Loads the image into memory
#     with io.open(file_name, 'rb') as image_file:
#         content = image_file.read()
#
#     image = types.Image(content=content)
#
#     # Performs label detection on the image file
#     response = client.label_detection(image=image)
#     labels = response.label_annotations
#
#     print('Labels:')
#     for label in labels:
#         print(label.description)
