""" 
Elaborar una función que nos retorne el perímetro de un cuadrado pasando
como parámetros el valor de un lado.
"""

def calc_perimetro(l):
    perimetro = l * 4
    return perimetro

lado = int(input('Ingrese el valor del lado para calcular el perimetro: '))
print(f'El perimetro del cuadrado es: {calc_perimetro(lado)}')
