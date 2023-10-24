# -*- coding: cp1252 -*-
#------------------------------------------------------------------------
#Programa...: Py1010_gps.py
#Autor......: Enrique Rodriguez
#Descripción: Operando Ando
#------------------------------------------------------------------------
print("-------------------------------------")
print("Programa...: Py1010_gps.py")
print("Autor......: Enrique Rodriguez")
print("--------------------------------------")

gps =["$GNRMC", "203544", "A, 0438.9198 N, 07404.3962 W", "1"]
print("La trama gps", gps)

#Seleccionamos los primeros caracteres de la cadena
gps1 = gps[0:1]
print ("Los caracteres de GGA son: " + str (gps1))

#Seleccionamos los segundos caracteres de la cadena
startLoc = 1 
endLoc = 2 
gps2 = gps[startLoc: endLoc] 
print ("Los caracteres que muestran la hora son: " + str (gps2)) 

#Seleccionamos los terceros caracteres de la cadena
startLoc1 = 2 
endLoc1 = 3
gps3 = gps[startLoc1:endLoc1]
print ("Los caracteres que muestran las cordenadas GPS son: " + str (gps3))

#Seleccionamos los cuartos caracteres de la cadena
startLoc2 = 3
endLoc2 = 4
gps4 = gps[startLoc2:endLoc2]
print ("La calidad del arreglo: " +str (gps4))
