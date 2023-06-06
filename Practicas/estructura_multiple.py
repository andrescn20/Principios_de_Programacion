temperatura = float(input('Introduzca la temperatura del paciente: '))

if( temperatura > 37 and temperatura < 42):
    print('El paciente tiene fiebre')
elif(temperatura < 30):
    print('El paciente se murio de frio')
elif(temperatura >= 42):
    print('El paciente se murio de calor')
else:
    print('El paciente no tiene fiebre')