import time
import board    #for neopixels
import neopixel #for neopixels

cSpace= (0,0,255)
cReality = (255,0,0)
cPower = (255,0,0)
cMind = (255,255,0)
cTime = (0,255,0)
cSoul = (255,180,0)

pSpace = 0
pReality = 1
pPower = 2
pMind = 3
pTime = 4
pSoul = 5

#Color Flashing
flashLoops	= 3
flashOn = 0.5
flashOff = 0.2

def flashStones(rgb):
	for i in range(flashLoops):
	   pixels.fill(rgb)
	   time.sleep(flashOn)
	   pixels.fill((0,0,0))
	   time.sleep(flashOff)

#Setup neoPixels
pixel_pin = board.D18
num_pixels = 1
ORDER = neopixel.RGB
BRIGHTNESS = 0.2    #Experiment with this...
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness = BRIGHTNESS, auto_write = True, pixel_order = ORDER)

