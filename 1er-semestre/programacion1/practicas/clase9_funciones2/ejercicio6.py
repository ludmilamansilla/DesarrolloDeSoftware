""" 
Confeccionar un programa que permita:
 a) Cargar una lista de 10 elementos enteros.
 b) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
 c) Imprimir las dos listas generadas.
"""

def list():
    lista_positiva = []
    lista_negativa = []
    for i in range(10):
        n = int(input('Ingrese un número: '))
        if n >= 0:
            lista_positiva.append(n)
        else:
            lista_negativa.append(n)
    return lista_positiva, lista_negativa

print(list())