""" 
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el
promedio y cuántas más bajas. 
"""
lista = []

for i in range(5):
    altura = float(input('Ingrese una altura: '))
    lista.append(altura)


sum=0
for i in range(len(lista)):
    sum += lista[i]

promedio = sum / len(lista)

mas_bajas = 0
mas_altas = 0
x = 0

while x < len(lista):
    if (lista[x]<promedio):
        mas_bajas += 1
    else:
        mas_altas += 1
    x += 1

print(f'El promedio de las personas es: {promedio}')
print(f'Las personas más bajas que el promedio son: {mas_bajas}')
print(f'Las personas más altas que el promedio son: {mas_altas}')