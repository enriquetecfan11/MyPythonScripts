#Lectura de datos Serial + txt + csv
#Enrique Rodriguez Vela
#Noviembre de 2018
#Version PC


import serial
ser= serial.Serial("/dev/ttyACM0", 9600)

#Ver Fecha y hora de los datos
import time
#print("Fecha y hora" + time.strftime("%c") +'\n')

#Importamos la libreria CSV
import csv

# Pasamos de formato bytes a string para poder manipular mejor los datos
data = ser.readline().decode("utf-8")

# miramos la longitud de la cadena
temp = len(data)
# y quitamos los utlimos 10 caracteres
data01 = data[:temp - 10]

#Creamos una lista de datos
datos = [data01]

#Creamos una lista del tiempo real
tiempo =[time.strftime("%c")]

#Lista para CSV
datos_temp = [datos, tiempo]


while 1:
      time.sleep(5)
      with open("test.txt", "w") as file:
        file.write(str(datos_temp))
      f=open('dataFile.txt','a')
      # Mostramos el valor leido y eliminamos el salto de linea del final
      print ("Lectura DHT11: ", datos)
