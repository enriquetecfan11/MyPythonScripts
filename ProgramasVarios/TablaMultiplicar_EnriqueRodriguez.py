#------------------------------------------------------------------------
#Programa...: PyExamen_tablamultiplicar.py
#Autor......: Enrique Rodriguez
#------------------------------------------------------------------------
print("------------------------------------------------")
print("     Programa...: PyExamen_tablamultiplicar.py")
print("        Autor......: Enrique Rodriguez")
print("-----------------------------------------------")

x = int(input("Igrese un numero del 1 al 10: "))

if x > 10:
    print("Numero Invalido")
    
if x <= 10:    
 print("Tabla del Numero: "+ str(x))
 r=range(x, x+1)
 for x in r:
   print("Numero "+ str(x) + " x 1: ")
   print(1*x)
   print("Numero "+ str(x) + " x 2: ")
   print(2*x)
   print("Numero "+ str(x) + " x 3:  ")
   print(3*x)
   print("Numero "+ str(x) + " x 4:  ")
   print(4*x)
   print("Numero "+ str(x) + " x 5:  ")
   print(5*x)
   print("Numero "+ str(x) + " x 6:  ")
   print(6*x)
   print("Numero "+ str(x) + " x 7:  ")
   print(7*x)
   print("Numero "+ str(x) + " x 8:  ")
   print(8*x)
   print("Numero "+ str(x) + " x 9:  ")
   print(9*x)
   print("Numero "+ str(x) + " x 10: ")
   print(10*x)
