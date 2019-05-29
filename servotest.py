import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

import time

pwm = GPIO.PWM(18,50)

pwm.start(5)

DCLow = 4.5
DCHigh = 12
DC = 5
sNum = 0.05
DCdelta = .1

pwm.ChangeDutyCycle(DCLow)

while DC < DCHigh:
   pwm.ChangeDutyCycle(DC)
   time.sleep(sNum)
   DC += DCdelta
   
GPIO.cleanup()
