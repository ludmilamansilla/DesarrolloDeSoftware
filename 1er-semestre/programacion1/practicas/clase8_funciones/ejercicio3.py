""" 
Desarrollar una funcion que reciba un string como parametro y nos muestre
la cantidad de vocales. Llamar a la función desde el bloque principal del
programa 3 veces con string distintos.
"""

def vocales(string):
    cant = 0
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
            cant += 1
    print(f'La cantidad de vocales de la palabra {string} es: {cant}')

vocales("hola")
vocales("cama")
vocales("camarero")

