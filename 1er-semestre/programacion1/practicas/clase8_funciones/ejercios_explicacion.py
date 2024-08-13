""" 
Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la
carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del
programa.
Implementar estas actividades en tres funciones.
"""

def presentacion():
 print("Programa que permite cargar dos valores por teclado.")
 print("Efectua la suma de los valores")
 print("Muestra el resultado de la suma")
 print("*******************************")
def carga_suma():
 valor1=int(input("Ingrese el primer valor:"))
 valor2=int(input("Ingrese el segundo valor:"))
 suma=valor1+valor2
 print("La suma de los dos valores es:",suma)
def finalizacion():
 print("*******************************")
 print("Gracias por utilizar este programa")

# programa principal
presentacion()
carga_suma()
finalizacion()


""" 
Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
Repetir la carga e impresion de la suma 5 veces.
Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.
"""

def carga_suma():
 valor1=int(input("Ingrese el primer valor:"))
 valor2=int(input("Ingrese el segundo valor:"))
 suma=valor1+valor2
 print("La suma de los dos valores es:",suma)
def separacion():
 print("*******************************")

# programa principal
for x in range(5):
 carga_suma()
 separacion()


""" 
Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la
carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del
programa.
"""

def mostrar_mensaje(mensaje):
 print("*************************************************")
 print(mensaje)
 print("*************************************************")
def carga_suma():
 valor1=int(input("Ingrese el primer valor:"))
 valor2=int(input("Ingrese el segundo valor:"))
 suma=valor1+valor2
 print("La suma de los dos valores es:",suma)

# programa principal
mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado.")
carga_suma()
mostrar_mensaje("Gracias por utilizar este programa")

""" 
Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de
los valores hacerlo por teclado
"""

def mostrar_mayor(v1,v2,v3):
    print("El valor mayor de los tres numeros es")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)

def cargar():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    valor3=int(input("Ingrese el tercer valor:"))
    mostrar_mayor(valor1,valor2,valor3)

# programa principal
cargar()

""" 
Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere
calcular y mostrar su perímetro o su superficie.
"""

def mostrar_perimetro(lado):
    per=lado*4
    print("El perimetro es",per)

def mostrar_superficie(lado):
    sup=lado*lado
    print("La superficie es",sup)

def cargar_dato():
    la=int(input("Ingrese el valor del lado de un cuadrado:"))
    respuesta=input("Quiere calcular el perimetro o la superficie[ingresar texto: perimetro/superficie]?")
    if respuesta=="perimetro":
        mostrar_perimetro(la)
    if respuesta=="superficie":
        mostrar_superficie(la)

# programa principal
cargar_dato()

""" 
Confeccionar una función que le enviemos como parámetro el valor del lado de un 
cuadrado y nos retorne su superficie.
"""

def retornar_superficie(lado):
 sup=lado*lado
 return sup

# bloque principal del programa
va = int(input("Ingrese el valor del lado del cuadrado:"))
superficie = retornar_superficie(va)
print(f"La superficie del cuadrado es: {superficie}")

""" 
Confeccionar una función que le enviemos como parámetros 
dos enteros y nos retorne el mayor.
"""

def retornar_mayor(v1,v2):
    if v1>v2:
        mayor = v1
    else:
        mayor = v2
    return mayor

# bloque principal
valor1=int(input("Ingrese el primer valor:"))
valor2=int(input("Ingrese el segundo valor:"))
print(retornar_mayor(valor1,valor2))

""" 
Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad
de caracteres que tiene. En el bloque principal solicitar la carga de dos nombres por teclado y
llamar a la función dos veces. Imprimir en el bloque principal cual de las dos palabras tiene más
caracteres.
"""

def largo(cadena):
 return len(cadena)

# bloque principal
nombre1=input("Ingrese primer nombre:")
nombre2=input("Ingrese segundo nombre:")
la1=largo(nombre1)
la2=largo(nombre2)

if la1==la2:
     print("Los nombres:",nombre1,nombre2,"tienen la misma cantidad de caracteres")
else:
    if la1>la2:
        print(nombre1,"es mas largo")
    else:
        print(nombre2,"es mas largo")

