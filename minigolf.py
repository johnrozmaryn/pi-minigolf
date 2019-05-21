#!/usr/bin/python3

#Starting skeleton for the golf course

from time import sleep
from pygame import mixer
import RPi.GPIO as GPIO

#import datetime

########6 stones##########
#Space Stone - Blue
#Reality Stone - Red
#Power Stone - Purple
#Mind Stone - Yellow
#Time Stone - Green
#Soul Stone - Orange

#GPIO Pins for the gates
#fake for now
print('\nSetting up constants')
gSpace = 2
gReality = 3
gPower = 4
gMind = 5
gTime = 6
gSoul = 7
gEnd = 8 #final gate, not a Stone)
gList = (gSpace, gReality, gPower, gMind, gTime, gSoul, gEnd)
gStones = (gSpace, gReality, gPower, gMind, gTime, gSoul)

##Color translations
cSpace = (0,0,255)
cReality = (255,0,0)
cPower = (255,0,0)
cMind = (255,255,0)
cTime = (0,255,0)
cSoul = (255,180,0)


#####Sound Files
fMusic = './snd/imperial_march.wav'
fSpace = './snd/blaster-firing.wav'
fReality = './snd/blaster-firing.wav'
fPower = './snd/blaster-firing.wav'
fMind = './snd/blaster-firing.wav'
fTime = './snd/blaster-firing.wav'
fSoul = './snd/blaster-firing.wav'
fSnap = './snd/R2D2-hey-you.wav'
fMsg = './snd/swvader01.wav'

print('...Done!')

#setup GPIO
print('Setting up GPIO')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#setup input pins
#All of the gates, with the on-board pulldown enabled
for g in gList:
	GPIO.setup(g,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print('...Done!')

#setup sound files
print('Initializing Audio')
mixer.init(channels = 1) # mono instead of stereo
mixer.music.load(fMusic)
sndSpace = mixer.Sound(fSpace)
sndReality = mixer.Sound(fReality)
sndPower = mixer.Sound(fPower)
sndMind = mixer.Sound(fMind)
sndTime = mixer.Sound(fTime)
sndSoul = mixer.Sound(fSoul)
sndSnap = mixer.Sound(fSnap)
sndMsg = mixer.Sound(fMsg)

print('...Done!')


#setup NeoPixels
#setup ServoThingy?
	





