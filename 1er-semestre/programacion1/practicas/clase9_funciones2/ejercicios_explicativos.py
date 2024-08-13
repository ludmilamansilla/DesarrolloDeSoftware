""" 
Definir por asignación una lista de enteros en el bloque principal del programa. Elaborar tres
funciones, la primera recibe la lista y retorna la suma de todos sus elementos, la segunda recibe
la lista y retorna el mayor valor y la última recibe la lista y retorna el menor.
"""

def sumar(lista):
    sum = 0
    for i in range(len(lista)):
        sum += lista[i]
    return sum

def mayor(lista):
    may = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > may:
            may = lista[i]
    return may

def menor(lista):
    men = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < men:
            men = lista[i]
    return men

# bloque principal del programa
listavalores=[10, 56, 23, 120, 94]
print("La lista completa es")
print(listavalores)
print("La suma de todos su elementos es", sumar(listavalores))
print("El mayor valor de la lista es", mayor(listavalores))
print("El menor valor de la lista es", menor(listavalores))

""" 
Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros.
Implementar una función que imprima el mayor y el menor valor de la lista.
"""

def mayormenor(lista):
    
    may = lista[0]
    men = lista[0]
    
    for i in range(1, len(lista)):
        if lista[i] > may:
            may = lista[i]
        else:
            if lista[i] < men:
                men = lista[i]
    
    print(f'El valor mayor de la lista es: {may}')
    print(f'El valor menor de la lista es: {men}')

# bloque principal
lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)
mayormenor(lista)

""" 
Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una
segunda función debe recibir una lista y mostrar todos los valores mayores a 10. Desde el
bloque principal del programa llamar a ambas funciones.
"""

def cargar_lista():
    lista = []
    for i in range(5):
        n = int(input('Ingrese un número: '))
        lista.append(n)
    return lista

def may_10(li):
    for i in range(len(li)):
        if li[i] > 10:
            print(li[i])

# BLOQUE PRINCIPAL

lista = cargar_lista()
may_10(lista)


""" 
Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una
segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista. Desde el
bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la
lista.
"""

def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li

def retornar_mayormenor(li):
    ma=li[0]
    me=li[0]
    for x in range(1,len(li)):
        if li[x]>ma:
            ma=li[x]
        else:
            if li[x]<me:
                me=li[x]
    return [ma,me]

# bloque principal del programa
lista=carga_lista()
rango=retornar_mayormenor(lista)
print("Mayor elemento de la lista:",rango[0])
print("Menor elemento de la lista:",rango[1])


""" 
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas.
Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas
mayores de edad (mayores o iguales a 18 años)
Imprimir la edad promedio de las personas.
"""

def datos():
    name = []
    age = []
    for i in range(5):
        v1 = input('Ingrese el nombre de la persona: ')
        name.append(v1)
        v2 = int(input('Ingrese la edad correspondiente de la persona: '))
        age.append(v2)
    return [name, age]

def mayores(name, age):
    print('Nombre de las personas mayores de edad: ')
    for i in range(len(name)):
        if age[i]>=18:
            print(name[i])

def prom_ages(age):
    sum = 0
    for i in range(len(age)):
        sum += age[i]
    promedio = sum / 5
    print(f'El promedio de edad de las personas es de: {promedio}')

# BLOQUE PRINCIPAL

nombres, edades = datos()
mayores(nombres, edades)
prom_ages(edades)