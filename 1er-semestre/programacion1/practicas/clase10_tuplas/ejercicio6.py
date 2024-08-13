""" 
Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada
elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
a) Cargar por teclado.
b) Listar los productos y precios.
c) Imprimir los productos con precios comprendidos entre 10 y 15. 
"""
def carga():
    productos = []
    for i in range(5):
        nombre = input('Introduce el nombre del producto: ')
        precio = int(input('Introduce el precio del producto: '))
        productos.append((nombre,precio))
    return productos

def imprimir(productos):
    print('Listado de productos y precios: ')
    for nombre, precio in productos:
        print(nombre, precio)

def entre10Y15(productos):
    print('Listado de productos y precios entre 10 y 15: ')
    for nombre, precio in productos:
        if precio>=10 and precio<=15:
            print(nombre, precio)

# Bloque principal

lista = carga()
imprimir(lista)
entre10Y15(lista)