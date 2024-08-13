""" 
Almacenar en una lista de 5 elementos los nombres de empleados de una empresa junto a sus últimos tres sueldos (estos tres valores en una tupla)
El programa debe tener las siguientes funciones:
a)Carga de los nombres de empleados y sus últimos tres sueldos.
b)Imprimir el monto total cobrado por cada empleado.
c)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses. 
"""

def carga():
    empleados = []
    for i in range(5):
        name = input('Ingrese nombre del empleado: ')
        sueldo1 = int(input('Ingrese primer sueldo: '))
        sueldo2 = int(input('Ingrese segundo sueldo: '))
        sueldo3 = int(input('Ingrese tercer sueldo: '))
        empleados.append([name,(sueldo1,sueldo2,sueldo3)])
    return empleados

def ganancias(empleados):
    print("Monto total ganado por empleado en los ultimos tres meses")
    for i in range(5):
        total = empleados[i][1][0] + empleados[i][1][1] + empleados[i][1][2]
        print(empleados[i][1], total)

def ganancia_10000(empleados):
    print("Empleados con ingresos superiores a 10000 en los ultimos 3 meses")
    for i in range(5):
        total = empleados[i][1][0] + empleados[i][1][1] + empleados[i][1][2]
        if total > 10000:
            print(empleados[i][1], total)

# bloque principal

empleados = carga()
ganancias(empleados)
ganancia_10000(empleados)