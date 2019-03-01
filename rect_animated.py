from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()
sense.clear()
pixel = range(0,8)

for i in pixel:
    sense.set_pixel(i, 0, (255,255,255))
    sense.set_pixel(i, i, (255,255,0))
    sense.set_pixel(0, i, (255,0,0))
    time.sleep(0.5)
