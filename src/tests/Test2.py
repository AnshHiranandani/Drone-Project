from djitellopy import tello
import time

from time import sleep

me = tello.Tello()

me.connect()

me.takeoff()

me.send_rc_control(0, 10, 0, 0)
sleep(0.1)