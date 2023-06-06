fecha = int(input('Ingrese fecha de la funcion: '))
es_promocion = bool(input('Tiene promocion: '))
es_para_mayores = bool(input('Es para mayores: '))
valoracion = int(input('Ingerese la valoracion: '))

if (fecha > 15 or es_promocion) and (not es_para_mayores or valoracion > 4):
        print('Vamos al cine')
else: 
    print ('No vamos al cine')