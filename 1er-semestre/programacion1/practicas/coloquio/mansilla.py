# Ludmila Ayelén Mansilla, DNI: 44865030
# COLOQUIO

print('----- BIENVENIDO AL PROGRAMA DE CONTROL DE GASTOS PERSONALES -----')

lista = []

""" 
Esta función permite al usuario ingresar diferentes tipos de gastos según categorías predeterminadas (Alimentación, Educación, Vivienda, Transporte, Salud, Ocio, y Ahorro e Inversión).
Cada gasto se guarda como una tupla que contiene una descripción del gasto, el monto del gasto, y la categoría correspondiente.
El usuario puede continuar ingresando gastos hasta que decida salir del menú principal.
"""

def ingresar_gastos():
    continuar = 's'
    
    while continuar == 's':
        print('-.-.-.- MENÚ PRINCIPAL -.-.-.-')
        categoria = int(input('Seleccione el número de categoria del gasto que quiere ingresar: \n1. Alimentación \n2. Educación \n3. Vivienda \n4. Transporte \n5. Salud \n6. Ocio \n7. Ahorro e inversión \n'))
    
        if categoria == 1:
            print('¡Elegiste la categoria de almacen!')
            rta = 's'
            while rta == 's':
                cat_almacen = input('Ingrese el nombre del tipo de gasto desea ingresar: ')
                gasto_almacen = int(input('Ingrese el gasto: '))
                lista.append((f'Alimentación - Gasto de {cat_almacen}', gasto_almacen, categoria))
                rta = input('¿Desea agregar otro gasto de almacen? [s/n]: ')
    
        elif categoria == 2:
            print('¡Elegiste la categoria de Educación!')
            rta = 's'
            while rta == 's':
                institucion = input('Ingrese nombre de la institución: ')
                gasto_institucion = int(input('Ingrese el gasto: '))
                lista.append((f'Educación - Nombre de la institución: {institucion}, gasto', gasto_institucion, categoria))
                rta = input('¿Desea agregar otro gasto de educación? [s/n]: ')
        
        elif categoria == 3:
            print('¡Elegiste la categoria de Vivienda!')
            rta = 's'
            while rta == 's':
                cat_vivienda = input('Ingrese el nombre del tipo de gasto desea ingresar: ')
                gasto_vivienda = int(input('Ingrese el gasto: '))
                lista.append((f'Vivienda - Gasto de {cat_vivienda}', gasto_vivienda, categoria))
                rta = input('¿Desea agregar otro gasto de vivienda? [s/n]: ')
        
        elif categoria == 4: 
            print('¡Elegiste la categoria de Transporte!')
            rta = 's'
            while rta == 's':
                cat_transporte = input('Ingrese el nombre del tipo de gasto desea ingresar: ')
                gasto_transporte = int(input('Ingrese el gasto: '))
                lista.append((f'Transporte - Gasto de {cat_transporte}', gasto_transporte, categoria))
                rta = input('¿Desea agregar otro gasto de transporte? [s/n]: ')
        
        elif categoria == 5: 
            print('¡Elegiste la categoria de Salud!')
            rta = 's'
            while rta == 's':
                cat_salud = input('Ingrese el nombre del tipo de gasto desea ingresar: ')
                gasto_salud = int(input('Ingrese el gasto: '))
                lista.append((f'Salud - Gasto de {cat_salud}', gasto_salud, categoria))
                rta = input('¿Desea agregar otro gasto de salud? [s/n]: ')
        
        elif categoria == 6: 
            print('¡Elegiste la categoria de Ocio')
            rta = 's'
            while rta == 's':
                cat_ocio = input('Ingrese el nombre del tipo de gasto desea ingresar: ')
                gasto_ocio = int(input('Ingrese el gasto: '))
                lista.append((f'Ocio - Gasto de {cat_ocio}', gasto_ocio, categoria))
                rta = input('¿Desea agregar otro gasto de ocio? [s/n]: ')
        
        elif categoria == 7: 
            print('¡Elegiste la categoria de Ahorro e inversión')
            rta = 's'
            while rta == 's':
                cat_ahorro_inversion = input('Ingrese el nombre del tipo de gasto desea ingresar: ')
                gasto_ahorro_inversion = int(input('Ingrese el gasto: '))
                lista.append((f'Ahorro e inversión - Gasto de {cat_ahorro_inversion}', gasto_ahorro_inversion, categoria))
                rta = input('¿Desea agregar otro gasto de ahorro e inversión? [s/n]: ')
        
        else:
            print('¡La opción seleccionada es incorrecta!')
            
        continuar = input('¿Desea volver al menú principal? [s/n]: ')
    
    return lista

