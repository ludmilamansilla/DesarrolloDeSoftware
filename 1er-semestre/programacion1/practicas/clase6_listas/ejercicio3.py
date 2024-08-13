"""  
Definir una lista que almacene por asignación los nombres de 5 personas.
Contar cuantos de esos nombres tienen 5 o más caracteres. 
"""

lista = ["Ana", "Ludmila", "Lautaro", "Luz", "Abril"]
cont = 0
x=0

while x < len(lista):
    if len(lista[x])>= 5:
        cont += 1
    x += 1

print(f'La cantidad de nombres que tienen 5 letras o más son: {cont}')