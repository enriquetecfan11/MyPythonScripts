##----------------------------------##
## Prueba de Serial Correcto
## Enrique Rodriguez Septiembre 2K19
##----------------------------------##

import serial
ser = serial.Serial('/dev/ttyACM0')  # open serial port
print(ser.name)         # check which port was really used