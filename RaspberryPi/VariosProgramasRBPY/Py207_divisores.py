# -*- coding: cp1252 -*-
#------------------------------------------------------------------------
#Programa...: Py207_divisores.py
#Autor......: Enrique Rodriguez
#Descripci�n: Operando Ando
#------------------------------------------------------------------------
print("------------------------------------------------")
print("     Programa...: Py207_divisores.py")
print("        Autor......: Enrique Rodriguez")
print("-----------------------------------------------")


numero = int(input("Ingresa un numero menor que 100: "))

divisor = 0


if numero >= 100:
 print("Divisores:")
 if numero % 2 == 0:
    iterar = numero / 2
 else:
    iterar = (numero - 1) / 2
 for i in range(1, int(iterar) + 1):
    if numero % i == 0:
        aux = numero / i
        if aux != divisor:
            divisor = aux
        if i == iterar:
            print(int(divisor), end = "")
        else:
            print("%d," % (divisor), end = "")
