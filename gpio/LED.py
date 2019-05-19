import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.output(11,GPIO.HIGH)
time.sleep(1)
GPIO.output(11,GPIO.LOW)
GPIO.output(9,GPIO.HIGH)
time.sleep(1)
GPIO.output(9,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(1)
GPIO.output(10,GPIO.LOW)


