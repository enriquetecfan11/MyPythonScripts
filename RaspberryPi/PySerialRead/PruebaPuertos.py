##----------------------------------##
## Prueba de Puertos
## Enrique Rodriguez Julio 2K19
##----------------------------------##

# Ejecutar este linea de codigo en la termninal para poder usar el puerto
# sudo chmod a+rw /dev/ttyACM0

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
time.sleep(0.5)
print("Puerto Abierto")

time.sleep(0.5)

while True:
    data = ser.readline()

    print(data)
