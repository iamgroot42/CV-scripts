import cv2
import sys
import json
import os

frames = os.listdir("Images")
frames.sort()

coor_dump = []

try:
	time = 1
	face_cascade = cv2.CascadeClassifier('Features/haarcascade_frontalface_default.xml')
	
	for frame in frames:
		data = cv2.imread("Images/"+frame)
		gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)		

		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		frame_coor = []
		for (x,y,w,h) in faces:
		    data = cv2.rectangle(data,(x,y),(x+w,y+h),(255,0,0),2)
		    roi_gray = gray[y:y+h, x:x+w]
		    roi_color = data[y:y+h, x:x+w]
		    frame_coor.append({"x":x+(w/2),"y":y+(h/2)})
			
		coor_dump.append({"time":time,"data":frame_coor})
		time += 1
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