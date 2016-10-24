
#MAKE U SURE U HAVE INSTALLED NUMPY IN UR IDLE 

import numpy as np

import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')

frame = cv2.VideoCapture(0)

while 1:
    ret, image = frame.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converting the image color
    face1 = face.detectMultiScale(gray, 1.3, 5) #deteting the face here
    for (x,y,w,h) in face1:
        cv2.rectangle(image,(x,y),(x+w,y+h),(240,140,0),2) #drawing the rectange using its co-ordinates,color of rect,width of rect
    eye1 = eye.detectMultiScale(gray, 1.3, 5)#detetcting eye here
    for (x,y,w,h) in eye1:   
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2) #drawing the rectange using ssame attributes as above
        

#U CAN USE BOTH THE CODE AT A TIME



    #face1 = face.detectMultiScale(gray, 1.3, 5)

    #for (x,y,w,h) in face1:
       # cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        #eye1 = gray[y:y+h, x:x+w]
        #eye2 = image[y:y+h, x:x+w]
        
        #eyes = eye.detectMultiScale(eye1)
        #for (ex,ey,ew,eh) in eyes:
          #  cv2.rectangle(eye2,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)

    cv2.imshow('img',image)
    k = cv2.waitKey(30)
    if k == 27:
        break

frame.release()
cv2.destroyAllWindows()
