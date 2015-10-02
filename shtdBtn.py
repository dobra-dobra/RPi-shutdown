#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import os

gpioPin = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpioPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
   GPIO.wait_for_edge(gpioPin, GPIO.FALLING)
   start = time.time()
   time.sleep(0.01)
   GPIO.wait_for_edge(gpioPin, GPIO.RISING)
   stop = time.time()
   interval = stop - start
   if interval < 1:
      os.system("sudo reboot")
   else:
      os.system("sudo shutdown -h now")
except:
   pass

GPIO.cleanup()
