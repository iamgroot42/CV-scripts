import cv2
import sys
import json
import os

frames = os.listdir("Images")
frames.sort()

coor_dump = []

try:
	for frame in frames:
		data = cv2.imread("Images/"+frame)
		gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
			
		face_cascade = cv2.CascadeClassifier('Features/haarcascade_frontalface_default.xml')
		# eye_cascade = cv2.CascadeClassifier('Features/haarcascade_eye.xml')
		
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		frame_coor = []
		for (x,y,w,h) in faces:
		    data = cv2.rectangle(data,(x,y),(x+w,y+h),(255,0,0),2)
		    roi_gray = gray[y:y+h, x:x+w]
		    roi_color = data[y:y+h, x:x+w]
		    # print "(",x,",",y,",",w,",",h,")"
		    frame_coor.append({"x":x+(w/2),"y":y+(h/2)})
	
		coor_dump.append(frame_coor)
		    # eyes = eye_cascade.detectMultiScale(roi_gray)
		    # for (ex,ey,ew,eh) in eyes:
		    #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		
		# cv2.imshow('data',data)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()
except:
	print "I/O error"

try:
	with open('Graphs/points.json', 'w') as outfile:
	    json.dump(coor_dump, outfile)
	print "Dumped JSON"
except:
	print "I/O error"