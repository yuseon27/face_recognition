#!/usr/bin/env python
#-*- coding:utf-8 -*-

# ys_face_recognition.py
# 20163228 남유선

import face_recognition
from PIL import Image, ImageDraw
import numpy as np


# 원본 이미지 보여주기
def show_image(image):
	whole_image = Image.fromarray(image)
	whole_image.show()

# Face Detection
def detect_face(image, cur) :
		
	# 얼굴의 위치 받아옴
	face_locations = face_recognition.face_locations(image)

	for face_location in face_locations :
	
		# 얼굴의 x와 y 범위 가져오기 (Top, Left, Bottom, Right 순)
		top, right, bottom, left = face_location
		print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

		# 이미지에 얼굴만 나오게 배열 자르기 
		face_image = image[top:bottom, left:right]

		# 얼굴 이미지 보여주기/저장
		face_pil_image = Image.fromarray(face_image)
#		face_pil_image.show()
		face_pil_image.save("ys0{}/detection.jpg".format(str(cur)))
		

	return (face_image)



# Find Features in the Face
def find_features(image, cur, index) :
	
	# 얼굴의 특징들 추출
	face_landmarks_list = face_recognition.face_landmarks(image)
	if index == 0 :
	    print("Found {} face(s)".format(len(face_landmarks_list)))

	# 얼굴의 특징을 얼굴 사진 위에 표현
	feature_pil_image = Image.fromarray(image)
	draw = ImageDraw.Draw(feature_pil_image)			

	for face_landmarks in face_landmarks_list :
		
	    for facial_feature in face_landmarks.keys():
			if index == 0:		
				print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

			# 얼굴의 특징을 선으로 그림
			draw.line(face_landmarks[facial_feature], width=5)

	# 얼굴 위에 특징 선 보여주기/저장 
#	feature_pil_image.show()
	feature_pil_image.save("ys0{}/feature{}.jpg".format(str(cur), str(index)))



# Recognize Face
def recognize_face(me, unknown) :
	
	# 알고있는 사진과 모르는 사진 얼굴 인식 후 비교하여 같은 지 결과로 반환
	results = face_recognition.compare_faces([ys_encoding[me]], ys_encoding[unknown])
	
	if results[0] == True :
		print("ys0{} is a picture of me:)".format(str(unknown)))
	else :
		print("ys0{} is not a picture of me;(".format(str(unknown)))



def do_recognition(cur) :

	print("\n============================================================")
	print("ys0{}.jpg".format(str(cur)))
	image = ys_image[cur]
#	show_image(image)

	print("1. Face Detection")	
	face_image = detect_face(image, cur)
	
	print("2. Feature of Face")
	find_features(image, cur, 0)
	find_features(face_image, cur, 1)
	
	print("\n3. Recognize Face")		
	print("I am ys0{}".format(str(cur)))
	for j in range (10) :
		if (cur != j) :
			recognize_face(cur, j)

	print("============================================================")


if __name__ == "__main__":
	
	# 10개의 이미지 불러오기
	ys_image = []
	for i in range (10) :
		ys_image.append(face_recognition.load_image_file("ys0{}/ys0{}.jpg".format(str(i), str(i))))
	print("이미지 파일 불러오기 완료")


	# 10개의 이미지 Encoding
	ys_encoding = []
	for i in range (10) :
		ys_encoding.append(face_recognition.face_encodings(ys_image[i])[0])
	print("이미지 파일 인코딩 완료")

	# 얼굴 인식 시작
	for i in range(10) :
		do_recognition(i)
'''
	cur = 7
	do_recognition(cur)
'''
