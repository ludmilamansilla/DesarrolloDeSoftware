# Ludmila Mansilla DNI: 44865030

# Creo función para que el usuario cargue la cantidad de palabras que desea, asi formar una lista con esa longitud
def ingresar_palabras():
    palabras = []
    n = int(input('¿Cuántas palabras desea ingresar?'))
    for i in range(n):
        palabra = input('Ingrese una palabra: ')
        palabras.append(palabra)
    return palabras

def encontrar_palabras_con_letra(palabras, letra):
    lista_contiene_letra = []
    # Mediante el for recorro la lista, y con otro for anidado recorro letra por letra, así cuando encuentra la letra que busca la devuelva.
    for i in range(len(palabras)):
        for x in palabras[i]:
            if letra == x:
                lista_contiene_letra.append(palabras[i])
                print(f'En la palabra {palabras[i]} esta la letra {letra}')
    print(f'La lista de palabras que contienen la letra {letra} es: {lista_contiene_letra}')

def ordenar_palabras_longitud(palabras):
    #  Mediante el algoritmo de ordenamiento de burbuja comparo los elementos de la lista y cambio su posición si es necesario
    for i in range(len(palabras)):
        for j in range(i + 1, len(palabras)):
            if palabras[i] > palabras[j]:
                palabras[i], palabras[j] = palabras[j], palabras[i]
    print(f'Lista de palabras ordenada de menor a mayor: {palabras}')

# Bloque Principal

palabras = ingresar_palabras()
letra = input("Ingrese la letra que quiere buscar: ")
palabras_con_letra = encontrar_palabras_con_letra(palabras, letra)
palabras_ordenadas_por_longitud = ordenar_palabras_longitud(palabras)