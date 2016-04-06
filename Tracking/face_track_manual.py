import cv2
import json
import os
import sys
import time as now
import homo # Local import

sys.settrace

homog = False

if len(sys.argv) < 2:
	print "python "+sys.argv[0]+" Y/N (to normalize camera motion)"
	exit()
else:
	if sys.argv[1].lower() == 'y':
		homog = True

print "Right-click to mark features (use same order throughout)"
print "Press any button to move to next frame"


if homog:
	frames = os.listdir("Images")
	frames.sort()
	frames = [x for x in frames if x.endswith(".jpg")]
	homo.warpVideo(frames,"sift")


frames = os.listdir("Images/Warped")
frames.sort()
frames = [x for x in frames if x.endswith(".jpg")]

raw_input("Ready?\n")

coor_dump = []
time = 1
right_clicks = list()
store = list()


#Called whenever the mouse is right-clicked
def mouse_callback(event, x, y, flags, params):
	if event == 2:
		global store
		store.append({"x":x,"y":y})
		print "{x:"+x+",y:"+y+"}"


try:
	for frame in frames:
		store = list() #reset the store array for next frame
		print "I read " + frame
		data = cv2.imread("Images/Warped/"+frame)

		cv2.imshow('data',data)
		cv2.setMouseCallback('data', mouse_callback)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

		right_clicks.append({"time":time,"data":store}) # append all the label points of frame in right_clicks array
		time += 1
except:
	print "I/O error"
	exit()

if not frames:
	print "Error : No images found"
	exit()

try:
	file_name = str(now.strftime("%Y%m%d%H%M%S.json"))
	with open("Graphs/Manual/" + file_name, 'w') as outfile:
	    json.dump(right_clicks, outfile)
	print "Dumped JSON : "+file_name
except:
	print "I/O error"
