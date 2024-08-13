num = int(input('Ingrese un número entero de hasta 3 cifras: '))

if num<10:
    print('El número es de 1 dígito')
elif num<100:
    print('El número es de 2 dígitos')
elif num<1000:
    print('El número es de 3 dígitos')
else:
    print('Erorr, no cumplis con las condiciones del número solicitado')