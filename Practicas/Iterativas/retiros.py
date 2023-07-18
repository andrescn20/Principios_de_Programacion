#Primero vamos a recibir el saldo inicial de la cuenta
saldo_inicial = int(input('Ingrese el saldo inicial de su cuenta: '))
saldo_restante = saldo_inicial

#Vamos a permitirle al usuario hacer retiros
while saldo_restante > 0:
    retiro = int(input('¿Cuánto desea retirar?: '))

    #Si el saldo restante es mayor al retiro solicitado, se retira.
    if(retiro <= saldo_restante):
        saldo_restante = saldo_restante - retiro
    #Si no, indica que no hay fondos
    else: 
        print('El saldo disponible no es suficiente.')

    print(f'Su saldo actual es de {saldo_restante}.')

print(f'No tiene saldo disponible')
