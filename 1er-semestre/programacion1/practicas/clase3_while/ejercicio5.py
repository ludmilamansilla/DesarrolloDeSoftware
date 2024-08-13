""" 
Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe
cuántos tienen notas mayores o iguales a 7 y cuántos menores.
"""
cont=1
notaBuena = 0
notaMala = 0

while cont<=10:
    
    nota = int(input('Ingrese su nota:'))
    
    if nota>=7:
        notaBuena += 1
    else:
        notaMala += 1
        
    cont += 1

print(f'La cantidad de notas >= 7 son {notaBuena}')
print(f'La cantidad de notas < 7 son {notaMala}')