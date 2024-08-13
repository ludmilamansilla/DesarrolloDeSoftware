""" 
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben
procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En
la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la
nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”. 
"""

nombres = []
notas = []
cont = 0

for i in range(4):
    nombre = input('Ingrese el nombre del alumno: ')
    nombres.append(nombre)
    nota = int(input('Ingrese la nota del correspondiente alumno: '))
    notas.append(nota)

for i in range(4):
        if notas[i]>=8:
            print(f"El alumno {nombres[i]} tiene: Muy Bueno")
            cont += 1
        elif 4<=notas[i]<=7:
            print(f"El alumno : {nombres[i]} tiene: Bueno")
        else:
            print(f"El alumno : {nombres[i]} tiene: Insuficiente")


print(f'Los alumnos son: {nombres}')
print(f'Las notas son: {notas}')
print(f'Los alumnos que consiguieron "Muy bueno" son: {cont}')