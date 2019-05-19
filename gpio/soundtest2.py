import time
from pygame import mixer

mixer.init()

sndSong = mixer.Sound('./sound/imperial_march.wav')
sndEffect1 = mixer.Sound('./sound/blaster-firing.wav')
sndEffect2 = mixer.Sound('./sound/R2D2-hey-you.wav')
sndEffect3 = mixer.Sound('./sound/swvader01.wav')

sndSong.Channel(0).play(sndSong)
time.sleep(5)
sndEffect1.Channel(1).play(sndEffect1)
time.sleep(5)
sndEffect2.Channel(2).play(sndEffect2)
time.sleep(5)
sndEffect3.Channel(3).play(sndEffect3)
time.sleep(5)
sndSong.Channel(0).stop()
time.sleep(2)
sndEffect1.Channel(1).play(sndEffect1)



