""" 
Realizar un programa que lea los lados de n triángulos, e informar:
 a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales),
isósceles (dos lados iguales), o escaleno (ningún lado igual)
 b) Cantidad de triángulos de cada tipo.
"""

cant_equ=0
cant_iso=0
cant_esc=0
n= int(input('Ingrese la cantidad que ingresará'))

for i in range(n):
    lado1 = int(input('Ingrese la medida del lado 1: '))
    lado2 = int(input('Ingrese la medida del lado 2: '))
    lado3 = int(input('Ingrese la medida del lado 3: '))
    if lado1 == lado2 == lado3:
        print('Es un triángulo equilátero')
        cant_equ += 1
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Es un triángulo isóseles')
        cant_iso += 1
    elif lado1 != lado2 != lado3:
        print('Es un triángulo escaleno')
        cant_esc += 1

print(f'La cantidad de triángulos escalenos ingresados es de: {cant_esc}, de isóseles es de: {cant_iso} y de equilateros es de: {cant_equ}')