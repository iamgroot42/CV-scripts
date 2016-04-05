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
	if sys.argv[1].upper() == 'Y':
		display = True


frames = os.listdir("Images")
frames.sort()
frames = [x for x in frames if x.endswith(".jpg")]

# homo.warpVideo(frames,"sift")

coor_dump = []

# try:
time = 1
face_cascade = cv2.CascadeClassifier('Features/haarcascade_frontalface_default.xml')

right_clicks = list()
store = list()

#this function will be called whenever the mouse is right-clicked
def mouse_callback(event, x, y, flags, params):
	# print "hello"
    #right-click event value is 2
	if event == 2:
		global store

        #store the coordinates of the right-click event
		store.append({"x":x,"y":y})

        #this just verifies that the mouse data is being collected
        #you probably want to remove this later
		print store

try:

	for frame in frames:
		
		store = list() #reset the store array for next frame
		
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
			cv2.setMouseCallback('data', mouse_callback)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		right_clicks.append({"time":time,"data":store}) # append all the label points of frame in right_clicks array


except:
	print "I/O error"

try:
	file_name = str(now.strftime("%Y%m%d%H%M%S.json"))
	with open("Graphs/" + file_name, 'w') as outfile:
	    json.dump(coor_dump, outfile)
	print "Dumped JSON : "+file_name
except:
	print "I/O error"


#append all data in labelling json file

try:
	file_name = str(now.strftime("Labelling_%m%d%H%M%S.json"))
	with open("Manual_Labels/" + file_name, 'w') as outfile:
	    json.dump(right_clicks, outfile)
	print "Dumped JSON : "+file_name
except:
	print "I/O error"

