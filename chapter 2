import cv2 
import numpy as np

img = cv2.imread("C:/Users/ASUS/Documents/resources/lena.png")  
kernel = np.ones((5, 5), np.uint8) #create a kernel for dilation

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to gray
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) #apply Gaussian blur
imgCanny = cv2. Canny(img, 150, 200) #apply Canny edge detection
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) #dilate the image
imgEroded = cv2.erode(imgDialation, kernel, iterations=1) #erode the image

cv2.imshow("Gray Image", imgGray) #display gray image
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation) #display dilated image
cv2.imshow("Eroded Image", imgEroded) #display eroded image 


cv2.waitKey(0)  
