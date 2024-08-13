""" 
Desarrollar un programa que permita cargar n números enteros y luego nos
informe cuántos valores fueron pares y cuántos impares.

Emplear el operador “%” en la condición de la estructura condicional (este
operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1): 
if valor%2==0:
"""

cont = 1
num_par = 0
num_impar = 0

nums = int(input('¿Cuántos valores son?: '))

while cont <= nums:
    num = int(input('Ingrese un número: '))
    if num%2==0:
        num_par += 1
    else:
        num_impar += 1
    cont += 1

print(f'La cantidad de números pares ingresados son {num_par}, y la cantidad de números impares son {num_impar}')