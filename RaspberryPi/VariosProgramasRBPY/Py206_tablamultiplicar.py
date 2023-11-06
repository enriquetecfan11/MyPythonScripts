# -*- coding: cp1252 -*-
#------------------------------------------------------------------------
#Programa...: Py206_tablamultiplicar.py
#Autor......: Enrique Rodriguez
#Descripción: Operando Ando
#------------------------------------------------------------------------
print("------------------------------------------------")
print("     Programa...: Py206_tablamultiplicar.py")
print("        Autor......: Enrique Rodriguez")
print("-----------------------------------------------")

x = int(input("Igrese un numero del 1 al 10: "))

if x > 10:
    print("Numero Invalido")
    
if x <= 10:    
 r=range(x, x+1)
 for x in r:
    print (x, 2*x, 3*x, 4*x, 5*x, 6*x, 7*x, 8*x, 9*x, 10*x)

    
