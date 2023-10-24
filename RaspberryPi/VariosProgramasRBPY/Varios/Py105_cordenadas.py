# -*- coding: cp1252 -*-
#------------------------------------------------------------------------
#Programa...: Py105_cordenadas.py
#Autor......: Enrique Rodriguez
#Descripción: Operando Ando
#------------------------------------------------------------------------
print("-------------------------------------")
print("Programa...: Py105_cordenadas.py")
print("Autor......: Enrique Rodriguez")
print("--------------------------------------")

import math

x1  = float(input("Introduzca X1..: "))
y1  = float(input("Introduzca Y1..: "))
x2  = float(input("Introduzca X2..: "))
y2  = float(input("Introduzca Y2..: "))

mediox = (x1+x2)/2
medioy = (y1+y2)/2
distancia = (math.sqrt((x2-x1)**2+(y2-y1)**2))

print("Punto Medio: " +str(mediox)+"," +str(medioy))
print("Distancia entre ellos: " +str(distancia))
