import cv2
import numpy as np
from djitellopy import tello



me = tello.Tello()

me.connect()

def findFace(img):
    faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
    imgGray: None = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces: None = faceCascade.detectMultiScale(imgGray, 1.2, 8)


    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


me.streamon()
while True:
#    status, img = cap.read()
#    print(statdus)
    print("Image is not")
    img = me.get_frame_read().frame

    img = cv2.resize(img, (360, 240))
    if img is None:
        continue
    findFace(img)

    cv2.imshow("Image", img)

    cv2.waitKey(1)