# 1)
for i in range(101):
    print(i)
    
# 2)
for i in range(20,31):
    print(i)

# 3)
for i in range(1,101):
    if i%2==1:
        print(i)

# La función range puede tener también tres parámetros, el primero indica el valor inicial que
# tomará la variable x, el segundo parámetro el valor final (que no se incluye) y el tercer
# parámetro indica cuanto se incrementa cada vuelta x.

for i in range(1,100,2):
    print(i)
    
# 4) 
sum = 0

for i in range(10): 
    num = int(input('Ingrese el valor: '))
    sum += num

print(f'La suma de los números ingresados es {sum}')
prom = sum / 10
print(f'El promedio es {prom}')

# 5)
nota_aprob = 0
nota_desap = 0

for i in range(10):
    nota = int(input('Ingrese la nota: '))
    if nota >= 7:
        nota_aprob += 1
    elif nota < 7:
        nota_desap += 1

print(f'Los alumnos que tienen nota >=7 son: {nota_aprob} y los que tienen nota <7 son {nota_desap}')

# 6)

for i in range(10):
    num = int(input('Ingrese el valor: '))
    if num%3==0 and num%5==0:
        print(f'El {num} es múltiplo de 3 y 5')
    elif num%3==0:
        print(f'El {num} es múltiplo de 3')
    elif num%5==0:
        print(f'El {num} es múltiplo de 5')
    else:
        print(f'No es multiplo ni de 3 ni de 5')
 
# 7)
n = int(input('Ingrese la cantidad de valores que ingresará:'))
cant = 0

for i in range(n):
    num = int(input('Ingrese un número:'))
    if num >= 1000:
        cant += 1

print(f'La cantidad de números mayores a 1000 ingresada es de: {cant}')