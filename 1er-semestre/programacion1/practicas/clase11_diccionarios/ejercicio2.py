""" 
Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave
sea el número de documento del alumno. Como valor almacenar una lista con
componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
a) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
b) Listado de todos los alumnos con sus notas
c) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas. 
"""

def cargar():
    alumnos = {}
    for i in range(3):
        dni = int(input('Ingrese su número de DNI sin puntos: '))
        materias = []
        continuar = 's'
        while continuar == 's':
            materia = input('Ingrese el nombre de la materia: ')
            nota = float(input('Ingrese la nota: '))
            materias.append((materia, nota))
            continuar = input('¿Deseas cargar otra materia para dicho alumno? [s/n]: ')
        alumnos[dni] = materias
    return alumnos

def listado(alumnos):
    for dni in alumnos:
        print(f'DNI del alumno: {dni}')
        print(f'Materias que cursa y sus notas: ')
        for nota, materia in alumnos[dni]:
            print(materia, nota)

def consultar(alumnos):
    dni = int(input('Ingrese DNI (sin puntos) para consultar las materias que cursa y sus notas: '))
    if dni in alumnos:
        for nota, materia in alumnos[dni]:
            print(materia, nota)

# BLOQUE PRINCIPAL

alumnos = cargar()
listado(alumnos)
consultar(alumnos)