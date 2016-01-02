import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("a.jpg")
img2 = cv2.imread("b.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
(kps, des) = sift.detectAndCompute(gray, None)
(kps2, des2) = sift.detectAndCompute(gray2, None)
print("A #  kps: {}, descriptors: {}".format(len(kps), des.shape))
print("B #  kps: {}, descriptors: {}".format(len(kps2), des2.shape))

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des,des2,k=2)
matchesMask = [[0,0] for i in xrange(len(matches))]   # drawing good matches

# src_pts = np.float32([ kps[m.queryIdx].pt for m in matches ]).reshape(-1,1,2)
# dst_pts = np.float32([ kps2[m.trainIdx].pt for m in matches ]).reshape(-1,1,2)

good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

MIN_MATCH_COUNT = 10

if len(good)>MIN_MATCH_COUNT:
	src_pts = np.float32([ kps[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
	dst_pts = np.float32([ kps2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

# M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
# matchesMask = mask.ravel().tolist()

	print src_pts.shape, dst_pts.shape
	print src_pts[0],dst_pts[0] 
else:
	print "Not enough good matches"
	exit()

draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)
img3 = cv2.drawMatchesKnn(img,kps,img,kps2,matches,None,**draw_params)
plt.imshow(img3,),plt.show()