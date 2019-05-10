#!/usr/bin/env python
#-*- coding:utf-8 -*-

import face_recognition
from PIL import Image

print("Start complile")

image = face_recognition.load_image_file("saporo2.jpg")
whole_image = Image.fromarray(image)
whole_image = whole_image.resize((378, 504))
whole_image.show()

face_locations = face_recognition.face_locations(image)
print(face_locations)

for face_location in face_locations :

	top, right, bottom, left = face_location
	print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

	face_image = image[top:bottom, left:right]
	pil_image = Image.fromarray(face_image)
	pil_image.show()


print("Python compile is completed.")
