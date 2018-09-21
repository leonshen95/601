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
consumer_key = "228XlU7E4gtzvw1zPI7YfcFoc"
consumer_secret = "gHPTudu33d7CCwPlbWFE9EbpJDyuTkVkzJUC4BBruZkRa3vuE0"
access_key = "1039252875698995200-2nOJAGrOPkmFgEfiNzLrPwGVlCDszD"
access_secret = "z9fjJ7Ll17F71dcXrhjWd414szehGQ9NK30oX4DYpCg0s"

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

tweets = api.user_timeline(screen_name='itsbeautynature',
                           count=60, include_rts=False,
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