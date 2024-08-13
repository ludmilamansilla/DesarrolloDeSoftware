""" 
Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se
ingresaron. Tener en cuenta que un espacio en blanco es igual a " ", en cambio
una cadena vacía es ""
"""

oracion = "Mi nombre es Ludmila"
x = 0
cont = 0

while x < len(oracion):
    if oracion[x]==" ":
        cont += 1
    x += 1

print(f'La oracion tiene {cont} espacio/s')