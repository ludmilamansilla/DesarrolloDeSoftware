""" 
Confeccionar un programa que solicite la carga de 10 valores flotantes (con
parte decimal) por teclado. Mostrar al final su suma. Definir varias líneas de
comentarios indicando el nombre del programa, el programador y la fecha de la
última modificación. Utilizar el caracter # para los comentarios.
"""

# PROGRAMA: Cargar 10 números

# Programadora: Ludmila Mansilla
# Fecha de última modificación: 27/05/2024

sum = 0

for i in range(10):
    num = float(input('Ingrese un número: '))
    sum += num

print(f'La suma total es de: {sum}')