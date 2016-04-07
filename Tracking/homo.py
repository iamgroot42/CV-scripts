import cv2
import numpy as np
import sys
import os


def getHomography(img, img2, feature_type):
	if feature_type is "sift":
		feature = cv2.xfeatures2d.SIFT_create()
	else:
		feature = cv2.xfeatures2d.SURF_create()

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
		
	(kps, des) = feature.detectAndCompute(gray, None)
	(kps2, des2) = feature.detectAndCompute(gray2, None)	
	
	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	flann = cv2.FlannBasedMatcher(index_params,{})
	matches = flann.knnMatch(des,des2,k=2)
	matchesMask = [[0,0] for i in xrange(len(matches))]  #  drawing good matches
	
	good = []
	for m,n in matches:
	    if m.distance < 0.7*n.distance:
	        good.append(m)
	
	MIN_MATCH_COUNT = 10
	M = np.identity(3)

	if len(good) > MIN_MATCH_COUNT:
		src_pts = np.float32([ kps[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
		dst_pts = np.float32([ kps2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
		M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)

	return M


def warp(img, M):
	warped_shape = img.shape[:-1][::-1] 	
	warped = cv2.warpPerspective(img,M,warped_shape)
	return warped


def warpVideo(frames, feature_type):
	first = cv2.imread("Images/" + frames[0])
	second = first

	cv2.imwrite("Images/Warped/" + frames[0], first)

	print "Warping..."

	i = 1
	for frame in frames[1:]:
		second = cv2.imread("Images/" + frame)
		M = getHomography(first, second, feature_type)
		third = warp(first,M)
		cv2.imwrite("Images/Warped/" + frames[i], third)
		print " - Warped"
		first = second
		i += 1


if __name__ == "__main__":

	if len(sys.argv) < 2:
		print "Format : python "+sys.argv[0]+" <SIFT/SURF>"
		exit()
	
	if sys.argv[1].lower() not in ["sift","surf"]:
		print "Choose from SIFT/SURF"
		exit()

	frames = os.listdir("Images")
	frames.sort()
	frames = [x for x in frames if x.endswith(".jpg")]
	warpVideo(frames,sys.argv[1].lower())
