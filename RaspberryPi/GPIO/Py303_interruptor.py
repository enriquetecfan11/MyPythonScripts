##-----------------------------------
## Py303_Interruptor
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
     interruptor = GPIO.input(22)
    if interruptor == False:
        GPIO.output(4,False)
        GPIO.output(18,True)

    else:
        GPIO.output(18,False)
        GPIO.output(4,True)