""" 
Definir una función que cargue una lista con palabras y la retorne.
Luego otra función tiene que mostrar todas las palabras de la lista que tienen más
de 5 caracteres. 
"""

def carga():
    lista = []
    n = int(input('¿Cuántas palabras cargaras?'))
    
    for i in range(n):
        palabra = input('Ingrese la palabra: ')
        lista.append(palabra)
    
    return lista

def mas5(lista):
    print('Estas son las palabras que tienen mas de 5 caracteres: ')
    for palabra in lista:
        if len(palabra)>5:
            print(palabra)

# Bloque principal

lista = carga()
mas5(lista) 