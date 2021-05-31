import cv2
face_detect=cv2.CascadeClassifier('classifier.xml')

img=cv2.imread('friends.jpeg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_detect.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('img',img)
    cv2.waitKey()