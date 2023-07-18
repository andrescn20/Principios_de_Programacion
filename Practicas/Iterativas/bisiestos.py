usuario_continua = True

while usuario_continua:
    ano = int(input('Ingrese el año que desea consultar: '))

    if (ano % 4 == 0):
    ##Aca adentro todo es multiplo de 4
        if(ano % 100 == 0 and ano % 400 == 0 ):
            ##Aca es multiplo de 4, 100 y 400
            print('Este año si es bisiesto')
        elif(ano % 100 == 0):
            #Aca es multiplo de 4 y 100 pero no 400
            print('El año no es bisiesto')
        else:
            ##Aca es multiplo de 4 pero no de 100
            print('El año si es bisiesto')
    else:
        print('Este año no es bisiesto')
    
    respuesta_usuario = input('¿Desea evaluar otro año?. Responda si o no: ')
    if(respuesta_usuario == 'no'):
        usuario_continua = False

print('Gracias por utilizar nuestro software.')
    