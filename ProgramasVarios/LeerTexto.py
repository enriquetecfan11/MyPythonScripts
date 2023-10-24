#Leer archivo TXT
#Enrique Rodriguez Vela
#Novimebre de 2018
#Version 0.2


f = open ('DATOS.txt','r')
mensaje = f.read()
print(mensaje)
f.close()