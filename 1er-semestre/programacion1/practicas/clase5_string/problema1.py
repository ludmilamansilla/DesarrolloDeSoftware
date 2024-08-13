""" 
Realizar la carga de dos nombres de personas distintos. Mostrar por pantalla
luego ordenados en forma alfabética. 
"""

name1 = input("Ingrese el primer nombre: ")
name2 = input("Ingrese el segundo nombre: ")

if name1 > name2:
    print(f'Ordenados alfabéticamente: {name1}, {name2}.')
else:
    print(f'Ordenados alfabéticamente: {name2}, {name1}.')


