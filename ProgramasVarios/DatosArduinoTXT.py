#Lectura de Valores desde Arduino por el Puerto Serie y puestos en fichero
#Enrique Rodriguez Vela
#28 de Octubre de 2018
#Version 0.2

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

# Pasamos de formato bytes a string para poder manipular mejor los datos
data = ser.readline().decode("utf-8")

#Abrimos un archivo de lectura.txt
f=open('dataFile.csv','a')

# Bucle infinito para leer todos los datos
while 1:
    time.sleep(5)
    f.write(ser.readline().decode("utf-8") + '\n' + ";")
    f.write('\n')
    f.write(time.strftime("%c") + '\n' + ";")
    f.write('\n')
    f.close()
    f=open('dataFile.csv','a')


