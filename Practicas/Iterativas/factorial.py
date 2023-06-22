N = int(input('Ingrese el valor a calcular: '))
factorial = 1
sumatoria = 0

##Calculo de Factorial
for n in range(1, N+1):
    factorial = factorial*n

##Calculo de Sumatoria
for n in range(1, N+1):
    sumatoria = sumatoria+n


print('El factorial de ' + str(N) +' es ' + str(factorial))
print('La sumatoria desde 1 hasta' + str(N) +' es ' + str(sumatoria))