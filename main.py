from time import sleep
from pygame import mixer #for sound
import RPi.GPIO as GPIO
import board    #for neopixels
import neopixel #for neopixels


########6 stones##########
#Space Stone - Blue
#Reality Stone - Red
#Power Stone - Purple
#Mind Stone - Yellow
#Time Stone - Green
#Soul Stone - Orange

#Sound Files
#background music
fMusic = './snd/av_theme.wav'
#sounds for each gate
fSpace = './snd/space.wav'
fReality = './snd/reality.wav'
fPower = './snd/power.wav'
fMind = './snd/mind.wav'
fTime = './snd/time.wav'
fSoul = './snd/soul.wav'
#end game sounds
fSnap = './snd/snap.wav'
fMsg = './snd/i-dont-feel-so-good-2.wav'
#boot sound
fReadySound = './snd/blaster-firing.wav'

#GPIO Pins for the gates and glove
#fake for now
gSpace = 9
gReality = 3
gPower = 4
gMind = 5
gTime = 6
gSoul = 7
gEnd = 8 #final gate, not a Stone)
gGlove = 13

#Colors
cSpace= (0,0,255)
cReality = (255,0,0)
cPower = (150,0,150)
cMind = (255,255,0)
cTime = (0,255,0)
cSoul = (255,80,0)

#Output neoPixel locations on the string, 0 for first
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
	
#Glove Movement
gloveMin = 5
gloveMax = 12
gloveStep = 0.1
gloveSleep = 0.1
gloveTimeout = 5000	
	

#Setup music and some sound effects, don't start yet
# mono instead of stereo
mixer.init(channels = 1)
mixer.music.load(fMusic)
sndSnap = mixer.Sound(fSnap)
sndMsg = mixer.Sound(fMsg)
sndReady = mixer.Sound(fReadySound)

#misc
tParkerDelay = 3

	
#####Even better stuff here
class Stone:
	def __init__(self, name, soundfile, pin, rgb, tripped, nPixel, sndObj):
		self.name = name    		#Stone Name
		self.soundfile = soundfile	#path of sound file, as string
		self.pin = pin				#GPIO pin for the gate associated with this stone 
		self.rgb = rgb				#List of RGB values (0-255 each), such as (255,0,0) for Red
		self.tripped = tripped		#True/False, has the gate been tripped
		self.nPixel = nPixel		#Address of the NeoPixel associated with the stone
		self.sndObj = sndObj		#mixer.sound object

Stones = []		

sSpace = Stone(
	name = 'Space',
	soundfile = fSpace,
	pin = gSpace,
	rgb = cSpace,
	tripped = False,
	nPixel = pSpace,
	sndObj = mixer.Sound(fSpace) )
	
Stones.append(sSpace)

sReality = Stone(
	name = 'Reality',
	soundfile = fReality,
	pin = gReality,
	rgb = cReality,
	tripped = False,
	nPixel = pReality,
	sndObj = mixer.Sound(fReality) )

Stones.append(sReality)

sPower = Stone(
	name = 'Power',
	soundfile = fPower,
	pin = gPower,
	rgb = cPower,
	tripped = False,
	nPixel = pPower,
	sndObj = mixer.Sound(fPower) )

Stones.append(sPower)

sMind = Stone(
	name = 'Mind',
	soundfile = fMind,
	pin = gMind,
	rgb = cMind,
	tripped = False,
	nPixel = pMind,
	sndObj = mixer.Sound(fMind) )

Stones.append(sMind)

sTime = Stone(
	name = 'Time',
	soundfile = fTime,
	pin = gTime,
	rgb = cTime,
	tripped = False,
	nPixel = pTime,
	sndObj = mixer.Sound(fTime) )
	
Stones.append(sTime)	

sSoul = Stone(
	name = 'Soul',
	soundfile = fSoul,
	pin = gSoul,
	rgb = cSoul,
	tripped = False,
	nPixel = pSoul,
	sndObj = mixer.Sound(fSoul) )

Stones.append(sSoul)

for s in Stones:
	print(s.name)
	

#Stub for logic

def findStoneByChannel(channel):
	for s in Stones:
		if s.pin == channel:
			return s

