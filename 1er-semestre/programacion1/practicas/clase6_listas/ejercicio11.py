""" 
Realizar un programa que pida la carga de dos listas numéricas enteras de 4
elementos cada una. Generar una tercer lista que surja de la suma de los
elementos de la misma posición de cada lista. Mostrar esta tercer lista. 
"""

lista1 = []
lista2 = []

for i in range(4):
    nums1 = int(input('Ingrese un número: '))
    lista1.append(nums1)
    nums2 = int(input('Ingrese otro número: '))
    lista2.append(nums2)

suma_listas = []

for i in range(4):
    suma_listas.append(lista1[i] + lista2[i])

print(f'La suma de los elementos paralelos de las 2 listas son: {suma_listas}')