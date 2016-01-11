# Homography Estimator 

An estimator which takes two images and estimates the homography transformation between them.

### Requirements 
- OpenCV (v3.x ,for Python)
- <a href="http://www.pyimagesearch.com/opencv-tutorials-resources-guides/"> opencv_contrib package (for SIFT,SURF) </a>
- Two images (taken from the same camera and nearly the same location)

### Running the scripts
- ```python feature_mapping.py <image1> <image2> <sift/surf>``` to map points by locating and matching features
- ```python homography.py``` to estimate the homography matrix 

Note : the use of some functions in these scripts (SIFT/SURF) is limited to educational purposes (for free,that is).