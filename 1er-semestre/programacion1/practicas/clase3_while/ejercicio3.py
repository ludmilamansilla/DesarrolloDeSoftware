contador = 1
sum = 0

while contador <=10:
    num = int(input('Introduce un numero:'))
    sum += num
    contador += 1

promedio = sum / 10

print(f'La suma es de los números ingresados es de: {sum}')
print(f'El promedio es de: {promedio}')