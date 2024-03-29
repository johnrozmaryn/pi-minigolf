import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(2,GPIO.IN, pull_up_down=GPIO.PUD_UP)

import time

pwm = GPIO.PWM(21,50)

pwm.start(5)

DCLow = 4.5
DCHigh = 12
DC = 5
sNum = 0.05
DCdelta = .1

pwm.ChangeDutyCycle(DCLow)

while 1:
   if GPIO.input(2):
      print('High')
   else:
      print('Low')         
      while DC < DCHigh:
         pwm.ChangeDutyCycle(DC)
         time.sleep(sNum)
         DC += DCdelta

      GPIO.cleanup()
      quit()

   time.sleep(.1)
       

   
GPIO.cleanup()
