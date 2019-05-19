import time
from pygame import mixer
mixer.init(channels=1)

mixer.music.load('./sound/imperial_march.wav')
sndEffect1 = mixer.Sound('./sound/blaster-firing.wav')
sndEffect2 = mixer.Sound('./sound/R2D2-hey-you.wav')
sndEffect3 = mixer.Sound('./sound/swvader01.wav')

mixer.music.play()
time.sleep(2)
mixer.Channel(0).play(sndEffect1)
time.sleep(2)
mixer.Channel(1).play(sndEffect2)
time.sleep(2)
mixer.Channel(2).play(sndEffect3)
time.sleep(2)
mixer.music.fadeout(1000)
time.sleep(3)
mixer.find_channel()
free_channel = mixer.find_channel()
free_channel.play(sndEffect1)
time.sleep(2)
free_channel = mixer.find_channel()
free_channel.play(sndEffect1)
time.sleep(2)
free_channel = mixer.find_channel()
free_channel.play(sndEffect1)

