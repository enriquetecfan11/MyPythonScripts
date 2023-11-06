#Prueba de lista en txt
#Enrique Rodriguez Vela
#Novimebre de 2018
#Version 0.2

#Conventir bytes a string
data = (int(input("Escribe un dato de temperatura: ")))
#print(data)

#Ver Fecha y hora de los datos
import time
#print("Fecha y hora" + time.strftime("%c") +'\n')

#Crea la lista de datos
datos = [data, time.strftime("%c")]

#Abrimos un archivo de lectura.txt
f=open('DATOS.txt','a')

# Bucle infinito para leer todos los datos
while 1:
    f.write(str(datos) + '\n')
    time.sleep(0.02)
    f.close()
    f=open('dataFile.txt','a')

