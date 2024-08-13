""" 
Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos
mayores o iguales a 10 y generar una nueva lista con dichos valores. 
"""

lista = []

for i in range(5):
    num = int(input('Ingresar número: '))
    lista.append(num)
    
    i = 0
    while i < len(lista):
        if lista[0]>=10:
            lista.pop(i)
        else:
            i += 1

print(lista)