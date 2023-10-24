##----------------------------------##
## Prueba de serial Python
## Enrique Rodriguez Julio 2K19
##----------------------------------##


#Abrimos un archivo de lectura.txt
f=open('datafile.txt', "a")
f.write("Hola esto una prueba")
f.write("      ")
f.write("Hola esto una prueba")
f.close()

s = open("datafile.txt").read()
s = s.replace("      ", "\n")
f=open('datafile.txt', "w")
f.write(s)
f.close