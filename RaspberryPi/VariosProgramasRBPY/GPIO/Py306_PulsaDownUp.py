##-----------------------------------
## Py306_PulsaDownUp
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

#Pulsadores
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

x=1 #Derecha

print("Py306_PulsaUpDown")

while True:
    
    input_state_01 = GPIO.input(22)
    input_state_02 = GPIO.input(27)
  
    if (x==0):
        if input_state_01 == False:
             print("Boton Presionado Nº1")
             time.sleep(0.5)
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
             x = 1 #esta en la derecha
    
    
    if (x==1):  
        if input_state_02 == False:
            print("Boton Presionado Nº2")
            time.sleep(0.5)
            GPIO.output(4,True)
            time.sleep(0.4)
            GPIO.output(4,False)
            GPIO.output(25,True)
            time.sleep(0.4)
            GPIO.output(25,False)
            GPIO.output(24,True)
            time.sleep(0.4)
            GPIO.output(24,False)
            GPIO.output(23,True)
            time.sleep(0.4)
            GPIO.output(23,False)
            GPIO.output(18,True)
            x = 0

GPIO.cleanup()
