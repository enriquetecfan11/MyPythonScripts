# -*- coding: cp1252 -*-
#------------------------------------------------------------------------
#Programa...: Py202_notas.py
#Autor......: Enrique Rodriguez
#Descripción: Operando Ando
#------------------------------------------------------------------------
print("-------------------------------------")
print("Programa...: Py201_notas.py")
print("Autor......: Enrique Rodriguez")
print("--------------------------------------")

notas_idme = int(input("Dime la nota de IDME: "))
notas_mer = int(input("Dime la nota de MER: "))
notas_mev = int(input("Dime la nota de MEV: "))

lista_notas =[notas_idme, notas_mer, notas_mev]

#print("Suma de las notas = ",sum(lista_notas))
nota_media = sum(lista_notas) /3

print("La nota media de las 3 notas es:", nota_media)
print("La nota mas alta de todas es: ", max(lista_notas))
