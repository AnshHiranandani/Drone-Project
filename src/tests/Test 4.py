import cv2
import numpy as np
from djitellopy import tello
import time
from time import sleep

TIME_BTW_RC_CONTROL_COMMANDS = 0.001
def findFace(img):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "./haarcascade_upperbody.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
         cx = x + w//2
         cy = y + h//2
         area = w * h
         cv2.circle(img,(cx,cy),5,(0,255,0) , cv2.FILLED)
         myFaceListC.append([cx,cy])
         myFaceListArea.append(area)
         if len(myFaceListArea) != 0:
             i = myFaceListArea.index(max(myFaceListArea))
             #return img, [myFaceListC[i],myFaceListArea[i]]
         else:
             print("No upper body detected")

def trackarea(area):
  if area > 12000:
      me.send_rc_control(0, 15, 0, 0)
      sleep(0.01)
      print ("area greater than 12000", area)
  elif area < 10000:
      me.send_rc_control(0, -15, 0, 0)
      sleep(0.01)
      print ("area less than 10000", area)
  else:
      me.send_rc_control(0, 0, 0, 0)
      print ("Stabilizing drone in area", area)
      sleep(0.01)

def trackx(zx):
  if zx < 170:
        me.send_rc_control(-15, 0, 0, 0)
        sleep(0.01)
        print("x1 less than 160", zx)
  elif zx > 190:
        me.send_rc_control(15, 0, 0, 0)
        sleep(0.01)
        print("x2 greater than 200", zx)
  else:
        me.send_rc_control(0, 0, 0, 0)
        print("stabilizing drone in X", zx)
        sleep(0.01)

def tracky(zy):
  if zy < 140:
        me.send_rc_control(0, 0, 15, 0)
        sleep(0.01)
        print("y1 is less than 140 ", zy)
  elif zy > 150:
        me.send_rc_control(0, 0, -15, 0)
        sleep(0.01)
        print("y1 is more than 150", zy)
  else:
        me.send_rc_control(0, 0, 0, 0)
        print ("Stabilizing drone in Y", zy)
        sleep(0.01)


# main code start here

me = tello.Tello()
# DO NOT DO THIS WITHOUT CONSULTING HIREN -> me.connect_to_wifi("FiOS-C3AKC","index5759six46host")
me.connect()
print(me.get_battery())

#me.takeoff()
me.send_rc_control(0,0,25,0)
sleep(8.678)

me.send_rc_control(0,0,0,0)
sleep(0.001)

me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    if img is None:
        continue
    try:
        img, info = findFace(img)
        length = len(info[0])
        zx = info[0][0]
        zy = info[0][1]
        print ("area zx zy", info[1], zx, zy)
        trackarea(info[1])
        trackx(zx)
        tracky(zy)

    except:
        print("Exception happened")
        # me.send_rc_control(0,0,0,0)
        # sleep (0.01)

    cv2.imshow("Image", img)
    cv2.waitKey(1)