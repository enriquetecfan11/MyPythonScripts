#------------------------------------------------------------------------
#Programa...:Py103_salario.py
#Autor......:Enrique Rodriguez      
#Descripción: Calcula el salario
#------------------------------------------------------------------------

print("-------------------------------------")
print("Programa...: Py103_Salario.py")
print("Autor......: Enrique Rodriguez")
print("--------------------------------------")

horas = int(input("Horas trabajadas: "))
importe = int(input("Importe por horas: "))
impuestos = int(input("Impuestos: "))

print("****------****----****")


bruto = horas * importe
retencion = bruto*(impuestos/100)
neto = bruto - retencion

print("Importe Bruto: " +str(bruto))
print("Retencion Impuestos: " +str(retencion))
print("Importe Neto: " +str(neto))

