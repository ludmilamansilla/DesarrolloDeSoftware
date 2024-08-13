""" 
Confeccionar un programa que lea n pares de datos, cada par de datos
corresponde a la medida de la base y la altura de un triángulo. El programa deberá
informar:
 a) De cada triángulo la medida de su base, su altura y su superficie.
 b) La cantidad de triángulos cuya superficie es mayor a 12 (la superficie se
 calcula multiplicando la base por la altura y a este valor dividiendolo en 2)
"""
n = int(input('Cuantos valores ingresará:'))
cantidad = 0

for i in range(n):
    b = int(input('Ingrese la base del triángulo:'))
    h = int(input('Ingrese la altura del triángulo:'))
    superficie = b*h/2
    print(f'La medida de la base es {b} y su superficie es {superficie}')
    if superficie > 12:
        cantidad += 1

print(f'La cantidad de triángulos con superficie mayores a 12 es de: {cantidad}')