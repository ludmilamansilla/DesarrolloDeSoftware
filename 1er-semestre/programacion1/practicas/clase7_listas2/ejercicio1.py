""" 
Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente
la lista e imprimirla.
"""

paises = []

for i in range(5):
    pais = input('Ingrese un país: ')
    paises.append(pais)

for x in range(5):
    for i in range(4-x):
        if paises[i]>paises[i+1]:
            aux = paises[i]
            paises[i] = paises[i+1]
            paises[i+1] = aux

print(f'La lista ordenada de los paises es: {paises}')