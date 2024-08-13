""" 
Definir varias tuplas e imprimir sus elementos.
"""

tupla = (1, 2, 3)
fecha = (25, "Diciembre", 2016)
punto = (10, 2)
persona = ("Rodriguez", "Pablo", 43)

print(tupla)
print(fecha)
print(punto)
print(persona)

""" 
Desarrollar una función que solicite la carga del dia, mes y año y almacene dichos datos en una
tupla que luego debe retornar. La segunda función a implementar debe recibir una tupla con la
fecha y mostrarla por pantalla.
"""

def cargar_fecha():
    dd=int(input("Ingrese numero de dia:"))
    mm=int(input("Ingrese numero de mes:"))
    aa=int(input("Ingrese numero de año:"))
    return (dd,mm,aa)

def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")

# bloque principal
fecha = cargar_fecha()
imprimir_fecha(fecha)

""" 
Definir una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista.
Modificar la lista y luego convertir la lista en tupla.
"""

fechatupla1 = (25, 12, 2016)
print("Imprimimos la primer tupla")
print(fechatupla1)

fechalista = list(fechatupla1)
print("Imprimimos la lista que se le copio la tupla anterior")
print(fechalista)

fechalista[0] = 31
print("Imprimimos la lista ya modificada")
print(fechalista)

fechatupla2 = tuple(fechalista)
print("Imprimimos la segunda tupla que se le copio la lista")
print(fechatupla2)

""" 
Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais y la cantidad de
habitantes.
Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y en la tercera
mostrar el nombre del país con mayor cantidad de habitantes.
"""

def cargar_paisespoblacion():
    paises=[]
    for x in range(2):
        nom=input("Ingresar el nombre del pais:")
        cant=int(input("Ingrese la cantidad de habitantes:"))
        paises.append((nom,cant))
    return paises

def imprimir(paises):
    print("Paises y su poblacion")
    for x in range(len(paises)):
        print(paises[x][0],paises[x][1])

def pais_maspoblacion(paises):
    pos = 0
    for x in range(1,len(paises)):
        if paises[x][1] > paises[pos][1]:
            pos = x
    print("Pais con mayor cantidad de habitantes:",paises[pos][0])
    
# bloque principal
paises=cargar_paisespoblacion()
imprimir(paises)
pais_maspoblacion(paises)

""" 
Confeccionar un programa que permita la carga de una lista de 5 enteros por teclado.
Luego en otras funciones:
1) Imprimirla en forma completa.
2) Obtener y mostrar el mayor.
3) Mostrar la suma de todas sus componentes.
Utilizar la nueva sintaxis de for vista en este concepto.
"""

def cargar():
    lista=[]
    for x in range(5):
        num=int(input("Ingrese un valor:"))
        lista.append(num)
    return lista

def imprimir(lista):
    print("Lista completa")
    for elemento in lista:
        print(elemento)

def mayor(lista):
    may = lista[0]
    for elemento in lista:
        if elemento > may:
            may = elemento
    print("El elemento mayor de la lista es",may) 

def sumar_elementos(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    print("La suma de todos sus elementos es",suma)

# bloque principal

lista = cargar()
imprimir(lista)
mayor(lista)
sumar_elementos(lista)

""" 
Almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.
Implementar las funciones:
1) Carga de empleados.
2) Impresión de los empleados y sus sueldos.
3) Nombre del empleado con sueldo mayor.
4) Cantidad de empleados con sueldo menor a 1000
"""

def cargar():
    empleados=[]
    for x in range(5):
        nombre=input("Nombre del empleado:")
        sueldo=int(input("Ingrese el sueldo:"))
        empleados.append((nombre,sueldo))
    return empleados

def imprimir(empleados):
    print("Listado de los nombres de empleados y sus sueldos")
    for nombre,sueldo in empleados:
        print(nombre,sueldo)

def mayor_sueldo(empleados):
    empleado = empleados[0]
    for emp in empleados:
        if emp[1]>empleado[1]:
            empleado = emp
    print("Empleado con mayor sueldo:",empleado[0],"su sueldo es",empleado[1])

def sueldos_menor1000(empleados):
    cant=0
    for empleado in empleados:
        if empleado[1]<1000:
            cant=cant+1
    print("Cantidad de empleados con un sueldo menor a 1000 son:",cant)

# bloque principal
empleados=cargar()
imprimir(empleados)
mayor_sueldo(empleados)
sueldos_menor1000(empleados)
