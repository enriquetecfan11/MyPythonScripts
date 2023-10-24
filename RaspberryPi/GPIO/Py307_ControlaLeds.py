##-----------------------------------
## Py307_ControlaLeds
## Enrique Rodriguez Vela
##-----------------------------------

import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Todos Led
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24,  GPIO.OUT)
GPIO.setup(4,  GPIO.OUT)
GPIO.setup(23,  GPIO.OUT)
GPIO.setup(25,  GPIO.OUT)

GPIO.output(18,False)
GPIO.output(4,True)

entrada=True

print("Programa para encender led")
while (entrada==True):
    respuesta=input("Pulse E para encender led, A para apagar, I para led impares, P para led pares y s para salir. Respuesta =  ")
     
    if (respuesta == "e"):
        GPIO.output(18,True)
        GPIO.output(24,True)
        GPIO.output(4,True)
        GPIO.output(23,True)
        GPIO.output(25,True)
            
    if (respuesta == "a"):
        GPIO.output(18,False)
        GPIO.output(24,False)
        GPIO.output(4,False)
        GPIO.output(23,False)
        GPIO.output(25,False)
           
    if (respuesta == "i"):
        GPIO.output(18,True)
        GPIO.output(24,True)
        GPIO.output(4,True)
           
    if (respuesta == "p"):
        GPIO.output(23,True)
        GPIO.output(25,True)
                   
    if (respuesta == "s"):
        entrada = False
        print("\nAdios......")

GPIO.cleanup()