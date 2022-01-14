import cv2
import numpy as np
from djitellopy import tello
import time

from time import sleep

me = tello.Tello()

me.connect()

#me.takeoff()


def findFace(img):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "./haarcascade_frontalface_default.xml")
    imgGray: None = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces: None = faceCascade.detectMultiScale(imgGray, 1.2, 8)


    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
         cx = x + w// 2
         cy = y + h//2
         area = w * h
         cv2.circle(img,(cx,cy),5,(0,255,0) , cv2.FILLED)
       #  cv2.circle(img,(cx,cy),)
         myFaceListC.append([cx,cy])
         myFaceListArea.append(area)
         if len(myFaceListArea) != 0:
             i = myFaceListArea.index(max(myFaceListArea))
             return img, [myFaceListC[i],myFaceListArea[i]]
         else:
             return img, [[0,0], 0]



def trackFace(img):
    if "Area" < 10000:
        me.send_rc_control(0, 10, 0, 0)
        sleep(0.0001)

    elif "Area" == 10000:
        me.send_rc_control(0, 0, 0, 0)

    elif "Area" > 10000
        me.send_rc_control(0, -10, 0, 0)
        sleep(0.0001)

