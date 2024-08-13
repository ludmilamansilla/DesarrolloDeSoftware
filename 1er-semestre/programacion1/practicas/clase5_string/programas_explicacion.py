""" 
Realizar la carga por teclado del nombre, edad y altura de dos personas. Mostrar por pantalla el
nombre de la persona con mayor altura.
"""

nombre1 = input('Ingrese el primer nombre: ')
edad1 = int(input('Ingrese la primera edad: '))
altura1 = float(input('Ingrese la primer altura (ejm: 1.70): '))

nombre2 = input('Ingrese el segundo nombre: ')
edad2 = int(input('Ingrese la segunda edad: '))
altura2 = float(input('Ingrese la segunda altura (ejm: 1.70): '))

if altura1 > altura2:
    print(f'¡{nombre1} es más alt@!')
else:
    print(f'¡{nombre2} es más alt@!')


""" 
Realizar la carga de dos nombres por teclado. Mostrar cual de los dos es mayor alfabéticamente
o si son iguales.
"""

nombre1 = input('Ingrese el primer nombre: ')
nombre2 = input('Ingrese el segundo nombre: ')

if nombre1 == nombre2:
    print('Ingresaste dos nombres iguales')
elif nombre1>nombre2:
    print(f'{nombre1} es mayor alfabeticamente')
else:
    print(f'{nombre2} es mayor alfabeticamente')


""" 
Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si desea cargar
otro valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
Mostrar la suma de los valores ingresados.
"""

opcion = "si"
suma = 0

while opcion == "si":
    valor = int(input("Ingrese un valor: "))
    suma += valor
    opcion = input("¿Deseas cargar otro número? (si/no): ")

print(f'La suma de los valores ingresados es: {suma}')

""" 
Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".
"""

mail = input("Ingrese un mail: ")
cantidad=0
x=0

while x<len(mail):
    if mail[x]=="@":
        cantidad += 1
    x += 1

if cantidad==1:
    print("Contiene solo un caracter @ el mail ingresado")
else:
    print("Incorrecto")