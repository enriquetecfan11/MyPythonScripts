#Lectura de Valores desde Arduino por el Puerto Serie
#Enrique Rodriguez Vela
#27 de Octubre de 2018
#Version 0.1

#!/usr/bin/python
import serial
import time

#Arduino es una entrada del Puerto Serie por le puerto USB0
arduino=serial.Serial('/dev/ttyUSB0',baudrate=9600, timeout = 3.0)

#Valor de Arduino es una linea del puerto serie
VArduino = arduino.readline()

#Imprimimos por el puerto serie el valor leido de arduino
print(VArduino)
 

arduino.close()
