""" 
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8
empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa que
permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.
"""

mañana = []
tarde = []

print('SUELDOS TURNO MAÑANA')
for i in range(4):
    sueldo_mañana = int(input('Ingrese sueldo: '))
    mañana.append(sueldo_mañana)

print('SUELDOS TURNO TARDE')
for i in range(4):
        sueldo_tarde = int(input('Ingrese sueldo: '))
        tarde.append(sueldo_tarde)


print(f'Los sueldos del turno mañana son: {mañana}')
print(f'Los sueldos del turno tarde son: {tarde}')