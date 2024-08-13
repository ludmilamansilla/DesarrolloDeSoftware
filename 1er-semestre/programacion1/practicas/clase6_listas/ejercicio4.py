""" 
Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la
lista y el promedio de sueldos.
"""

lista_sueldos = [1200,1520.45,1200,1320,1245.50]
sum=0

for i in range(len(lista_sueldos)):
    sum += lista_sueldos[i]

promedio = sum / len(lista_sueldos)

print(f'El promedio de los sueldos es: {promedio}')