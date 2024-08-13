# Ludmila Mansilla, DNI: 44865030

while True:
    num1 = int(input('Ingrese el número: '))
    num2 = int(input('Es divisible por: '))
    
    if num2==0:
        print('No es posible dividir por 0')
        break;
    
    if num1%num2==0:
        print("Si")
    else:
        print("No")


