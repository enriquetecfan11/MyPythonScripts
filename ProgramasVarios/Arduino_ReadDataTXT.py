#Lectura de Valores desde Arduino por el Puerto Serie y puestos en fichero
#Enrique Rodriguez Vela
#28 de Octubre de 2018
#Version 0.2

import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

#Conventir bytes a string
data = ser.readline().decode("utf-8")
#print(data)

#Ver Fecha y hora de los datos
import time
#print("Fecha y hora" + time.strftime("%c") +'\n')

#Abrimos un archivo de lectura.txt
f=open('dataFile.txt','a')

# Bucle infinito para leer todos los datos
while 1:
    f.write(ser.readline().decode("utf-8"))
    f.close()
    f=open('dataFile.txt','a')
