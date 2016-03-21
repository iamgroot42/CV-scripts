import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys

if len(sys.argv) < 4:
	print "Format : python "+sys.argv[0]+" <image1> <image2> <SIFT/SURF>"
	exit()

if sys.argv[3].lower() not in ["sift","surf"]:
	print "Choose from SIFT/SURF"
	exit()

img = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])

# img = cv2.resize(img,(2,2))
# img2 = cv2.resize(img,(2,2))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

if sys.argv[3].lower() is "sift":
	feature = cv2.xfeatures2d.SIFT_create()
	(kps, des) = feature.detectAndCompute(gray, None)
	(kps2, des2) = feature.detectAndCompute(gray2, None)
	print("A #  {} keypoints".format(len(kps)))
	print("B #  {} keypoints".format(len(kps2)))
else:
	feature = cv2.xfeatures2d.SURF_create()
	(kps, des) = feature.detectAndCompute(gray, None)
	(kps2, des2) = feature.detectAndCompute(gray2, None)
	print("A #  {} keypoints".format(len(kps)))
	print("B #  {} keypoints".format(len(kps2)))


FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
# search_params = dict(checks=50)   # or pass empty dictionary
flann = cv2.FlannBasedMatcher(index_params,{})
matches = flann.knnMatch(des,des2,k=2)
matchesMask = [[0,0] for i in xrange(len(matches))]   # drawing good matches

good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

MIN_MATCH_COUNT = 10

if len(good)>MIN_MATCH_COUNT:
	src_pts = np.float32([ kps[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
	dst_pts = np.float32([ kps2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
	f = open('Mapping/points_img1.txt','w')
	f2 = open('Mapping/points_img2.txt','w')
	for x in range(src_pts.size):
		if x % 2 == 0:
			f.write(str(src_pts.item(x))+" ")
			f2.write(str(dst_pts.item(x))+" ")
		else:
			f.write(str(src_pts.item(x))+"\n")
			f2.write(str(dst_pts.item(x))+"\n")
	f.close()
	f2.close()
	print "Files generated"
	M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
	print "Homography calculated via in-built function : "
	print M

	matchesMask = mask.ravel().tolist()
	h,w = img.shape[0],img.shape[1]
	pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
	dst = cv2.perspectiveTransform(pts,M)
	img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)
	draw_params = dict(matchColor = (0,255,0), # draw matches in green color
	    singlePointColor = None,
	    matchesMask = matchesMask, # draw only inliers
	    flags = 2)
	img3 = cv2.drawMatches(img,kps,img2,kps2,good,None,**draw_params)
	plt.imshow(img3, 'gray'),plt.show()
else:
	print "Not enough good matches"
	exit()