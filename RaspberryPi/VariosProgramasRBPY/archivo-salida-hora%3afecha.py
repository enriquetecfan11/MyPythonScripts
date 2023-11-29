#Archivo de salia mas la hora y fecha actual del sistema
#Enrique Rodriguez Vela
#1 de Noviembre de 2018
#!/usr/bin/python

import time

f = open ('holamundo.txt','w')

f.write('Temperatura 25 y Humedad 50' +'\n')
f.write("Fecha y hora" + time.strftime("%c") +'\n')
f.close()
