""" 
Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor mayor de la lista
a la última posición.

La primera aproximación para llegar en el próximo problema al ordenamiento completo de una
lista tiene por objetivo analizar los intercambios de elementos dentro de la lista y dejar el mayor
en la última posición.

El algoritmo consiste en comparar si la primera componente es mayor a la segunda, en caso que
la condición sea verdadera, intercambiamos los contenidos de las componentes.
"""

sueldos = []

for i in range(5):
    valor = int(input('Ingrese sueldo: '))
    sueldos.append(valor)

for i in range(4):
    if sueldos[i] > sueldos[i+1]:
        aux = sueldos[i]
        sueldos[i] = sueldos[i+1]
        sueldos[i+1] = aux

print(f"Lista con el último elemento ordenado: {sueldos}") 

""" 
Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.
"""

sueldos = []

for i in range(5):
    valor = int(input('Ingrese sueldo:'))
    sueldos.append(valor)
    
for i in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux
            
for k in range(4):
 for x in range(4-k):
    if sueldos[x]>sueldos[x+1]:
        aux=sueldos[x]
        sueldos[x]=sueldos[x+1]
        sueldos[x+1]=aux

print(f'La lista ordenada de los sueldos es: {sueldos}')


""" 
Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas
respectivas. Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los
alumnos.
"""

alumnos = []
notas = []

for x in range(5):
    nom = input('Ingrese nombre del alumno: ')
    alumnos.append(nom)
    nota = int(input('Ingrese la nota de dicho alumno: '))
    notas.append(nota)


for i in range(4):
    for x in range(4-i):
        if notas[x]<notas[x+1]:
            aux1 = notas[x+1]
            notas[x+1] = notas[x]
            notas[x] = aux1
            aux2 = alumnos[x]
            alumnos[x] = alumnos[x+1]
            alumnos[x+1] = aux2

print("Lista de alumnos y sus notas ordenadas de mayor a menor")
for x in range(5):
    print(alumnos[x],notas[x])


""" 
Crear una lista por asignación. La lista tiene que tener cuatro elementos. Cada elemento debe
ser una lista de 3 enteros.
Imprimir sus elementos accediendo de diferentes modos.
"""

lista = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(lista[0])):
    print(lista[0][i]) 


for k in range(len(lista)):
 for x in range(len(lista[k])):
    print(lista[k][x])


""" 
Crear una lista por asignación. La lista tiene que tener 2 elementos. Cada elemento debe ser una
lista de 5 enteros.
Calcular y mostrar la suma de cada lista contenida en la lista principal.
"""

lista = [[1,2,3,4,5],[6,7,8,9,10]]

sum = 0
for i in range(len(lista[0])):
    sum += lista[0][i]

print(f'La suma de la primer lista es: {sum}')

sum = 0
for i in range(len(lista[1])):
    sum += lista[1][i]

print(f'La suma de la segunda lista es: {sum}') 


""" 
Crear una lista por asignación. La lista tiene que tener 5 elementos. Cada elemento debe ser una
lista, la primera lista tiene que tener un elemento, la segunda dos elementos, la tercera tres
elementos y así sucesivamente.
Sumar todos los valores de las listas.
"""

lista = [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]

suma=0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
        print(suma)


""" 
Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas,
almacenar las notas en una lista paralela. Cada componente de la lista paralela debe ser también
una lista con las dos notas. Imprimir luego cada nombre y sus dos notas
"""

alumnos = []
notas = []

for i in range(3):
    nombre = input('Ingrese nombre del alumno: ')
    alumnos.append(nombre)
    
    nota1 = int(input('Ingrese la primer nota del respectivo alumno: '))
    nota2 = int(input('Ingrese la segunda nota del respectivo alumno: '))
    notas.append([nota1,nota2])


for i in range(3):
    print(alumnos[i],notas[i][0],notas[i][1])


""" 
Se tiene que cargar la siguiente información:
· Nombres de 3 empleados
· Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
Confeccionar el programa para:
a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para
cada empleado.
c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado
"""

nombres = []
sueldos = []
total_sueldos = []

for i in range(3):
    nombre = input('Ingrese nombre del empleado: ')
    nombres.append(nombre)

    sueldo1 = int(input('Ingrese sueldo del empleado correspondiente: '))
    sueldo2 = int(input('Ingrese sueldo del empleado correspondiente: '))
    sueldo3 = int(input('Ingrese sueldo del empleado correspondiente: '))
    sueldos.append([sueldo1,sueldo2,sueldo3])

for i in range(3):
    total = sueldos[i][0] + sueldos[i][1] + sueldos[i][2]
    total_sueldos.append(total)

for i in range(3):
    print(nombres[i], total_sueldos[i])

mayor = total_sueldos[0]
p_mayor = 0
for i in range(1,3):
    if total_sueldos[i]>mayor:
        mayor = total_sueldos[i]
        p_mayor = i

print("Empleado con mayores ingresos en los ultimos tres meses")
print(nombres[p_mayor])
print("con un ingreso de",mayor)


""" 
Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que crearemos
en la lista. El segundo valor indica la cantidad de elementos que tendrá cada una de las listas
internas a la lista principal.
Mostrar la lista y la suma de todos sus elementos.
"""
 
lista = []

elementos = int(input('Cuantos elementos tendra la lista: '))
sub = int(input('Cuantos elementos tendran las listas internas: '))

for i in range(elementos):
    lista.append([])
    for x in range(sub):
        valor = int(input('Ingrese valor: '))
        lista[i].append(valor)

print(lista)

sum = 0
for i in range(len(lista)):
    for x in range(len(lista[i])):
        sum += lista[i][x]

print(f"La suma de todos sus elementos: {sum}")


""" 
Definir dos listas de 3 elementos.
La primer lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
La segunda lista está constituida por listas con los nombres de los hijos de cada familia. Puede
haber familias sin hijos.
Imprimir los nombres del padre, la madre y sus hijos.
También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.
"""

padres=[]
hijos=[]

for i in range(3):
    
    papa = input('introduce el nombre del padre: ')
    mama = input('introduce el nombre de la madre: ')
    padres.append([papa,mama])
    
    cant_hijos = int(input('¿Cuántos hijos tiene esa familia?'))
    hijos.append([])
    
    for x in range(cant_hijos):
        nombre = input('Ingrese nombre del hijo: ')
        hijos[i].append(nombre)

print("Listado del padre, madre y sus hijos")
for k in range(3):
    print("Padre:",padres[k][0])
    print("Madre:",padres[k][1])
    for x in range(len(hijos[k])):
        print("Hijo:",hijos[k][x])
        print("Listado del padre y cantidad de hijos que tiene")

for x in range(3):
    print("padre:",padres[x][0])
    print("Cantidad de hijos:",len(hijos[x]))


""" 
Crear una lista por asignación con 5 enteros. Eliminar el primero, el tercero y el último de la
lista.
"""

lista=[10, 20, 30, 40, 50]
print(lista)

lista.pop(0)
lista.pop(1)
lista.pop(2)
print(lista)


""" 
Crear una lista y almacenar 10 enteros pedidos por teclado. Eliminar todos los elementos que
sean iguales al número entero 5.
"""

lista = []

for i in range(10):
    num = int(input('Ingresar un número: '))
    if num != 5:
        lista.append(num)

print(lista) 

lista=[]
for x in range(10):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)
print(lista)

posicion=0
while posicion<len(lista):
    if lista[posicion]==5:
        lista.pop(posicion)
    else:
        posicion=posicion+1

print(lista)