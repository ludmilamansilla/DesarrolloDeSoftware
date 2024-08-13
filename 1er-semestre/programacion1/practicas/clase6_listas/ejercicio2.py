""" 
Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los
elementos con valor iguales o superiores a 7. 
"""

lista = [1,587,21,65,45]
x = 0

while x<len(lista):
    if lista[x]>=7:
        print(lista[x])
    x += 1