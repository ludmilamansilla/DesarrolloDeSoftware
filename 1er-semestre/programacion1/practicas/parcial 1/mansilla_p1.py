# Ludmila Mansilla, DNI: 44865030

valor = int(input('Ingrese un valor: '))
sum = 0

for i in range(1,valor+1):
    if i%2==0:
        print("\n",i)
        sum += i

print(f'\nLa suma de los números pares es: {sum}')    

