compras_realizadas = int(input('Ingrese el total de compras realizadas: '))
monto_de_compra = int(input('Ingrese el monto de la nueva compra: '))
descuento = 0
if ( compras_realizadas >= 6 and monto_de_compra > 10000) :
        descuento = 0.35
total = monto_de_compra*(1-descuento)

print('El total es de '+str(total)+' CRC')