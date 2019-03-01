from sense_hat import SenseHat
import time

sense = SenseHat()


r = [255,0,0]

g = [0,50,0]
b = [0,0,255]
bl = [108,60,0]
p = [200, 210, 180]

marioDown = [
    g, g, g, r, g, g, g, g,
    g, g, r, r, r, r, g, g,
    g, bl, p, p, p, g, g, g,
    g, bl, p, p, p, g, g, g,
    g, g, r, b, r, g, g, g,
    g, r, b, b, b, r, g, g,
    g, g, b, b, b, g, g, g,
    g, bl, bl, g, bl, bl, g, g,
    ]

marioUp =  [
    g, g, r, r, r, r, g, g,
    g, bl, p, p, p, g, g, g,
    g, bl, p, p, p, r, g, g,
    g, g, r, b, r, g, g, g,
    g, r, b, b, b, g, g, g,
    g, g, b, b, b, g, g, g,
    g, bl, bl, g, bl, bl, g, g,
    g, g, g, g, g, g, g, g,
    ]
sense.clear()


sense.set_pixels(marioDown)

def jump():
        event = sense.stick.wait_for_event()
        if (event):
                sense.set_pixels(marioUp)
                time.sleep(0.2)
                sense.set_pixels(marioDown)
        jump()
jump()
