import RPi.GPIO as GPIO

gLight = 9


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(gLight, GPIO.OUT)

def my_callback_11(channel):
   print('Edge callback on channel ' & channel)

gpio.addevent_detect(11,
   
while 1:

      
