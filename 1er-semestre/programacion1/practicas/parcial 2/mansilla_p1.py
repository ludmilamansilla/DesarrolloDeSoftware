# Ludmila Mansilla DNI: 44865030

# Creo una funcion para cargar los datos del empleado, el nombre y su sueldo:

def cargar():
    
    cantidad = int(input('¿Cuántos empleados desea cargar?: '))
    
    nombres = []
    sueldos = []
    
    for i in range(cantidad):
        nombre = input('Ingrese nombre del empleado: ')
        nombres.append(nombre)
        sueldo = int(input('Ingrese el sueldo de dicho empleado: $'))
        sueldos.append(sueldo)
    return [nombres, sueldos]

# creo la funcion calcular_promedio_sueldos() que me saca el promedio en cuestion de todos los sueldos ingresados

def calcular_promedio_sueldos(sueldos):
    sum = 0
    for n in range(len(sueldos)):
        sum += sueldos[n]
    promedio = sum / len(sueldos)
    print(f'El promedio de los sueldos es de: {promedio:.2f}') # .2f (para que me muestre 2 decimales)
    

# Creo la funcion obtener_empleado_sueldo_max() asi mediante un for recorro todos los sueldos y voy comparando así descubrir cual es el mayor, y una vez recorrida toda la lista imprimo.

def obtener_empleado_sueldo_max(sueldos, nombres):
    may = sueldos[0]
    nom = 0
    for i in range(1, len(sueldos)):
        if sueldos[i] > may:
            may = sueldos[i]
            nom = i
    print(f'El empleado con mayor sueldo es {nombres[nom]} y su sueldo es de ${may}')

def ordenar_por_sueldo(nombres, sueldos):

#  Utilizo el algoritmo de ordenamiento de burbuja para comparar los elementos de la lista y cambiar su posición si es necesario

    for i in range(len(sueldos)):
        for j in range(i + 1, len(sueldos)):
            if sueldos[i] > sueldos[j]:
                sueldos[i], sueldos[j] = sueldos[j], sueldos[i]
    
    print('Sueldos ordenados de menor a mayor: ')
    
    for i in range(len(nombres)):
        print(f"{nombres[i]}: ${sueldos[i]}")
  

# BLOQUE PRINCIPAL

nombres, sueldos = cargar()
calcular_promedio_sueldos(sueldos)
obtener_empleado_sueldo_max(sueldos, nombres)
ordenar_por_sueldo(nombres, sueldos)