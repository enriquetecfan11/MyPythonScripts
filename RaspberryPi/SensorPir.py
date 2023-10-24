
##-----------------------------------
## Py301_Parpadeo
## Enrique Rodriguez Vela
##-----------------------------------

import RPi.GPIO as GPIO
import time

print("Programa para leer desde un Sensor PIR")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN)  #Pin del PIR
GPIO.setup(11, GPIO.OUT) # Pin del led

while True:
   if GPIO.input(7):
        print("leido")
        GPIO.output(11, True)
        time.sleep(0.5)
   else:
        print("No")
        GPIO.output(11, False)
        time.sleep(0.5)


        