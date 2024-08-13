"""  
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
 a) La cantidad de valores ingresados negativos.
 b) La cantidad de valores ingresados positivos.
 c) La cantidad de múltiplos de 15.
 d) El valor acumulado de los números ingresados que son pares.
"""
cont = 0
posit = 0
neg = 0
par = 0
mult15 = 0

for i in range(10):
    num = int(input('Ingrese un valor: '))
    if num>=0:
        if num%2==0:
            par += 1
        elif num%15==0:
            mult15 +=1    
        posit += 1
    elif num<0: 
        if num%2==0:
            par += 1
        if num%15==0:
            mult15 +=1
        neg += 1
        
print(f'La cantidad de números ingresados negativos es de {neg}')
print(f'La cantidad de números ingresados positivos es de {posit}')
print(f'La cantidad de números ingresados múltiplos de 15 es de {mult15}')
print(f'La cantidad de números ingresados pares es de {par}')