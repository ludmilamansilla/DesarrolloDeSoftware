""" 
Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha función
(sin utilizar una estructura repetitiva)
"""

def menor_de_3 ():
    num1 = int(input('Ingrese el primer número: '))
    num2 = int(input('Ingrese el segundo número: '))
    num3 = int(input('Ingrese el tercer número: '))
    
    if num1<num2 and num1<num3:
        print(f'El número {num1} es el menor de los ingresados')
    elif  num2<num1 and num2<num3:
        print(f'El número {num2} es el menor de los ingresados')
    else:
        print(f'El número {num3} es el menor de los ingresados')

menor_de_3()