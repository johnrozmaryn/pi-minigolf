import time
import board    #for neopixels
import neopixel #for neopixels

#exec(open("filename.py").read())

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

pixel_pin = board.D21
num_pixels = 6

def flashStones(rgb):
	for i in range(flashLoops):
	   pixels.fill(rgb)
	   time.sleep(flashOn)
	   pixels.fill((0,0,0))
	   time.sleep(flashOff)

def alloff():
   for i in range(num_pixels):
      pixels.fill((0,0,0))

#Setup neoPixels

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

flashStones(cSpace)
flashStones(cReality)
flashStones(cPower)
flashStones(cMind)
flashStones(cTime)
flashStones(cSoul)

pixels[pSpace] = cSpace
pixels[pReality] = cReality
pixels[pPower] = cPower
pixels[pMind] = cMind
pixels[pTime] = cTime
pixels[pSoul] = cSoul

time.sleep(2)

alloff()

