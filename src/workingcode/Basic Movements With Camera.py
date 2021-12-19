from djitellopy import tello

import cv2

from time import sleep

me = tello.Tello()

me.connect()

print(me.get_battery())

me.streamon()

me.takeoff()

for x in range(1000):
    img = me.get_frame_read().frame

    img = cv2.resize(img, (360, 240))

    cv2.imshow("Image", img)

    cv2.waitKey(1)

    me.send_rc_control(0, 10, 0, 0)

    sleep(0.0001)


me.land()