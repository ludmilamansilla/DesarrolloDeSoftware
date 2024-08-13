""" 
Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista.
Mostrar el nombre de persona menor en orden alfabético. 
"""

lista = []

for i in range(5):
    nombre = input('Ingrese el nombre:')
    lista.append(nombre)

menor = lista[0]

for i in range(5):
    if lista[i]<menor:
        menor = lista[i]

print(f'La lista ingresada de nombres es: {lista}')
print(f'El nombre con menor orden alfabético es: {menor}')