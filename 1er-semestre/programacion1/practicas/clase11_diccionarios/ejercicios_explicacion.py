"""
En el bloque principal del programa definir un diccionario que almacene los nombres de paises
como clave y como valor la cantidad de habitantes. Implementar una función para mostrar cada
clave y valor.
"""

def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

# bloque principal
paises={"argentina":40000000, "españa":46000000, "brasil":190000000, "uruguay": 3400000}
imprimir(paises)

""" 
Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de
productos y como valor el precio del mismo.
Desarrollar además las funciones de:
1) Imprimir en forma completa el diccionario
2) Imprimir solo los artículos con precio superior a 100.
"""

def cargar():
    productos = {}
    for i in range(5):
        nombre = input('Ingrese el nombre del producto: ')
        precio = int(input('Ingrese el precio de dicho producto: '))
        productos[nombre] = precio
    return productos

def imprimir(productos):
    print('Listado de articulos: ')
    for producto in productos:
        print(producto, productos[producto])

def imprimir_mas_100(productos):
    print('Listado de articulos con precios mayores a 100: ')
    for producto in productos:
        if productos[producto]>100:
            print(producto)

# bloque principal
productos = cargar()
imprimir(productos)
imprimir_mas_100(productos) 


""" 
Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano. La clave es la
palabra en ingles y el valor es la palabra en castellano.
Crear las siguientes funciones:
1) Cargar el diccionario.
2) Listado completo del diccionario.
3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traducción. 
"""

def carga():
    diccionario = {}
    continuar = 'si'
    while continuar == 'si':
        castellano = input('Ingrese la palabra en castellano: ')
        ingles = input('Ingrese la palabra en inglés: ')
        diccionario[ingles] = castellano
        continuar = input('¿Deseas cargar otra palabra [si/no]?')
    return diccionario

def imprimir(diccionario):
    print('Listado completo del diccionario: ')
    for palabras in diccionario:
        print(palabras, diccionario[palabras])

def consultar(diccionario):
    palabra = input('Ingrese una palabra en inglés a consultar: ')
    if palabra in diccionario:
        print(f'En castellano significa: {diccionario[palabra]}')
    else:
        print('No se encuentra cargada la palabra que estás buscando')

# Bloque Principal

diccionario = carga()
imprimir(diccionario)
consultar(diccionario) 

""" 
Confeccionar un programa que permita cargar un código de producto como clave en un
diccionario. Guardar para dicha clave el nombre del producto, su precio y cantidad en stock.
Implementar las siguientes actividades:
1) Carga de datos en el diccionario.
2) Listado completo de productos.
3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.
4) Listado de todos los productos que tengan un stock con valor cero.
"""

def cargar():
    
    productos = {}
    continuar = "s"
    
    while continuar == "s":
        codigo = int(input('Ingrese el codigo del producto: '))
        descripcion = input('Ingrese la descripción')
        precio = float(input('Ingrese el precio: '))
        stock = int(input('Ingrese el stock actual: '))
        productos[codigo] = (descripcion, precio, stock)
        continuar = input('¿Desea cargar otro producto? [s/n]')
    
    return productos

def imprimir(productos):
    print('Listado de productos: ')
    for producto in productos:
        print(producto, productos[producto][0], productos[producto][1], productos[producto][2])

def consultar(productos):
    codigo = int(input('Ingrese le codigo del producto a consultar: '))
    if codigo in productos:
        print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])


def listado_stock0(productos):
    print('Listado de articulos con stock en cero: ')
    for codigo in productos:
        if productos[codigo][2] == 0:
            print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])

# bloque principal
productos = cargar()
imprimir(productos)
consultar(productos)
listado_stock0(productos)

""" 
Confeccionar una agenda. Utilizar un diccionario cuya clave sea la fecha. Permitir almacenar
distintas actividades para la misma fecha (se ingresa la hora y la actividad)
Implementar las siguientes funciones:
1) Carga de datos en la agenda.
2) Listado completo de la agenda.
3) Consulta de una fecha.
"""

def carga():
    agenda = {}
    continuar = 's'
    
    while continuar == 's':
        
        fecha = input('Ingrese la fecha con formato dd/mm/aa: ')
        
        continuar2 = 's'
        lista = []
        
        while continuar2 == 's':
            hora = input('Ingrese la hora con formato hh:mm: ')
            actividad = input('Ingrese la descipción de la actividad: ')
            lista.append((hora,actividad))
            continuar2 = input('¿Quieres ingresar otra actividad para la misma fecha? [s/n]: ')
        
        agenda[fecha] = lista
        continuar = input('¿Quieres ingresar otra fecha? [s/n]: ')
    
    return agenda

def imprimir(agenda):
    print('Listado completo de la agenda: ')
    for fecha in agenda:
        print(f'Para la fecha {fecha}')
        for hora, actividad in agenda[fecha]:
            print(hora, actividad)

def consultar(agenda):
    fecha = input('Ingrese la fecha que desea consultar: ')
    if fecha in agenda:
        for hora, actividad in agenda[fecha]:
            print(hora, actividad)
    else:
        print('No hay actividades agendadas para dicha fecha')


# BLoque principal
agenda = carga()
imprimir(agenda)
consultar(agenda)