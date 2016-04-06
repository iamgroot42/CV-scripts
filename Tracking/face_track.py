import cv2
import sys
import json
import os
import time as now
import homo # Local import

display = False

if len(sys.argv) < 2:
	print "python "+sys.argv[0]+" Y/N (to show tracked faces or not)"
	exit()
else:
	if sys.argv[1].lower() == 'y':
		display = True

frames = os.listdir("Images")
frames.sort()
frames = [x for x in frames if x.endswith(".jpg")]

homo.warpVideo(frames,"sift")
exit()

coor_dump = []

# try:
time = 1
face_cascade = cv2.CascadeClassifier('Features/haarcascade_frontalface_default.xml')

try:
	for frame in frames:
		print "I read " + frame
		data = cv2.imread("Images/"+frame)
		gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)		

		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		frame_coor = []
		for (x,y,w,h) in faces:
			cv2.rectangle(data,(x,y),(x+w,y+h),(255,0,0),2) 
			roi_gray = gray[y:y+h, x:x+w]
	    	roi_color = data[y:y+h, x:x+w]
	    	frame_coor.append({"x":x+(w/2),"y":y+(h/2)})
	
		coor_dump.append({"time":time,"data":frame_coor})
		time += 1
		if display:
			cv2.imshow('data',data)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
except:
	print "I/O error"
	exit()

if not frames:
	print "Error : No images found"
	exit()
	
try:
	file_name = str(now.strftime("%Y%m%d%H%M%S.json"))
	with open("Graphs/Automatic/" + file_name, 'w') as outfile:
	    json.dump(coor_dump, outfile)
	print "Dumped JSON : "+file_name
except:
	print "I/O error"
