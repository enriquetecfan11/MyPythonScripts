##----------------------------------##
## Prueba de serial Python
## Enrique Rodriguez Julio 2K19
##----------------------------------##

##
print("Empieza el programa.")

#Importamos la libreria serial
import serial
import time

#Leemos el puerto donde esta enchufado nuestro dispositivo
ser = serial.Serial('/dev/ttyACM0', 9600 )

#Reseteamos el puerto

print("Puerto Cerrado")
ser.close()
print("Puerto Abierto")
ser.open()

#Bucle para hacer la lectura de los datos
i = 1

while i <= 100:
    i += 1
    #print(i)
    data = ser.readline().decode("utf-8")
    print(data)

    #Abrimos un archivo de lectura.txt para ecribir los datos
    f=open('datafile.txt', "a")

    f.write(data)

    f.close()

time.sleep(5)
ser.close()
print("Datos recogidos")
