  
from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

letters = ["N", "M", "D"]

def my_Function():
	for i in letters:
		colour = (randint(0,255), randint(0,255), randint(0,255))
		sense.show_letter(i, text_colour=colour)
		time.sleep(1)
	time.sleep(2)
	my_Function()
	
my_Function()
