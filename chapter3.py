import cv2

img=cv2.imread("C:/Users/ASUS/Documents/resources/lambo.png")
print(img.shape) #print the shape of the image
imgResize=cv2.resize(img,(300,200)) #resize the image
print(imgResize.shape)
imgCropped = img[0:200,200:500] #crop the image


cv2.imshow("Image",img)
cv2.imshow("Image resize",imgResize)
cv2.imshow("Image cropped",imgCropped)  #show the image
cv2.waitKey(0)