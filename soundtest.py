import time
from pygame import mixer
mixer.init(channels=1)

mixer.music.load('./snd/imperial_march.wav')
sndEffect1 = mixer.Sound('./snd/blaster-firing.wav')
sndEffect2 = mixer.Sound('./snd/R2D2-hey-you.wav')
sndEffect3 = mixer.Sound('./snd/swvader01.wav')

mixer.music.play()
time.sleep(2)
sndEffect1.play()
time.sleep(2)
sndEffect2.play()
time.sleep(2)
sndEffect3.play()
time.sleep(2)
mixer.music.fadeout(1000)
time.sleep(3)
sndEffect1.play()
time.sleep(1)
