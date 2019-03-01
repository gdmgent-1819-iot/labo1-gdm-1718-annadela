from sense_hat import SenseHat
import time
from random import randint, random

sense = SenseHat()
halfsense = range(0,4)
fullsense = range(0,8)

def randAvatar():
	randColour = (randint(0,255), randint(0,255), randint(0,255))
	for i in halfsense:
		for a in fullsense:
			if(random() < 0.7):
			    sense.set_pixel(i,a,randColour)
			    sense.set_pixel((7-i), a, randColour)
	time.sleep(1)
	sense.clear()
	randAvatar()
				
randAvatar()
