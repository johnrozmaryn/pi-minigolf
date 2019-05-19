import RPi.GPIO as GPIO
import time
import datetime
while 1==1 :
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(9,GPIO.OUT)
	GPIO.setup(10,GPIO.OUT)
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(9,GPIO.HIGH)
	GPIO.output(10,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(11,GPIO.LOW)
	GPIO.output(9,GPIO.LOW)
	GPIO.output(10,GPIO.LOW)
	time.sleep(1)
	print(str(datetime.datetime.now()))


