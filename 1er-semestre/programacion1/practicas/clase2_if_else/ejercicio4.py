num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))

if num1>num2 and num1>num3:
    print(f'{num1} es el mayor de los 3')
elif num2>num1 and num2>num3:
    print(f'{num2} es el mayor de los 3')
else:
    print(f'{num3} es el mayor de los 3')

# -------------------------------------------------

if num1>num2:
    if num1>num3:
        print(f'{num1} es el mayor de los 3')
    else:
        print(f'{num3} es el mayor de los 3')
else:
    if num2>num3:
        print(f'{num2} es el mayor de los 3')
    else:
        print(f'{num3} es el mayor de los 3')