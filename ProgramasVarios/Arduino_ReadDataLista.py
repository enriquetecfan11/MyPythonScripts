#Lectura de Valores desde Arduino por el Puerto Serie y en una lista
#Enrique Rodriguez Vela
#28 de Octubre de 2018
#Version 0.2

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

#Ver Fecha y hora de los datos
import time
#print("Fecha y hora" + time.strftime("%c") +'\n')

#Crea la lista de datos
datos = [ser.readline(), time.strftime("%c")]

#Ver Fecha y hora de los datos
import time
#print("Fecha y hora" + time.strftime("%c") +'\n')

#Abrimos un archivo de lectura.txt
f=open('dataFile.txt','a')

# Bucle infinito para leer todos los datos
while 1:
    f.write(str(datos) + '\n')
    time.sleep(0.02)
    f.close()
    f=open('dataFile.txt','a')
