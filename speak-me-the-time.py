#!/usr/bin/env python

#https://gist.github.com/alicraigmile/7f5526c8058e35243dba/edit

import RPi.GPIO as GPIO
import time
import os

JOB = "date +'%d %B %I:%M%p' | festival --tts"
LED_PIN = 8
BUTTON_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN,GPIO.IN)
GPIO.setup(LED_PIN,GPIO.OUT)
print "LED on GPIO" + str(LED_PIN) + "..."
print "Listening for switch on GPIO" + str(BUTTON_PIN )+ "..."

#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0
while True:
  #take a reading
  input = GPIO.input(BUTTON_PIN)
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    print("Button pressed - i'll now run the job")
    #turn on the led
    GPIO.output(LED_PIN,GPIO.HIGH)
    os.system(JOB)
    #flash the led once the job completes and then turn it off
    GPIO.output(LED_PIN,GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(LED_PIN,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN,GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(LED_PIN,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN,GPIO.LOW)
    print "Job complete. Listening again on GPIO" + str(BUTTON_PIN) + "..."
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)
