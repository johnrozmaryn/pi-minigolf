import time
from pygame import mixer

mixer.init()

sndSong = './sound/imperial_march.wav'
sndEffect1 = mixer.Sound('./sound/blaster-firing.wav')
sndEffect2 = mixer.Sound('./sound/R2D2-hey-you.wav')
sndEffect3 = mixer.Sound('./sound/swvader01.wav')

mixer.music.load(sndSong)
mixer.music.play(-1)
time.sleep(5)
sndEffect1.play()
time.sleep(5)
sndEffect2.play()
time.sleep(5)
sndEffect3.play()
time.sleep(5)
mixer.music.pause()
time.sleep(5)
sndEffect1.play()