def gate_passed(channel):
	gatePassed = findStoneByChannel(channel)
	if not mixer.music.get_busy():
	   mixer.music.play()
	if not gatePassed.tripped: #this is the first time the gate has been passed
		gatePassed.tripped = True
		gatePassed.sndObj.play()	#play a sound effect
		flashStones(gatePassed.rgb) #flash all of the stones the color just passed
		for s in Stones:		#finish with only collected stones turned on 
			if not s.tripped:
				pixels[s.nPixel] = (0,0,0)
			else:
				pixels[s.nPixel] = s.rgb

def flashStones(rgb):
	for i in range(flashLoops):
	   pixels.fill(rgb)
	   sleep(flashOn)
	   pixels.fill((0,0,0))
	   sleep(flashOff)

def bAllGatesPassed():	#Returns True if there aren't any untriggered stones
	val = True 
	for s in Stones:
		if not s.tripped:
			val = False
	return val

def openGlove():
   print('open Glove')
   DC = gloveMin
   glovePWM.start(DC)
   glovePWM.ChangeDutyCycle(DC)
   while DC < gloveMax:
      glovePWM.ChangeDutyCycle(DC)
      sleep(gloveSleep)
      DC += gloveStep
      
def closeGlove():
   print('close Glove')
   DC = gloveMax
   glovePWM.start(DC)
   while DC > gloveMin:
      glovePWM.ChangeDutyCycle(DC)
      sleep(gloveSleep)
      DC -= gloveStep
      


def finalGatePassed(): #channel is passed from GPIO, but not used
	mixer.music.stop()
	sndSnap.play()
	pixels.fill((0,0,0))
	sleep(tParkerDelay)
	sndMsg.play()
	for s in Stones:
	   s.tripped = False
	closeGlove()
	
	
#Setup music and some sound effects, don't start yet
 # mono instead of stereo
mixer.music.load(fMusic)
sndSnap = mixer.Sound(fSnap)
sndMsg = mixer.Sound(fMsg)
sndReady = mixer.Sound(fReadySound)

#Setup neoPixels
pixel_pin = board.D21
num_pixels = 6
ORDER = neopixel.RGB
BRIGHTNESS = 0.2    #Experiment with this...
pixels = neopixel.NeoPixel(pixel_pin, num_pixels)
	
#GPIO Config 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Setup GPIO for glove
GPIO.setup(gGlove, GPIO.OUT)
glovePWM = GPIO.PWM(gGlove, 50)
glovePWM.start(gloveMin)
sleep(3)
glovePWM.stop()


#Setup GPIO for the stones, includting callback events for everything	
for s in Stones:
	GPIO.setup(s.pin, GPIO.IN, pull_up_down = GPIO.PUD_UP) #change PUD_UP to PUD_DOWN if no response?
	GPIO.add_event_detect(s.pin, GPIO.FALLING, callback=gate_passed, bouncetime = 200)
	

#Setup GPIO for exit chute
GPIO.setup(gEnd, GPIO.IN, pull_up_down = GPIO.PUD_UP) #needs same pullup/pulldown value as the stone gates

#Play bootup sound
sndReady.play()

#testloop
while 1:
   testInput = input()
   if testInput == '1':
      gate_passed(gSpace)
   elif testInput == '2':
      gate_passed(gReality)
   elif testInput == '3':
      gate_passed(gPower)
   elif testInput == '4':
      gate_passed(gMind)
   elif testInput == '5':
      gate_passed(gTime)
   elif testInput == '6':
      gate_passed(gSoul)
   elif testInput == 'q':
      quit()
      
   if bAllGatesPassed():
      openGlove()
      GPIO.wait_for_edge(gEnd, GPIO.FALLING, timeout = gloveTimeout)
      finalGatePassed()
      
   sleep(1)							
							
							
							
							
							
							
#do a pip3 install readchar
#import readchar
#c = readchar.readchar()
#key = readchar.readkey()
#key is really a keystroke, so it handles ctrl- and alt-sequences, things I probably don't need.
#https://pypi.org/project/readchar/
#but this make break ctrl-c, so look at https://github.com/magmax/python-readchar/issues/40

