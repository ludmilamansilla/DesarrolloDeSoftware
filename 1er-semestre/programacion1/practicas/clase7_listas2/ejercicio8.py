""" 
Se desea saber la temperatura media trimestral de cuatro paises. Para ello se
tiene como dato las temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias
mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los
datos en memoria.
a - Cargar por teclado los nombres de los paises y las temperaturas medias
mensuales.
b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las
mismas.
c - Calcular la temperatura media trimestral de cada país.
c - Imprimr los nombres de los paises y las temperaturas medias trimestrales.
b - Imprimir el nombre del pais con la temperatura media trimestral mayor. 
"""

paises = []
temperaturas = []
promedio_temperatura = []

for i in range(4):
    pais = input('Ingresa el país: ')
    paises.append(pais)
    
    temperaturas.append([])
    for x in range(3):
        temperatura = int(input('Ingresa la temperatura media mensuales: '))
        temperaturas[i].append(temperatura)

print(f'Los paises son: {paises} y sus temperaturas: {temperaturas}')

for i in range(4):
    promedio = (temperaturas[i][0]+temperaturas[i][1]+temperaturas[i][2]) // 3
    promedio_temperatura.append(promedio)

print(f'Los paises y las temperaturas medias trimestrales: ')
for i in range(4):
    print(paises[i],promedio_temperatura[i])


mayor = 0
for i in range(1,4):
    if promedio_temperatura[i]>promedio_temperatura[mayor]:
        mayor = i

print(f'El pais con temperatura media trimestral mayor es {paises[mayor]}')