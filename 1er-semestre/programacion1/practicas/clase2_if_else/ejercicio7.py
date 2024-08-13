preguntas = int(input('Ingrese la cantidad total de preguntas: '))
rts_correctas = int(input('Ingrese la cantidad de preguntas contestadas correctamente: '))

porcentaje = rts_correctas*100 / preguntas

if porcentaje>=90:
    print('Nivel Máximo')
elif porcentaje>=75 and porcentaje<90:
    print('Nivel medio')
elif porcentaje>=50 and porcentaje<75:
    print('Nivel regular')
else:
    print('Fuera de nivel')


