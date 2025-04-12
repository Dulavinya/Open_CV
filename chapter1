
#read an image
import cv2

#load an image 
img=cv2.imread("C:/Users/ASUS/Documents/resources/lena.png")

if img is None:
	raise FileNotFoundError("The image file 'resources/lena.png' was not found. Please check the file path.")

#display 
cv2.imshow("Lena Soderberg",img)
cv2.waitKey(0)

#read webcam 

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)

cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150) #brightness 
while True:
    success, img = cap.read()
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




#read video

frameWidth =640
frameHeight =480
cap = cv2.VideoCapture("C:/Users/ASUS/Documents/resources/test_video.mp4")
while True: 
    success, img = cap.read()
    img=cv2.resize(img,(frameWidth,frameHeight))    
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

   