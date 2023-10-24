##-----------------------------------
## Py302_Secuencia
## Enrique Rodriguez Vela
##-----------------------------------
import RPi.GPIO as GPIO
import time

print("Programa para encender led")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)


while(True):
   GPIO.output(18,True)
   time.sleep(0.4)
   GPIO.output(18,False)
   GPIO.output(23,True)
   time.sleep(0.4)
   GPIO.output(23,False)
   GPIO.output(24,True)
   time.sleep(0.4)
   GPIO.output(24,False)
   GPIO.output(25,True)
   time.sleep(0.4)
   GPIO.output(25,False)
   GPIO.output(4,True)
   time.sleep(0.4)
   GPIO.output(4,False)
 