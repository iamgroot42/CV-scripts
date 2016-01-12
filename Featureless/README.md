# Flow estimator

An estimator which takes two images and estimates the optical flow from one to the other.
(Least square minimization (LK), using a 5x5 pixel window)

### Requirements 
- OpenCV (v3.x ,for Python)
- <a href="http://www.pyimagesearch.com/opencv-tutorials-resources-guides/"> opencv_contrib package (for SIFT,SURF) </a>
- Two images (taken from the same camera and nearly the same location)

### Running the scripts
- ```python self_flow.py <image1> <image2>``` to estimate optical flow

Note : the use of some functions in these scripts (SIFT/SURF) is limited to educational purposes (for free,that is).