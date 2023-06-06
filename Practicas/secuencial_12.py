##Queremos un programa que reciba las hora de entrada y de salida de Felipe. Además recibe la tarifa horaria. 
##Con estos datos queremos que nos calcule lo que se le debe pagar a Felipe y la cantidad de horas que trabajó

##Datos de entrada.
##Nota: Las horas solo son en formato de 24h y sin minutos. 
hora_entrada = int(input('Introduzca la hora de entrada: '))
hora_salida = int(input('Introduzca la hora de salida: '))
tarifa_horaria =  int(input('Introduzca la tarifa por hora: '))

horas_trabajadas = hora_salida - hora_entrada 
monto_a_pagar = tarifa_horaria * horas_trabajadas

print('Felipe trabajó ' + str(horas_trabajadas) + ' horas. Se le debe pagar '+str(monto_a_pagar)+'.')


