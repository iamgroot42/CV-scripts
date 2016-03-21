import numpy as np
import cv2
import sys

if len(sys.argv) < 4:
	print "Format : python "+sys.argv[0]+"<input> <image/video>"
	exit()

if sys.argv[2].lower() not in ["image","video"]:
	print "Choose from image/video"
	exit()

if sys.argv[2].lower() is "image":
	data = cv2.imread(sys.argv[1])
	gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    data = cv2.rectangle(data,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = data[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('data',data)
cv2.waitKey(0)
cv2.destroyAllWindows()