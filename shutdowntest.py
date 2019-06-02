#!/usr/bin/python3
#does that line need to be '/usr/bin/env python'? 'python3'?

#This is from the following website:
#https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi

#when done, move it to /usr/local/bin
#chmod +x the file
#move the accompanying .sh file to /etc/init.d and chmod +x it as well

import RPi.GPIO as GPIO
import subprocess
#define GPIO pin to be used for shutdown here
gPin = 2


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(gPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(gPin, GPIO.FALLING)
print("powering down")
#subprocess.call(['shutdown', '-h', 'now'], shell=False)
