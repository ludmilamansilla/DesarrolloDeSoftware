""" 
Confeccionar un programa con las siguientes funciones:
a) Cargar una lista de 5 enteros.
b) Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor. 
"""

def cargar_lista():
    list = []
    for i in range(5):
        n = int(input('Ingresa un entero: '))
        list.append(n)
    return list

def mayMen(lista):
    
    men = lista[0] 
    may = lista[0]
    
    for i in range(len(lista)):
        if lista[i]>may:
            may = lista[i]
        elif lista[i]<men:
            men = lista[i]
    
    return (may,men)

# bloque principal

lista = cargar_lista()
mayor, menor = mayMen(lista)
print('el mayor elemento de la lista de enteros es: ', mayor)
print('el menor elemento de la lista de enteros es: ', menor)