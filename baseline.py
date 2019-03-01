from sense_hat import  SenseHat
import time
from random import randint
sense = SenseHat()

message = "Hello! We are New Media Development :)"

def my_Function(message):
    backgroundColour = (randint(0,100), randint(0,100), randint(0,100))
    messageColour = (randint(0,255), randint(0,255), randint(0,255))
    sense.show_message(message, text_colour=messageColour, back_colour=backgroundColour)
    my_Function(message)
    
my_Function(message)
