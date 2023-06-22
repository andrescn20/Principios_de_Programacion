def saludar():
     print('Hola querido usuario.')

saludar()

datos_ingeniero = [3, 6, 5, 2, 3]

def operacion_complicada(x):
     resultado = ((x**2+4*x-3)**(1/3))/(4-x) 
     return resultado

def operacion_sencilla(x):
     return (x*3600)/(x**2)

for x in datos_ingeniero:
    resultado_nuevo = operacion_sencilla(x)
    resultado_viejo = operacion_complicada(x)
    print('Para el valor ' + str(x)+', el resultado nuevo es: ' + str(resultado_nuevo)+' y el viejo es: ' +str(resultado_viejo))

##Necesito que, para el menor valor, me devuelva la division de ambos resultados

minimo_valor = min(datos_ingeniero)
x = minimo_valor
division_mistica = operacion_complicada(minimo_valor) / operacion_sencilla(minimo_valor)

## Ahora calcule ademas la multiplicacion de esos resultados 
multiplicacion_mistica = operacion_complicada(minimo_valor) * operacion_sencilla(minimo_valor)




