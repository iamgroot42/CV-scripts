import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('house.tiff',0)
cv2.imshow('House',img)
cv2.waitKey(0)
cv2.destroyAllWindows()