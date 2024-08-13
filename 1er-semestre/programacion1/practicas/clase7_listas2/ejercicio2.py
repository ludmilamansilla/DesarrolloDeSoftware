""" 
Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear y
cargar una lista con todos los sueldos de dichos empleados. Imprimir la lista de
sueldos ordenamos de menor a mayor. 
"""

sueldos = []
cant_empleados = int(input('Ingresar la cantidad de empleados que tiene la empresa: '))

for i in range(cant_empleados):
    sueldo = int(input('Ingresar el sueldo: '))
    sueldos.append(sueldo)


for x in range(len(sueldos)):
    for i in range((len(sueldos)-1)-x):
        if sueldos[i] > sueldos[i+1]:
            aux = sueldos[i]
            sueldos[i] = sueldos[i+1]
            sueldos[i+1] = aux

print(f'Lista de sueldos ordenada. {sueldos}')