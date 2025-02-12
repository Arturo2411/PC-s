##         PRACTICA NRO1
## ALUMNO:Arturo Manuel Baldarrago Huarhua

#4 

print("Hola mundo")

#5 

nombre=input("Introduce tu nombre: ")

print(f"Hola ,", nombre)

#6 

edad=int(input("Introduce tu edad: "))

if edad >=18:
    print(f"Usted tiene",edad,"años, es mayor de edad")
else:
    print(f"Usted tiene",edad,"años, es menor de edad")

#7 

numero=int(input("Introduce un número entero: "))
numero_residuo = numero % 2

if numero_residuo == 1:
    print(f"El numero",numero,", es impar")
else:
    print(f"El numero",numero,", es par")

#8 
numero_entero=int(input("Introduce un número entero cualquiera: "))
suma= (numero_entero/2)*(numero_entero + 1)

print(f"La suma de todos los numeros enteros existentes entre 1 y",numero_entero,"es",suma)