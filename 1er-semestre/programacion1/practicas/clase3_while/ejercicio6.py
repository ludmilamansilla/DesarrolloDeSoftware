""" 
Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura
promedio de las personas.
"""

personas = int(input('Ingrese cuantas personas hay: '))
cont = 1
sum = 0

while cont<=personas:
    altura = float(input('Ingrese la altura: '))
    sum += altura
    cont += 1

promedio = sum / personas

print(f'El promedio de altura es de: {promedio}')