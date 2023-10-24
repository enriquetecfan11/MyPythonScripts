# -*- coding: cp1252 -*-
#------------------------------------------------------------------------
#Programa...: Py203_punto.py
#Autor......: Enrique Rodriguez
#Descripción: Operando Ando
#------------------------------------------------------------------------
print("-------------------------------------")
print("Programa...: Py203_punto.py")
print("Autor......: Enrique Rodriguez")
print("--------------------------------------")

print("¿Donde esta el punto P en el cuadrante?")
x1  = float(input("Coordenada punto P en x..: "))
y1  = float(input("Coordenada punto P en y..: "))

#Para el pimer cuadrante es positivo positivo
if (x1>1 and y1>1 ):
  print("El punto P esta en el primer cuadrante")

#Para el segundo cuadrante es negativo positivo
if (x1<0 and y1>0 ):
  print("El punto P esta en el segundo cuadrante")

#Para el tercer cuadrante es negativo negativo
if (x1<0 and y1<0 ):
  print("El punto P esta en el tercer cuadrante") 

#Para el tercer cuadrante es postivo negativo
if (x1>0 and y1<0 ):
  print("El punto P esta en el cuarto cuadrante")

print("Las cordenadas del punto P son", x1, "y", y1)
