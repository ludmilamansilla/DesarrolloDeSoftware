""" 
Crear dos listas paralelas. En la primera ingresar los nombres de empleados y
en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la
empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el
sueldo como su nombre) 
"""

nombres = []
sueldos = []

cant_empleados = int(input('¿Cuantos empleados tiene la empresa?: '))

for i in range(cant_empleados):
    
    nombre = input('Ingresa el nombre del empleado: ')
    nombres.append(nombre)
    
    sueldo = int(input('Ingresa el sueldo del empleado: '))
    sueldos.append(sueldo)
    
    i = 0
    while i<len(sueldos):
        if sueldos[i]>10000:
            sueldos.pop(i)
            nombres.pop(i)
        else: 
            i += 1

print(f'Los empleados son: {nombres}, y sus respectivos sueldos son: {sueldos}')

