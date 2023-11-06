# -*- coding: cp1252 -*-
#------------------------------------------------------------------------
#Programa...: Py204_renta.py
#Autor......: Enrique Rodriguez
#Descripción: Operando Ando
#------------------------------------------------------------------------
print("-------------------------------------")
print("Programa...: Py204_renta.py")
print("Autor......: Enrique Rodriguez")
print("--------------------------------------")

print("¿Cual es tu salario bruto? ")
x1  = int(input("Introduce el salario(sin separador de miles): "))

#Para el pimer cuadrante es positivo positivo
if (x1>0 and x1<=12000 ):
  print("Se te aplica el 0% en el IRPF")
  print ("El neto a percibir es: ", x1)

elif (x1>12000 and x1<=20000 ):
  print("Se te aplica el 20% en el IRPF:")
  print ("El neto a percibir es: ", x1 - (x1 * 0.2))

elif (x1>20000 and x1<=50000 ):
  print("Se te aplica el 25% en el IRPF")
  print ("El neto a percibir es: ", x1 - (x1 * 0.25))

elif(x1>50000):
  print("Se te aplica el 3% en el IRPF")
  print ("El neto a percibir es: ", x1 - (x1 * 0.03))


