""" 
Ingresar una oración que pueden tener letras tanto en mayúsculas como
minúsculas. Contar la cantidad de vocales. Crear un segundo string con toda la
oración en minúsculas para que sea más fácil disponer la condición que verifica
que es una vocal. 
"""

oracion = input('Ingrese una oracion: ')
oracion_redu = oracion.lower()
cant = 0
x = 0

while x < len(oracion):
    if oracion[x] == "a" or oracion[x] == "e" or oracion[x] == "i" or oracion[x] == "o" or oracion[x] == "u":
        cant += 1
    x += 1

print(f'La cantidad de vocal/es que hay en la oracion es de: {cant}')