#BEFORE THIS U MAKE SURE THAT U HAVE HAARCASCADE FILES(EYE AND FACE THIS TIME) IN YOUR CURRENT DIRECTORY



import numpy as np
import cv2 
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
     
image = cv2.imread('nit1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



face1 = face.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in face1:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    

eye1 = eye.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in eye1:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
    
# U CAN USE BOTH THE CODE AT A TIME EITHER THIS ONE OR THE ANOTHER ONE WHICH IS WRITTEN BELOW



#for (x,y,w,h) in face1:
 #   cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
  #  eye1 = gray[y:y+h, x:x+w]
   # eye2 = image[y:y+h, x:x+w]
   # eyes = eye.detectMultiScale(eye1)
   # for (ex,ey,ew,eh) in eyes:
    #    cv2.rectangle(eye2,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
     
cv2.imshow('IMAGE',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
