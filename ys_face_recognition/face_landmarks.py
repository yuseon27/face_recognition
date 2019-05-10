#!/usr/bin/env python
#-*- coding:utf-8 -*-

import face_recognition
from PIL import Image, ImageDraw

print("Start complile")

image = face_recognition.load_image_file("saporo2.jpg")
whole_image = Image.fromarray(image)
whole_image = whole_image.resize((378, 504))
whole_image.show()


face_landmarks_list = face_recognition.face_landmarks(image)

print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# Create a PIL imagedraw object so we can draw on the picture
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list :
	# Print the location of each facial feature in this image
    for facial_feature in face_landmarks.keys():
		print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

		# Let's trace out each facial feature in the image with a line!
		d.line(face_landmarks[facial_feature], width=5)

pil_image = pil_image.resize((756, 1008))
pil_image.show()


print("Python compile is completed.")
