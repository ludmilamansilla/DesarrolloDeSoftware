""" 
Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto
cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
"""
cuad1=0
cuad2=0
cuad3=0
cuad4=0
cant = int(input('Ingrese la cantidad de puntos a procesar: '))

for i in range(cant):
    x = int(input('Ingrese la coordenada x: '))
    y = int(input('Ingrese la coordenada y: '))
    if x>0 and y>0:
        cuad1 += 1
    elif x<0 and y>0:
        cuad2 += 1
    elif x<0 and y<0:
        cuad3 += 1
    elif x>0 and y<0:
        cuad4 += 1

print(f'La cantidad de puntos en el cuadrante uno es de: {cuad1}, en el cuadrante dos es de: {cuad2}, en el cuadrante tres es de: {cuad3} y en el cuadrante cuatro es de: {cuad4}')