# -*- coding: cp1252 -*-
#------------------------------------------------------------------------
#Programa...: Py104_resistencias.py
#Autor......: Enrique Rodriguez
#Descripción: Resistencias Serie Paralelo
#------------------------------------------------------------------------
print("-------------------------------------")
print("Programa...: Py104_reistencias.py")
print("Autor......: Enrique Rodriguez")
print("--------------------------------------")


r1   = int(input("Introduzca R1..: "))
r2   = int(input("Introduzca R2..: "))
r3   = int(input("Introduzca R3..: "))

paralelo = r1 + r2 + r3
serie    = (1/r1) + (1/r2) + (1/r3)

print("El paralelo de las resitencias es: " + str(paralelo))
print("El serie de las resitencias es: " + str(serie))
