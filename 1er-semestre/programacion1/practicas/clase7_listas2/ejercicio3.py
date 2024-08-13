""" 
Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y
mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente. 
"""
elementos = []

for i in range(5):
    elemento = int(input('Ingresa un número: '))
    elementos.append(elemento)

for x in range(5):
    for i in range(4-x):
        if elementos[i]>elementos[i+1]:
            aux = elementos[i+1]
            elementos[i+1] = elementos[i]
            elementos[i] = aux

print(f'Lista ordenada de menor a mayor: {elementos}')

for x in range(5):
    for i in range(4-x):
        if elementos[i]<elementos[i+1]:
            aux = elementos[i]
            elementos[i] = elementos[i+1]
            elementos[i+1] = aux

print(f'Lista ordenada de mayor a menor: {elementos}')