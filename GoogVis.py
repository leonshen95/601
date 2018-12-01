#author: Leyang Shen
import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import mysql.connector
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pymongo import MongoClient

credential_file = "/Users/leon/Downloads/PicDesc-87a0e7d15396.json"
def get_image_client(credential_file):
    return vision.ImageAnnotatorClient.from_service_account_file(credential_file)
client = get_image_client(credential_file)
# The name of the image file to annotate
list = os.listdir('/Users/leon/PycharmProjects/untitled/images')

n = 0
cnx = mysql.connector.connect(user='root', password='leon950417', database='twitter')
cursor = cnx.cursor()
add_transaction = ("INSERT INTO transactions "
                   "(usrid, num, image_name, description) "
                   "VALUES (%s, %s, %s, %s)")
while n < len(list)-1:
    file_name = os.path.join(
        os.path.dirname(__file__),
        '/Users/leon/PycharmProjects/untitled/images/image' + str(n) + '.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    Des = []
    # print('Labels:')
    for label in labels:
        # print(label.description)
        Des.append(label.description)

    font = ImageFont.truetype('HelveticaNeue.ttc', 30)
    cursor.execute("INSERT INTO transactions(image_name, description) VALUES('%s', '%s')"% ('image' + str(n) + '.jpg', Des))
    # open the image
    imageFile = "/Users/leon/PycharmProjects/untitled/images/image" + str(n)+".jpg"
    im1 = Image.open(imageFile)

    draw = ImageDraw.Draw(im1)
    # (0,0):coordinates, (255,0,0):font color, font size
    draw.text((0, 0), str(Des), (255, 0, 0), font=font)
    draw = ImageDraw.Draw(im1)

    # save the labeled image
    if not os.path.exists('finalimages'):
        os.mkdir('finalimages')
    im1.save("/Users/leon/PycharmProjects/untitled/finalimages/image"+str(n)+".png")

    n = n + 1
emp_no = cursor.lastrowid

cnx.commit()
cursor.close()
cnx.close()

os.system("ffmpeg -framerate 24 -r 1 -i /Users/leon/PycharmProjects/untitled/finalimages/image%d.png -s 1080*1080 -pix_fmt yuv420p out.mp4")
