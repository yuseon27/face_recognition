#!/usr/bin/env python
#-*- coding:utf-8 -*-

import face_recognition
from PIL import Image, ImageDraw

print("Start complile")

image = face_recognition.load_image_file("saporo2.jpg")
whole_image = Image.fromarray(image)
whole_image = whole_image.resize((378, 504))
whole_image.show()

# Detect Faces
face_locations = face_recognition.face_locations(image)
print(face_locations)

for face_location in face_locations :

	top, right, bottom, left = face_location
	print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

	face_image = image[top:bottom, left:right]
	pil_image = Image.fromarray(face_image)
	pil_image.show()

	# Find features in the face_detected array
	face_landmarks_list = face_recognition.face_landmarks(face_image)
	print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

	
	landmark_image = Image.fromarray(face_image)
	draw = ImageDraw.Draw(landmark_image)
	
	for face_landmarks in face_landmarks_list :
		for facial_feature in face_landmarks.keys() :
			print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
			draw.line(face_landmarks[facial_feature], width=5)

	landmark_image.show()
	


print("Python compile is completed.")
