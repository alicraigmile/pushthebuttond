#!/usr/bin/env python

#https://gist.github.com/alicraigmile/7f5526c8058e35243bda

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
print "Listening on GPIO17..."

prev_input = 0
while True:
	input = GPIO.input(17)
	if ((not prev_input) and input):
		print "Button pressed - I will now speak the time"
		os.system("date +'%d %B %I:%M %p' | festival --tts")
	prev_input = input
	time.sleep(0.05)
