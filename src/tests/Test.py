from djitellopy import tello
from time import sleep

me = tello.Tello()

me.connect()

print(me.get_battery())

me.takeoff()

me.send_rc_control(0, 0, 60, 0)
sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)

me.send_rc_control(0, 0, 0, 0)

me.land()

