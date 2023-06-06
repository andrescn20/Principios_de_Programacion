##Definimos el precio regular 

precio = 4500

dia_semana = input('Introduzca el dia de la semana: ')

## Si es miercoles, redefine el precio a la mitad
if dia_semana == 'miercoles' or 'miércoles':
    precio = precio/2

#Imprime precio   
print(precio)



