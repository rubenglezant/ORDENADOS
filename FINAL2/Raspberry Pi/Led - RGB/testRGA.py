#!/usr/bin/python
import time
import RPi.GPIO as GPIO

#LED CONFIG - Set GPIO Ports
PIN1 = 17   #B4
PIN2 = 27   #B18
PIN3 = 22   #B23
LED = [PIN1,PIN2,PIN3]

#Set up the wiring
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
# Setup Ports
for val in LED:
  GPIO.setup(val, GPIO.OUT)

GPIO.output(LED,[0,0,0])
time.sleep(3)
GPIO.output(LED,[0,0,1])
time.sleep(3)
GPIO.output(LED,[0,1,0])
time.sleep(3)
GPIO.output(LED,[0,1,1])
time.sleep(3)
GPIO.output(LED,[1,0,0])
time.sleep(3)
GPIO.output(LED,[1,0,1])
time.sleep(3)
GPIO.output(LED,[1,1,0])
time.sleep(3)
GPIO.output(LED,[1,1,1])
time.sleep(3)
