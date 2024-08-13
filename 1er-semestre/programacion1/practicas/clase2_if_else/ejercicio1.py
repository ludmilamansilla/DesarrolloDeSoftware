num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))

if num1>num2:
    print(f'Suma: {num1}+{num2}={num1+num2}')
    print(f'Resta: {num1}-{num2}={num1-num2}')
else:
    print(f'Multiplicación: {num1}*{num2}={num1*num2}')
    print(f'División: {num1}/{num2}={num1/num2}')