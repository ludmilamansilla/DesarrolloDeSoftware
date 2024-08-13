""" 
Elaborar una función que reciba tres enteros y nos retorne el valor promedio
de los mismos.
"""

def promedio3(a,b,c):
    promedio = (a+b+c) / 3
    return promedio

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))

print(f'El valor promedio de los tres números ingresados es de: {promedio3(num1,num2,num3)}')