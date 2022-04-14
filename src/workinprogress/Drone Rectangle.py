import cv2
import numpy as np
from djitellopy import tello
import time

from time import sleep

me = tello.Tello()

me.connect()

print(me.get_battery())

#me.takeoff()


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


def trackarea(area):
  #  print("Area", area, "zx", zx, "zy", zy)
  if area < 12000:
      me.send_rc_control(0, 15, 0, 0)
      sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
      print("Area1", area)
  #  print("this is the end of the fifth if")
  elif area == 12000:
      me.send_rc_control(0, 0, 0, 0)
      print("Area2", area)
      me.send_rc_control(0, 0, 0, 0)
  #   print("this is the end of the sixth if")
  elif area > 12000:
      me.send_rc_control(0, -15, 0, 0)
      sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
      print("Area3", area)
      #  print("this is the end of the seventh if")
  else:
      me.send_rc_control(0, 0, 0, 0)

def trackx(zx):
  if zx < 170:
      #  print(" I am inside the thrid if")
        me.send_rc_control(0, 0, 0, -15)
        sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        print("x1", zx)
  #  print("this is the end of the third if")
  elif zx > 170:
     #   print(" I am inside the fourth  if")
        me.send_rc_control(0, 0, 0, 15)
        sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        print("x2", zx)
   # print("this is the end of the fourth if")
  else:
      me.send_rc_control(0, 0, 0, 0)

def tracky(zy):
  if zy < 100:
        me.send_rc_control(0, 0, 15, 0)
        sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        print("y1", zy)
   # print("this is the end of the first if")
  elif zy > 100:
        me.send_rc_control(0, 0, -15, 0)
        sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        print("y2", zy)
 #   print("this is the end of the second if")
  else:
      me.send_rc_control(0, 0, 0, 0)


me.send_rc_control(0,0,30,0)

sleep(8.678)

me.send_rc_control(0,0,0,0)

me.streamon()
while True:
#    status, img = cap.read()
#    print(statdus)
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    if img is None:
        continue
    try:
        img, info = findFace(img)
        length = len(info[0])
        zx = info[0][0]
        zy = info[0][1]
        trackarea(info[1])
        trackx(zx)
        tracky(zy)
        #print(info[1])
        #print(zx)
        #print(zy)
    except:
        print("Expection happened")

    cv2.imshow("Image", img)

    cv2.waitKey(1)

 #    print(zx, zy)