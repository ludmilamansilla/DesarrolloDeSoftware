""" 
Para crear una lista por asignación debemos indicar sus elementos encerrados entre corchetes y
separados por coma.

lista1=[10, 5, 3] # lista de enteros
lista2=[1.78, 2.66, 1.55, 89,4] # lista de valores float
lista3=["lunes", "martes", "miercoles"] # lista de string
lista4=["juan", 45, 1.92] # lista con elementos de distinto tipo
"""

""" 
Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.
"""

lista = [1,2,3,4,5]
sum = 0
x = 0

while x < len(lista):
    sum += lista[x]
    x += 1 

print('Los elementos son:', lista)
print('La suma es:', sum)


""" 
Definir una lista por asignación que almacene los nombres de los primeros cuatro meses de año.
Mostrar el primer y último elemento de la lista solamente.
"""

meses = ["enero", "febrero", "marzo", "abril"]

print(meses[0], meses[-1])


""" 
Definir una lista por asignación que almacene en la primer componente el nombre de un alumno y en las
dos siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas.
"""

lista = ["Ludmila", 8, 7]

promedio = (lista[-1] + lista[-2]) / 2

print(f'El promedio de {lista[0]} es: {promedio}')

""" 
Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista.
Imprimir la lista generada.
"""

lista = []

for i in range(5):
    num = int(input('Ingrese un número para guardar en su lista: '))
    lista.append(num)

print(f'La lista creada es: {lista}')

""" 
Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de
enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.
"""

lista = []
num = int(input('Ingrese valor (0 para finalizar): '))

while num!=0:
    lista.append(num)
    num = int(input('Ingrese valor (0 para finalizar): '))

print(f'La lista formada es: {lista}')

""" 
Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor
de la lista.
"""

lista = []

for i in range(5):
    num = int(input('Ingrese un valor: '))
    lista.append(num)

mayor = lista[0]

for i in range(5):
    if lista[i]>mayor:
        mayor = lista[i]

print(f'La lista es: {lista}')
print(f'El elemento mas grande de la lista es: {mayor}')

""" 
Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el
menor valor de la lista y la posición donde se encuentra.
"""

lista = []

for i in range(5):
    num = int(input('Ingrese un valor: '))
    lista.append(num)

menor = lista[0]

for i in range(5):
    if lista[i]<menor:
        menor = lista[i]
        posicion = i

print(f'La lista es: {lista}')
print(f'El elemento mas chico de la lista es: {menor} y se encuentra en la posición: {posicion}')

""" 
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas.
Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas
mayores de edad (mayores o iguales a 18 años)
"""

nombres = []
edades = []

for i in range(5):
    nombre = input('Ingrese el nombre de la persona: ')
    nombres.append(nombre)
    edad = int(input('Ingrese la edad de dicha persona: '))
    edades.append(edad)

mayores = []

for i in range(5):
    if edades[i]>= 18:
        mayores.append(nombres[i])


print(f'Los nombres son: {nombres}')
print(f'Las edades correspondientes son: {edades}')
print(f'Los mayores de edad son: {mayores}')