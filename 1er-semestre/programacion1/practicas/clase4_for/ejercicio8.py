""" 
Se cuenta con la siguiente información:
 Las edades de 5 estudiantes del turno mañana.
 Las edades de 6 estudiantes del turno tarde.
 Las edades de 11 estudiantes del turno noche.
 Las edades de cada estudiante deben ingresarse por teclado.
 a) Obtener el promedio de las edades de cada turno (tres promedios)
 b) Imprimir dichos promedios (promedio de cada turno)
 c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
"""

sum = 0

for i in range(5):
    edad = int(input('Ingrese la edad: '))
    sum += edad

prom_man = sum / 5
print(f'El promedio de edad del turno mañana es de: {prom_man}')

sum = 0

for i in range(6):
    edad = int(input('Ingrese la edad: '))
    sum += edad

prom_tar = sum / 6
print(f'El promedio de edad del turno tarde es de: {prom_tar}')

sum = 0

for i in range(11):
    edad = int(input('Ingrese la edad: '))
    sum += edad

prom_noc = sum / 11
print(f'El promedio de edad del turno tarde es de: {prom_noc}')

if prom_man > prom_tar and prom_man > prom_noc:
    print('El turno con promedio de edad mayor es la mañana')
elif prom_tar > prom_man and prom_tar > prom_noc:
    print('El turno con promedio de edad mayor es la tarde')
elif prom_noc > prom_tar and prom_noc > prom_man:
    print('El turno con promedio de edad mayor es la noche')