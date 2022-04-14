import cv2
import numpy as np
from djitellopy import tello
import time
from time import sleep
import smtplib

TIME_BTW_RC_CONTROL_COMMANDS = 0.001

def findFace(img):
    # faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "./haarcascade_upperbody.xml")
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "./haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
    myFaceListC = []
    myFaceListArea = []
    count = len (faces)
    if count > 1:
        print ("There is an INTRUDER")
    # if (emailcount == 1):
    #     try:
    #         # create your SMTP session
    #         print ("i am just before 587")
    #         smtp = smtplib.SMTP('smtp.gmail.com',587)
    #         print ("i am just after 587")
    #
    #         # use TLS to add security
    #         smtp.starttls()
    #
    #     # user Authentication
    #         smtp.login("phillippirrip858@gmail.com", "yet12345678")
    #
    #     # defining The Message
    #         message = "There is an intruder"
    #
    #     # sending the Email
    #         smtp.sendmail("phillippirrip858@gmail.com", "adages.bendy_0l@icloud.com", message)
    #
    #     # terminating the session
    #         smtp.quit()
    #         print("Email sent successfully!")
    #         emailcount = emailcount + 1
    #
    #     except Exception as ex:
    #         print("Something went wrong while sending email....")

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        print("No person detected")


def trackarea(area):
    # if area > 12000:
    if area > 3900:
        me.send_rc_control(0, -30, 0, 0)
        sleep(0.05)
        print("area greater than 3900", area)
    elif area < 3600:
        me.send_rc_control(0, 30, 0, 0)
        sleep(0.05)
        print("area less than 3600", area)
    else:
        me.send_rc_control(0, 0, 0, 0)
        print("Stabilizing drone in area", area)
        sleep(0.05)


def trackx(zx):
    if zx < 160:
        me.send_rc_control(-30, 0, 0, 0)
        sleep(0.05)
        print("x1 less than 150", zx)
    elif zx > 200:
        me.send_rc_control(30, 0, 0, 0)
        sleep(0.05)
        print("x2 greater than 210", zx)
    else:
        me.send_rc_control(0, 0, 0, 0)
        print("stabilizing drone in X", zx)
        sleep(0.05)


def tracky(zy):
    if zy < 100:
        me.send_rc_control(0, 0, 30, 0)
        sleep(0.05)
        print("y1 is less than 90 ", zy)
    elif zy > 140:
        me.send_rc_control(0, 0, -30, 0)
        sleep(0.05)
        print("y1 is more than 150", zy)
    else:
        me.send_rc_control(0, 0, 0, 0)
        print("Stabilizing drone in Y", zy)
        sleep(0.05)


# main code start here

me = tello.Tello()
# me.connect_to_wifi("FiOS-C3AKC","index5759six46host")
# me.connect_to_wifi("SMH","f0abcdeff0")

me.connect()
print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 0, 25, 0)
sleep(8.678)

me.send_rc_control(0, 0, 0, 0)
sleep(0.001)
count = 0
emailcount = 1
me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    if img is None:
        continue
    try:
        img, info = findFace(img)
        zx = info[0][0]
        zy = info[0][1]
        # print("area zx zy count ", info[1], zx, zy, count)
        trackarea(info[1])
        trackx(zx)
        tracky(zy)
    except:
        print("Exception happened")

    cv2.imshow("Image", img)
    cv2.waitKey(1)