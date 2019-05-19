import time
from pygame import mixer

mixer.init()

sndSong = mixer.Sound('./sound/imperial_march.wav')
sndEffect1 = mixer.Sound('./sound/blaster-firing.wav')
sndEffect2 = mixer.Sound('./sound/R2D2-hey-you.wav')
sndEffect3 = mixer.Sound('/sound/swvader01.wav')

sndSong.play()
time.sleep(5)
sndEffect1.play()
time.sleep(5)
sndEffect2.play()
time.sleep(5)
sndEffect3.play()
time.sleep(5)
sndSong.stop()
time.sleep(2)
sndEffect1.play()



