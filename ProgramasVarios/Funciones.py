def nombre():
    nombre = str(input("Introduzca tu nombre: "))
    return nombre

def apellido():
    apellido = str(input("Introduza tu apellidos: "))
    return apellido

name = nombre()

surname = apellido()

print("Hola " +str(name) + " " +str(surname))

def edad():
    
    edad = int(input("Introduzca tu edad: "))
    
    if edad > 18:
        print("Eres mayor de edad")
    else:
        print("No eres mayor de edad")
    
    return edad


age = edad()


def remplazar():
    string = 'Tutorial Gateway Provides Python Programming Tutorial'
 
    x = string.replace('t', 'X')
    
    print(x)
    
    return remplazar

replace = remplazar()

print("String reemplazada: " +str(replace))
    


