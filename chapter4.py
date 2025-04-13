import cv2
import numpy as np


img = np.zeros((512, 512,3),np.uint8) # create a black imag
img[200:300,200:300] = 255,0,0 # BGR color (blue)

cv2.imshow("Image", img) # show the image
cv2.waitKey(0) # wait for a key press