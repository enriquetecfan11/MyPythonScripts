# -*- coding: cp1252 -*-
#------------------------------------------------------------------------
#Programa...: Py108_grados.py
#Autor......: Enrique Rodriguez
#Descripci�n: Operando Ando
#------------------------------------------------------------------------
print("-------------------------------------")
print("Programa...: Py108_grados.py")
print("Autor......: Enrique Rodriguez")
print("--------------------------------------")

temp  = int(input("Introduzca la temperatura en grados: "))
print(str(temp) + '�C')
kelvin = (temp+273.15)
faren  = (kelvin*1.8 -459.67)

print("Los grados en Kelvin: " +str(kelvin))
print("Los grados en Farenhait " +str(faren))
