#!/usr/bin/env python

import cv2

cc = cv2.CascadeClassifier()
if not cc.load("haarcascade_frontalface_alt.xml"):
    print "load error"
    quit()

cam=cv2.VideoCapture(0)

flag,img=cam.read()

while flag:
    faces = cc.detectMultiScale(img, 1.1)
    
    color = (0, 255, 0)
    
    for (x, y, w, h) in faces:
        p1 = (x, y)
        p2 = (x + w, y + h)
        cv2.rectangle(img, p1, p2, color, 2)
    
    cv2.imwrite("detected.jpg", img)
    cv2.imshow("result",img)
    key=cv2.waitKey(1)
    flag, img = cam.read()
    if key>0 and chr(key)=='q': break

