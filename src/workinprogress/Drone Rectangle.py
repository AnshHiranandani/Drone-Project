import cv2
import numpy as np
from djitellopy import tello
import time

from time import sleep

me = tello.Tello()

me.connect()

print(me.get_battery())

me.takeoff()


def findFace(img):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "./haarcascade_upperbody.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
         cx = x + w// 2
         cy = y + h//2
         area = w * h
         cv2.circle(img,(cx,cy),5,(0,255,0) , cv2.FILLED)
         #cv2.circle(img,(cx,cy),)
         myFaceListC.append([cx,cy])
         myFaceListArea.append(area)
         if len(myFaceListArea) != 0:
             i = myFaceListArea.index(max(myFaceListArea))
             return img, [myFaceListC[i],myFaceListArea[i]]
         else:
             return img, [[0,0], 0]


def trackFace(area, zx, zy):
#     print("Area", area)
#     if zy < 100:
#         me.send_rc_control(0, 0, 30, 0)
#         sleep(0.00001)
#         print("y1", zy)
#         me.send_rc_control(0, 0, 0, 0)
#     elif zy > 100:
#         me.send_rc_control(0, 0, -30, 0)
#         sleep(0.00001)
#         print("y2", zy)
#         me.send_rc_control(0, 0, 0, 0)
#
#     if zx < 170:
#         me.send_rc_control(0, 0, 0, -30)
#         sleep(0.01)
#         print("x1", zx)
#         me.send_rc_control(0, 0, 0, 0)
#     elif zx > 170:
#         me.send_rc_control(0, 0, 0, 30)
#         sleep(0.01)
#         print("x2", zx)
#         me.send_rc_control(0, 0, 0, 0)
#
    if area < 12000:
       me.send_rc_control(0, 10, 0, 0)
       sleep(0.0001)
       print("Area1", area)
       me.send_rc_control(0, 0, 0, 0)

    elif area == 12000:
        me.send_rc_control(0, 0, 0, 0)
        print("Area2", area)
        me.send_rc_control(0, 0, 0, 0)

    elif area > 12000:
        me.send_rc_control(0, -10, 0, 0)
        sleep(0.0001)
        print("Area3", area)
        me.send_rc_control(0, 0, 0, 0)



me.send_rc_control(0,0,30,0)

sleep(5)

# me.streamon()
# while True:
# #    status, img = cap.read()
# #    print(statdus)
#     img = me.get_frame_read().frame
#     img = cv2.resize(img, (360, 240))
#     if img is None:
#         continue
#     try:
#         img, info = findFace(img)
#         length = len(info[0])
#         zx = info[0][:1]
#         zy = info[0][1]
#         trackFace(info[1], zx, zy)
#         #print(info[1])
#         #print(zx)
#         #print(zy)
#     except:
#         print("Expection happened")
#
#     cv2.imshow("Image", img)
#
#     cv2.waitKey(1)
#
# #    print(zx, zy)
