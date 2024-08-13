""" 
Desarrollar un programa que solicite la carga de 10 números e imprima la
suma de los últimos 5 valores ingresados.
"""

sum = 0

for i in range(10):
    num = int(input('Ingrese un valor: '))
    if i>=5:
        sum += num

print(f'La suma de los ultimos 5 números es de: {sum}')