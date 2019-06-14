from time import sleep
from pygame import mixer #for sound
import RPi.GPIO as GPIO
import serial #pyserial,for sending commands to the Arduino
import wiringpi

#look here for possibly better PWM for servo:
#https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor/software

########6 stones##########
#Space Stone - Blue
#Reality Stone - Red
#Power Stone - Purple
#Mind Stone - Yellow
#Time Stone - Green
#Soul Stone - Orange

#Sound Files
#background music
#I'm now using absolute paths because of how I call execution in /etc/rc.local
fMusic = '/home/pi/pi-minigolf/snd/av_theme.wav'
#sounds for each gate
fSpace = '/home/pi/pi-minigolf/snd/space.wav'
fReality = '/home/pi/pi-minigolf/snd/reality.wav'
fPower = '/home/pi/pi-minigolf/snd/power.wav'
fMind = '/home/pi/pi-minigolf/snd/mind.wav'
fTime = '/home/pi/pi-minigolf/snd/time.wav'
fSoul = '/home/pi/pi-minigolf/snd/soul.wav'
#end game sounds
fSnap = '/home/pi/pi-minigolf/snd/snap.wav'
fMsg = '/home/pi/pi-minigolf/snd/i-dont-feel-so-good-2.wav'
#boot sound
fReadySound = '/home/pi/pi-minigolf/snd/blaster-firing.wav'

#GPIO Pins for the gates and glove
#fake for now
gSpace = 13
gReality = 27
gPower = 22
gMind = 5
gTime = 17
gSoul = 6
gEnd = 19 #final gate, not a Stone)
gGlove = 18

#Constants to use in the serial commands to the Arduino for pixel stuff
flashSpace = 70
flashReality = 71
flashPower = 72
flashMind= 73
flashTime = 74
flashSoul = 75
rainbowEffect = 90
clearPixels = 99

bitSpace = 1
bitReality = 2
bitPower = 4
bitMind = 8
bitTime = 16
bitSoul = 32

	
#Glove Movement
gloveOpenPos = 100
gloveClosePos = 195
gloveStep = 1
gloveSleep = 0.03     #This was 0.01 in the video
gloveTimeout = 5000	
	
#setup serial connection to the Arduino
#ard = serial.Serial('/dev/ttyACM0', 115200)
ard = serial.Serial('/dev/ttyUSB0', 115200)

#Setup music and some sound effects, don't start yet
# mono instead of stereo
mixer.init(channels = 1)
mixer.music.load(fMusic)
sndSnap = mixer.Sound(fSnap)
sndMsg = mixer.Sound(fMsg)
sndReady = mixer.Sound(fReadySound)

#misc
tParkerDelay = 3

	
#####The Stone class will hold lots of stone related suff
class Stone:
	def __init__(self, name, soundfile, pin, tripped, sndObj, bit, flashCmd):
		self.name = name    		#Stone Name
		self.soundfile = soundfile	#path of sound file, as string
		self.pin = pin				#GPIO pin for the gate associated with this stone 
		self.tripped = tripped		#True/False, has the gate been tripped
		self.sndObj = sndObj		#mixer.sound object
		self.bit = bit          #The bit used to build commands to the Arduino
		self.flashCmd = flashCmd       #The command used to flash all of these colors. Colors stored in Arduino

Stones = []  #this will be the collection of all 6 stones		

sSpace = Stone(
	name = 'Space',
	soundfile = fSpace,
	pin = gSpace,
	tripped = False,
	sndObj = mixer.Sound(fSpace),
	bit = bitSpace,
	flashCmd = flashSpace )
	
Stones.append(sSpace)

sReality = Stone(
	name = 'Reality',
	soundfile = fReality,
	pin = gReality,
	tripped = False,
	sndObj = mixer.Sound(fReality),
	bit = bitReality,
	flashCmd = flashReality )

Stones.append(sReality)

sPower = Stone(
	name = 'Power',
	soundfile = fPower,
	pin = gPower,
	tripped = False,
	sndObj = mixer.Sound(fPower),
	bit = bitPower,
	flashCmd = flashPower )

Stones.append(sPower)

sMind = Stone(
	name = 'Mind',
	soundfile = fMind,
	pin = gMind,
	tripped = False,
	sndObj = mixer.Sound(fMind),
	bit = bitMind,
	flashCmd = flashMind )

Stones.append(sMind)

sTime = Stone(
	name = 'Time',
	soundfile = fTime,
	pin = gTime,
	tripped = False,
	sndObj = mixer.Sound(fTime),
	bit = bitTime,
	flashCmd = flashTime )
	
Stones.append(sTime)	

sSoul = Stone(
	name = 'Soul',
	soundfile = fSoul,
	pin = gSoul,
	tripped = False,
	sndObj = mixer.Sound(fSoul),
	bit = bitSoul,
	flashCmd = flashSoul )

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
   gatePassed.sndObj.play()	#play a sound effect  


#GPIO Config 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Setup GPIO for the stones, includting callback events for everything	
for s in Stones:
	GPIO.setup(s.pin, GPIO.IN, pull_up_down = GPIO.PUD_UP) #change PUD_UP to PUD_DOWN if no response?
	GPIO.add_event_detect(s.pin, GPIO.FALLING, callback=gate_passed, bouncetime = 1000)

#Play bootup sound
sndReady.play()

#testloop
while 1:
      
   sleep(1)							
														
							
							
							
							
#do a pip3 install readchar
#import readchar
#c = readchar.readchar()
#key = readchar.readkey()
#key is really a keystroke, so it handles ctrl- and alt-sequences, things I probably don't need.
#https://pypi.org/project/readchar/
#but this make break ctrl-c, so look at https://github.com/magmax/python-readchar/issues/40

