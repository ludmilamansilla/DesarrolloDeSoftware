""" 
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y
$500, realizar un programa que lea los sueldos que cobra cada empleado e
informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de
$300. Además el programa deberá informar el importe que gasta la empresa en
sueldos al personal.
"""

cant_empleados = int(input('Ingrese la cantidad de empleados en la empresa: '))

cont = 1
sueldos_rang_1_3 = 0
sueldos_mayor_3 = 0
sum = 0

while cont <= cant_empleados:
    sueldo = int(input('Ingrese su sueldo: '))
    if sueldo >= 100 and sueldo <= 300:
        sueldos_rang_1_3 += 1
    elif sueldo > 300:
        sueldos_mayor_3 += 1
    sum += sueldo
    cont += 1

print(f'La cantidad de empleados que cobran entre $100 y $300 son: {sueldos_rang_1_3}')
print(f'La cantidad de empleados que cobran más de $300 son: {sueldos_mayor_3}')
print(f'La empresa para pagarle a todos los empleados gasta un monto de: ${sum}')