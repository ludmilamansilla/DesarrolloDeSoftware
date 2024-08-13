""" 
Confeccionar una función que reciba tres enteros y los muestre ordenados de
menor a mayor. En otra función solicitar la carga de 3 enteros por teclado y
proceder a llamar a la primer función definida.
"""

def ordenar3(a,b,c):
    if a<b and a<c:
        if b < c:
            print(f'Los números ordenados de menor a mayor: {a,b,c}')
        else:
            print(f'Los números ordenados de menor a mayor: {a,c,b}')
    elif b<a and b<c:
        if a<c:
            print(f'Los números ordenados de menor a mayor: {b,a,c}')
        else:
            print(f'Los números ordenados de menor a mayor: {b,c,a}')
    elif c<a and c<b:
        if a<b:
            print(f'Los números ordenados de menor a mayor: {c,a,b}')
        else:
            print(f'Los números ordenados de menor a mayor: {c,b,a}')

def carga():
    num1 = int(input('Ingrese el primer número: '))
    num2 = int(input('Ingrese el segundo número: '))
    num3 = int(input('Ingrese el tercer número: '))
    ordenar3(num1,num2,num3)

carga()