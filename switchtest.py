import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)

GPIO.setup(14,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
   if GPIO.input(14) and GPIO.input(15):
      GPIO.output(11, True)
      GPIO.output(9, False)
      GPIO.output(10, False)
#      print('14 and 15 on')
   else:
      GPIO.output(11, False)
#      print('14 and 15 not both on')
      if GPIO.input(14):
         GPIO.output(10, True)
#         print('14 only on')		
      else:
         GPIO.output(10, False)

      if GPIO.input(15):
         GPIO.output(9, True)
#         print('15 only on')
      else:
         GPIO.output(9, False)


