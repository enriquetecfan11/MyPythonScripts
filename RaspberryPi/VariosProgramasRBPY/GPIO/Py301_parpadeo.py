##-----------------------------------
## Py301_Parpadeo
## Enrique Rodriguez Vela
##-----------------------------------

import RPi.GPIO as GPIO
import time

print("Programa para encender led")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

while(True):
 GPIO.output(18,True)
 GPIO.output(4,True)
 time.sleep(2)
 GPIO.output(18,False)
 GPIO.output(4,False)
 time.sleep(2)
