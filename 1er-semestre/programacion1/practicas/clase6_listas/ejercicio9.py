""" 
Crear y cargar dos listas con los nombres de 5 productos en una y sus
respectivos precios en otra. Definir dos listas paralelas. Mostrar cuantos
productos tienen un precio mayor al primer producto ingresado. 
"""

productos = []
precios = []

for i in range(5):
    producto = input('Ingrese el producto: ')
    productos.append(producto)
    precio = int(input('Ingrese el precio correspondiente al producto: '))
    precios.append(precio)

mayor_al_primero = precios[0]
cont = 0

for i in range(5):
    if precios[i] > mayor_al_primero:
        cont += 1

print(f'Los productos mayores al precio del primer producto ingresado son: {cont}')