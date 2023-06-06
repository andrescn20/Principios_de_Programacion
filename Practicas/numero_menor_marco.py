##Este programa recibe 3 numeros e indica cual es el menor

num1 = int(input('Ingrese el primer valor: '))
num2 = int(input('Ingrese el segundo valor: '))
num3 = int(input('Ingrese el tercer valor: '))

if (num1 < num2 and num1 < num3):
    menor = num1
elif (num2 < num1 and num2 < num3):
    menor = num2
else: 
    menor = num3

print('El numero menor es '+str(menor))

