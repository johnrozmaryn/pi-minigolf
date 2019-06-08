from gpiozero import Button
import os
Button(16).wait_for_press()
os.system("sudo poweroff")
