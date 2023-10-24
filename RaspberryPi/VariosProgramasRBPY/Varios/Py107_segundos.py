# -*- coding: cp1252 -*-
#------------------------------------------------------------------------
#Programa...: Py107_segundos.py
#Autor......: Enrique Rodriguez
#Descripción: Operando Ando
#------------------------------------------------------------------------
print("-------------------------------------")
print("Programa...: Py107_segundos.py")
print("Autor......: Enrique Rodriguez")
print("--------------------------------------")

segundos  = int(input("Introduzca los segundos: "))

float minutos  = (segundos /60)
float horas = (minutos / 60)

print("Son tantos minutos: "+str(minutos))
print("Son tantas horas: "+str(horas))
