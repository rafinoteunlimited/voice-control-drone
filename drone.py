import sys
from djitellopy import Tello
from sys import argv
import time

tello = Tello()
tello.connect()
time.sleep(0.5)

print(tello.get_battery())

if argv[1] == "takeoff":
    tello.takeoff()
elif argv[1] == "land":
    tello.land()
elif argv[1] == "forward":
    tello.move_forward(70)
elif argv[1] == "left":
    tello.move_left(70)
elif argv[1] == "right":
    tello.move_right(70)
elif argv[1] == "back":
    tello.move_back(70)
elif argv[1] == "flip":
    tello.flip_forward()
elif argv[1] == "up":
    tello.move_up()
elif argv[1] == "down":
    tello.move_down
