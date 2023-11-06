##----------------------------------##
## Prueba de Puertos
## Enrique Rodriguez Julio 2K19
##----------------------------------##

import serial
import time
ser = serial.Serial("/dev/ttyUSB0", 9600)

time.sleep(0.5)

print(ser)
print("Puerto Cerrado")
ser.close()
print("Puerto Abierto")
ser.open()


time.sleep(0.5)

i = 1

while i <= 15:
    data = ser.readline()
    print(data)
    with open ("datafile.txt","a") as file:
        file.write(data)
        file.close()

time.sleep(0.5)
ser.close()
print("Puerto Serie Cerrado y datos recogidos")