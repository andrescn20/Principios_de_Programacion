##Recibo el salario como dato de entrada

salario = int(input('Ingrese el salario: '))

##Defino el % de impuesto a cobrar
impuesto = 0.1 ##Esto equivale al 10%

##Si el salario es más de 1 000 000, le rebajamos el 10%
if salario >= 1000000:
    salario = int(salario*(1-impuesto)) ##Esto nos retorna el equivalente al 90%
    
print('El salario neto del trabajador es de ' + str(salario) +' CRC')