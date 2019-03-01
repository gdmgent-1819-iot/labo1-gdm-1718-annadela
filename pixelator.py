from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

pixel = range(0,8)

def my_Function():
    for i in pixel:
        for a in pixel:
            sense.clear()
            sense.set_pixel(i, a, (randint(0,255), randint(0,255), randint(0,255)))
            time.sleep(0.1)
    my_Function()
my_Function()
