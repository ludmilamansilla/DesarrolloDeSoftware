# Ludmila Mansilla, DNI: 44865030

cadena = ''

while cadena.lower() != "salir":
    cont = 0
    cadena = input('Ingrese la cadena de caracteres: ')
    
    if cadena.lower() == "salir":
        print("Saliendo del programa")
        break
    
    for i in range(len(cadena)):
        print(cadena[i])
        print(len(cadena))
        cont += 1
    
    print(f'La cantidad de letras es: {cont}')


""" 
En este ejercicio primero inicializo una variable con una cadena vacia.
Luego en un ciclo while pongo que mientras que la cadena sea distinto de la palabra salir, haga las siguientes instrucciones
creo un contador y lo incializo en 0
cambio el valor de la variable cadena por lo que escriba el usuario mediante el input.
con un if, si es que el usuario escribe salir, me salga del bucle, por eso el break.
Si la palabra que ingresa el usuario no es "salir", mediante el bucle for, me imprima letra por letra de la cadena ingresada y cuente cuantas letras tiene. 
"""