from pygame import mixer #for sound
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.IN, pull_up_down=GPIO.PUD_UP)

mixer.init(channels = 1)
sndReady = mixer.Sound('./snd/time.wav')



import time

def print_msg(channel):  #channel passed, but not used
   print("gate tripped")
   sndReady.play()



GPIO.add_event_detect(2, GPIO.FALLING, callback=print_msg, bouncetime = 200)  
while 1:
#   GPIO.add_event_detect(2, GPIO.FALLING, callback=print_msg, bouncetime = 200, timeout = 2000)    
   time.sleep(1)
#   print("timeout")


   
GPIO.cleanup()
