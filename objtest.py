from time import sleep
#from pygame import mixer

########6 stones##########
#Space Stone - Blue
#Reality Stone - Red
#Power Stone - Purple
#Mind Stone - Yellow
#Time Stone - Green
#Soul Stone - Orange



fMusic = './snd/imperial_march.wav'
fMusic = './snd/imperial_march.wav'
fSpace = './snd/blaster-firing.wav'
fReality = './snd/blaster-firing.wav'
fPower = './snd/blaster-firing.wav'
fMind = './snd/blaster-firing.wav'
fTime = './snd/blaster-firing.wav'
fSoul = './snd/blaster-firing.wav'
fSnap = './snd/R2D2-hey-you.wav'
fMsg = './snd/swvader01.wav'

#mixer.init(channel = 1) # mono instead of stereo
#mixer.music.load(fMusic)
#sndSoul = mixer.Sound(fSpace)
#sndReality = mixer.Sound(fReality)
#sndPower = mixer.Sound(fPower)
#sndMind = mixer.Sound(fMind)
#sndTime = mixer.Sound(fTime)
#sndSoul = mixer.Sound(fSoul)
#sndSnap = mixer.Sound(fSnap)
#sndMsg = mixer.Sound(fMsg)


#GPIO Pins for the gates
#fake for now
gSpace = 2
gReality = 3
gPower = 4
gMind = 5
gTime = 6
gSoul = 7
gEnd = 8 #final gate, not a Stone)

#Colors
cSpace= (0,0,255)
cReality = (255,0,0)
cPower = (255,0,0)
cMind = (255,255,0)
cTime = (0,255,0)
cSoul = (255,180,0)

#OutputPixel
pSpace = 0
pReality = 1
pPower = 2
pMind = 3
pTime = 4
pSoul = 5
	
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
#	sndObj = mixer.Sound(fSpace) )
	sndObj = fSpace )	
Stones.append(sSpace)

sReality = Stone(
	name = 'Reality',
	soundfile = fReality,
	pin = gReality,
	rgb = cReality,
	tripped = False,
	nPixel = pReality,
#	sndObj = mixer.Sound(fReality) )
	sndObj = fReality )	
Stones.append(sReality)

sPower = Stone(
	name = 'Power',
	soundfile = fPower,
	pin = gPower,
	rgb = cPower,
	tripped = False,
	nPixel = pPower,
#	sndObj = mixer.Sound(fPower) )
	sndObj = fPower )	
Stones.append(sPower)

sMind = Stone(
	name = 'Mind',
	soundfile = fMind,
	pin = gMind,
	rgb = cMind,
	tripped = False,
	nPixel = pMind,
#	sndObj = mixer.Sound(fMind) )
	sndObj = fMind )	
Stones.append(sMind)

sTime = Stone(
	name = 'Time',
	soundfile = fTime,
	pin = gTime,
	rgb = cTime,
	tripped = False,
	nPixel = pTime,
#	sndObj = mixer.Sound(fTime) )
	sndObj = fTime )	
Stones.append(sTime)	

sSoul = Stone(
	name = 'Soul',
	soundfile = fSoul,
	pin = gSoul,
	rgb = cSoul,
	tripped = False,
	nPixel = pSoul,
#	sndObj = mixer.Sound(fSoul) )
	sndObj = fSoul )	
Stones.append(sSoul)

for s in Stones:
	print(s.name)

	



#do a pip3 install readchar
#import readchar
#c = readchar.readchar()
#key = readchar.readkey()
#key is really a keystroke, so it handles ctrl- and alt-sequences, things I probably don't need.
#https://pypi.org/project/readchar/
#but this make break ctrl-c, so look at https://github.com/magmax/python-readchar/issues/40

