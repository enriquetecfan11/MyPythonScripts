#Prueba Lectura de datos por Serial
#Enrique Rodriguez Vela
#Noviembre de 2018
#Version 0.2

import serial
ser= serial.Serial("/dev/ttyACM0", 9600)

print(ser)

#Ver Fecha y hora de los datos
import time

print("Fecha y hora" + time.strftime("%c") +'\n')

while True:
  # Pasamos de formato bytes a string para poder manipular mejor los datos
  data = ser.readline().decode("utf-8")
  print(data)
