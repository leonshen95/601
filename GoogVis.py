import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    '/Users/leon/PycharmProjects/untitled/images/image2.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations
Des=[]
print('Labels:')
for label in labels:
    print(label.description)
    Des.append(label.description)


font = ImageFont.truetype('HelveticaNeue.ttc', 60)

#打开图片
imageFile = "/Users/leon/PycharmProjects/untitled/images/image2.jpg"
im1=Image.open(imageFile)

draw = ImageDraw.Draw(im1)
# (0,0):坐标 "XUNALOVE"：添加的字体 (0,0,255):字体颜色 font:字体大小
draw.text((0, 0), str(Des), (255, 0, 0), font=font)
draw = ImageDraw.Draw(im1)

# 保存
im1.save("/Users/leon/PycharmProjects/untitled/images/image2.png")