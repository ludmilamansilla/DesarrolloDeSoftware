""" 
Crear una lista de enteros por asignación. Definir una función que reciba una
lista de enteros y un segundo parámetro de tipo entero. Dentro de la función
mostrar cada elemento de la lista multiplicado por el valor entero enviado. 
"""

def multiplicar(lista, n):
    for i in range(len(lista)):
        print(lista[i]*n)

# BLOQUE PRINCIPAL

lista = [7,2,7,5,2,1,1]
print(f'Lista original: {lista}')
print(f'Lista multiplicada cada elemento por 3: ')
multiplicar(lista,3)