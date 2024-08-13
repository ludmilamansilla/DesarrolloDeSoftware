""" 
Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la
cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir los
resultados. Por último ordenar con respecto a la cantidad de habitantes (de mayor
a menor) e imprimir nuevamente.
"""

paises = []
habitantes = []

for i in range(5):
    pais = input('Ingrese un país: ')
    cant_hab = int(input('Ingrese la cantidad de habitantes correspondiente al mismo: '))
    paises.append(pais)
    habitantes.append(cant_hab)

for i in range(4):
    for x in range(4-i):
        if paises[x]>paises[x+1]:
            aux1 = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux1
            aux2 = habitantes[x]
            habitantes[x] = habitantes[x+1]
            habitantes[x+1] = aux2

print("Listado de paises en orden alfabetico")
for x in range(5):
    print(paises[x],habitantes[x])     

for i in range(4):
    for x in range(4-i):
        if habitantes[x]<habitantes[x+1]:
            aux1 = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux1
            aux2 = habitantes[x]
            habitantes[x] = habitantes[x+1]
            habitantes[x+1] = aux2


print("Listado de paises por cantidad de habitantes")
for x in range(5):
 print(paises[x],habitantes[x])