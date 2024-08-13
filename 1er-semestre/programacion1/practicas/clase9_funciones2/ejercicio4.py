""" 
En una empresa se almacenaron los sueldos de 10 personas.
 Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
 a) Carga de los sueldos en una lista.
 b) Impresión de todos los sueldos.
 c) Cuántos tienen un sueldo superior a $4000.
 d) Retornar el promedio de los sueldos.
 e) Mostrar todos los sueldos que están por debajo del promedio.
"""

def sueldos():
    sueldos = []
    for i in range(10):
        n = int(input('Introduce el primer sueldo: '))
        sueldos.append(n)
    return sueldos

def sueldos_super(sueldos):
    cont = 0
    for i in range(len(sueldos)):
        if sueldos[i]>4000:
            cont += 1
    print(f'Los sueldos mayores a $4000 son {cont}')

def prom_sueldos(sueldos):
    sum = 0
    for i in range(len(sueldos)):
        sum += sueldos[i]
    promedio = sum / len(sueldos)
    print(f'El promedio de los sueldos es de: {promedio}')

# BLOQUE PRINCIPAL

sueldo = sueldos()
sueldos_super(sueldo)
prom_sueldos(sueldo)