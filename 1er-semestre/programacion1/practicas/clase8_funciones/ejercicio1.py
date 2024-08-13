""" 
Desarrollar un programa con dos funciones. La primer solicite el ingreso de
un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga
de dos valores y muestre el producto de los mismos. LLamar desde el bloque del
programa principal a ambas funciones. 
"""
result = 0

def cuadrado():
    num = int(input('Ingrese un número: '))
    result = num ** 2
    print(f'El cuadrado del número {num} es {result}')

result = 0
def multiplicación():
    num1 = int(input('Ingrese un número: '))
    num2 = int(input('Ingrese otro número: '))
    result = num1 * num2
    print(f'La multiplicación de {num1} * {num2} es {result}')

# bloque principal
cuadrado()
multiplicación()