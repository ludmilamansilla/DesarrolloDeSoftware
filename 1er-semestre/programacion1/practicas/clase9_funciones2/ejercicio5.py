""" 
Desarrollar una aplicación que permita ingresar por teclado los nombres de 5
artículos y sus precios.
 Definir las siguientes funciones:
 a) Cargar los nombres de articulos y sus precios.
 b) Imprimir los nombres y precios.
 c) Imprimir el nombre de artículo con un precio mayor
 d) Ingresar por teclado un importe y luego mostrar todos los artículos con un
precio menor igual al valor ingresado.
"""

def cargar():
    
    articulo = []
    precio = []
    
    for i in range(5):
        v1 = input('Ingrese el nombre del artículo: ')
        articulo.append(v1)
        v2 = int(input('Ingrese el precio de dicho artículo: '))
        precio.append(v2)
    
    return [articulo,precio]

def mayor(articulo, precio):
    may = precio[0]
    art = 0
    for i in range(1, len(precio)):
        if precio[i]>may:
            may = precio[i]
            art = i
    print(f"Articulo con un precio mayor es : {articulo[art]} su precio es: {may}")

def buscar_precio(articulo, precio):
    valor = int(input("Ingrese un importe para mostrar los articulos con un precio menor:"))
    for i in range(len(precio)):
        if precio[i]< valor:
            print(articulo[i], precio[i])


# BLOQUE PRINCIPAL

articulos,precios = cargar()
print(articulos,precios)
mayor(articulos,precios)
buscar_precio(articulos,precios)