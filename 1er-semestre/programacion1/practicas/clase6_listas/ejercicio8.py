""" 
Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se
repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones
en la lista) 
"""

lista = []

for i in range(5):
    num = int(input('Ingrese un valor: '))
    lista.append(num)

mayor = lista[0]

for i in range(5):
    if lista[i] > mayor:
        mayor = lista[i]

igual = lista[0]
iguales = 0

for i in range(5):
    if lista[i]==igual:
        iguales += 1

print(f'La lista es: {lista}')
print(f'El elemento mayor de la lista es: {mayor}')

if iguales == 1:
    print(f'Se repite {iguales} vez')
elif iguales > 1:
    print(f'Se repiten {iguales} veces')