""" 
Esta función recibe la lista de gastos y calcula el total sumando los montos de todos los gastos.
"""

def suma_gastos(gastos):
    total = 0
    for i, gasto, k in gastos:
        total += gasto
    return total

""" 
Esta función ordena la lista de gastos de menor a mayor según el monto del gasto utilizando el algoritmo de burbuja (bubble sort).
Recorre la lista de gastos y compara los montos, intercambiándolos si es necesario para ordenar la lista.
"""

def ordenar_gastos(gastos):
    n = len(gastos)
    for i in range(n):
        for j in range(0, n-i-1):
            if gastos[j][1] > gastos[j+1][1]:
                gastos[j], gastos[j+1] = gastos[j+1], gastos[j]
    return gastos

""" 
Esta función permite al usuario consultar los gastos según la categoría seleccionada.
Recibe la lista de gastos y la categoría a consultar.
Busca y muestra todos los gastos correspondientes a la categoría seleccionada, y preguntará si quiere buscar otro gasto.
Si no encuentra gastos en esa categoría, muestra un mensaje indicando que no se encontraron gastos registrados.
"""

def consultar_gasto(gastos, categoria):
    encontrados = []
    
    for desc, gasto, cat in gastos:
        if categoria == cat:
            encontrados.append((desc, gasto))
    
    if len(encontrados) == 0:
        print("No se encuentra ningún gasto registrado en esta categoría.")
    else:
        print("\nGastos encontrados en la categoría seleccionada:")
        for desc, gasto in encontrados:
            print(f"{desc}: ${gasto}")

    

# BLOQUE PRINCIPAL

# Llamamo a la función ingresar_gastos para permitir al usuario ingresar gastos.
gastos = ingresar_gastos()

# Imprimo los gastos ingresados por el usuario.
print('\nGastos ingresados: ')
for desc, gasto, _ in gastos:
    print(f'{desc}: ${gasto}')

# Calculo el total de todos los gastos utilizando la función suma_gastos.
total_gastos = suma_gastos(gastos)
print(f'\nEl total de gastos es de: ${total_gastos}')

# Ordenamos los gastos de menor a mayor utilizando la función ordenar_gastos.
gastos_ordenados = ordenar_gastos(gastos)
print("\nLista de gastos ordenada de menor a mayor:")
for desc, gasto, _ in gastos_ordenados:
    print(f"{desc}: ${gasto}")

# Bucle que permite al usuario consultar gastos por categoría repetidamente.
while True:
    # Solicita al usuario que ingrese el número de la categoría para consultar los gastos.
    categoria = int(input("\nIngrese el número de la categoría para consultar los gastos: "))
    
    # Llama a la función consultar_gasto para mostrar los gastos de la categoría seleccionada.
    consultar_gasto(gastos, categoria)
    
    # Pregunto al usuario si desea buscar otro gasto por categoría.
    continuar_busqueda = input('\n¿Desea buscar otro gasto por categoría? [s/n]: ')
    
    # Si el usuario responde algo diferente de 's', salimos del bucle.
    if continuar_busqueda.lower() != 's':
        break