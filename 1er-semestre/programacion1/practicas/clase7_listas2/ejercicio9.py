""" 
Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos
días
"""

empleados = []
faltas = []

for i in range(3):
    nombre = input('Ingrese nombre del empleado: ')
    empleados.append(nombre)
    
    cant_faltas = int(input('¿Cuántas veces falto el empleado?: '))
    faltas.append([])    
    for x in range(cant_faltas):
        dia = int(input('Ingresa el número de día que falto: '))
        faltas[i].append(dia)

print("Nombres de empleados y cantidad de inasistencias")
for x in range(3):
    print(empleados[x],len(faltas[x]))

menos = len(faltas[0])
for x in range(1,3):
    if len(faltas[x])<menos:
        menos = len(faltas[x])

print("Empleado o empleados que faltaron menos")
for x in range(3):
 if len(faltas[x])==menos:
     print(empleados[x])
