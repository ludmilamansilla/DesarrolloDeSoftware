""" 
Realizar un programa que permita cargar dos listas de 15 valores cada una.
Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor
(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un
algoritmo.
"""


cont = 1
sum1 = 0
sum2 = 0

print('**** Primera lista ****')
while cont <= 15:
    cant = int(input('Ingrese valor: '))
    sum1 += cant
    cont += 1

cont = 1

print('**** Segunda lista ****')
while cont <= 15:
    cant = int(input('Ingrese valor: '))
    sum2 += cant
    cont += 1

if sum1==sum2:
    print('Las listas son iguales')
elif sum1>sum2:
    print('La lista 1 es mayor')
else:
    print('La lista 2 es mayor')