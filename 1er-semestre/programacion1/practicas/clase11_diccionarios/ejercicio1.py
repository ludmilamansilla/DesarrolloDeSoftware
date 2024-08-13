""" 
Crear un diccionario en Python que defina como clave el número de
documento de una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
a) Cargar por teclado los datos de 4 personas.
b) Listado completo del diccionario.
c) Consulta del nombre de una persona ingresando su número de documento. 
"""

def cargar():
    personas = {}
    for i in range(4):
        nombre = input('Ingrese su nombre: ')
        dni = int(input('Ingrese DNI sin puntos: '))
        personas[dni] = nombre
    return personas

def imprimir(personas):
    print('Listado del diccionario completo: ')
    for numero in personas:
        print(numero, personas[numero])

def consultar(personas):
    num = int(input('Ingrese número de DNI de la persona que desea consultar: '))
    if num in personas:
        print(f'Nombre de la persona: {personas[num]}')
    else:
        print('No existe una persona registrada con ese DNI')

# Bloque principal

personas = cargar()
imprimir(personas)
consultar(personas)