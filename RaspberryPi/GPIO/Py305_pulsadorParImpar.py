##-----------------------------------
## Py305_pulsadorParImpar
## Enrique Rodriguez Vela
##-----------------------------------

import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Led Impares
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24,  GPIO.OUT)
GPIO.setup(4,  GPIO.OUT)

#Led Pares
GPIO.setup(23,  GPIO.OUT)
GPIO.setup(25,  GPIO.OUT)

#Pulsadores
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    input_state_01 = GPIO.input(22)
    input_state_02 = GPIO.input(27)
    
    if input_state_01 == False:
        print("Boton Presionado Nº1")
        GPIO.output(18,True)
        GPIO.output(24,True)
        GPIO.output(4,True)
        time.sleep(0.2)
    else:
        GPIO.output(18,False)
        GPIO.output(24,False)
        GPIO.output(4,False)
        
        
    if input_state_02 == False:
        print("Boton Presionado Nº1")
        GPIO.output(23,True)
        GPIO.output(25,True)
        time.sleep(0.2)
    else:
        GPIO.output(23,False)
        GPIO.output(25,False)

GPIO.cleanup()