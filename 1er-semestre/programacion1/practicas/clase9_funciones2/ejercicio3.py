""" 
Definir una lista de enteros por asignación en el bloque principal. Llamar a
una función que reciba la lista y nos retorne el producto de todos sus elementos.
Mostrar dicho producto en el bloque principal de nuestro programa.
"""

def multi(lista):
    mult = lista[0]
    for i in range(1, len(lista)):
        mult = (lista[i]*mult)
    return mult

# BLOQUE PRINCIPAL

lista = [1,2,1,2,1,2]
print('La multiplicación de cada elemento de la lista es:', multi(lista))