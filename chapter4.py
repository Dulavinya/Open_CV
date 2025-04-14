import cv2
import numpy as np


img = np.zeros((512, 512,3),np.uint8) # create a black imag
#img[200:300,200:300] = 255,0,0 # BGR color (blue)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),5)   # draw a circle

cv2.imshow("Image", img) # show the image
cv2.waitKey(0) # wait for a key press