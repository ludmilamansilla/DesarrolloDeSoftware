""" 
Definir por asignación una lista con 8 elementos enteros. Contar cuantos de
dichos valores almacenan un valor superior a 100. 
"""

lista = [1,2,3,4,5,6,7,8]
x=0
cont=0

while x < len(lista):
    if lista[x] > 100:
        cont += 1
    x += 1

print(f'Los valores mayores a 100 en la lista son: {cont}')