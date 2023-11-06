# -*- coding: cp1252 -*-
#------------------------------------------------------------------------
#Programa...: Py205_llamada.py
#Autor......: Enrique Rodriguez
#Descripción: Operando Ando
#------------------------------------------------------------------------
print("-------------------------------------")
print("Programa...: Py205_llamada.py")
print("Autor......: Enrique Rodriguez")
print("--------------------------------------")

tiempo_llamada = float(input("¿Cuantos minutos dura la llamada? "))
tarifa = input("¿Que tarifa usas? ")

if tarifa == "plana":
    dinero = tiempo_llamada * 0.25
    print("Te cuesta la llamada", dinero)

if tarifa == "mini":
    dinero = (tiempo_llamada - 2) * 0.20
    print("Te cuesta la llamada", dinero)

if tarifa == "maxi":
    dinero = (tiempo_llamada - 5) * 0.15
    print("Te cuesta la llamada", dinero)






