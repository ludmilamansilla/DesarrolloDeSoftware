""" 
Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras 'a' o 'A'.
"""

def cant_a (palabra):
    cant = 0
    for i in range(len(palabra)):
        if palabra[i] == 'a' or palabra[i] == 'A':
            cant += 1
    return cant

palabra = input('Ingrese una palabra: ')
print(f'La cantidad de letras "a/A" que hay es: {cant_a(palabra)}')