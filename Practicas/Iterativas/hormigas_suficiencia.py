
import matplotlib.pyplot as plt
import datetime 

##El código que se muestra a continuación representa el comportamiento de la población
# de hormigas en una isla. Considera la razón a la que crecen y además el efecto que 
# que tiene en la población la presencia de un oso hormiguero que las depreda. 

    
bitacora = open(f'bitacora.txt' , 'w')

def generar_bitacora(poblacion, eje_x, eje_y):
    bitacora.write(f'Poblacion al final del estudio: {poblacion}\n')
    bitacora.write(f'Datos ejes coordenados de grafica de Poblacion\n')
    bitacora.write(f'Eje x: {eje_x} \n')
    bitacora.write(f'Eje y: {eje_y}\n')
    bitacora.write('FIN DEL ESTUDIO\n')

bitacora.write('------------------------------------\n')
fecha = datetime.datetime.now()
bitacora.write(f'Fecha de Estudio: {fecha}\n')
meses_de_estudio = int(input('Ingrese la cantidad de meses a estudiar: '))
poblacion_inicial = int(input('Ingrese la poblacion actual: '))
bitacora.write(f'Meses de estudio: {meses_de_estudio}\n')
bitacora.write(f'Poblacion al inicio del estudio: {poblacion_inicial}\n')
x = []
y = []
perezoso_mes = 7000
poblacion_final = poblacion_inicial
for mes in range(1, meses_de_estudio+1):
    tasa_de_crecimiento = 1.40
    if(poblacion_final > 28000):
        tasa_de_crecimiento = 1.31
    poblacion_final = poblacion_final*tasa_de_crecimiento
    if(poblacion_final <= perezoso_mes):
        poblacion_final = 0
    elif(poblacion_final > perezoso_mes): 
        poblacion_final = poblacion_final - perezoso_mes
    x.append(mes)
    y.append(round(poblacion_final))
poblacion_final = round(poblacion_final)

generar_bitacora(poblacion_final,x, y)

#Estos son métodos de la libreria importada, no es necesario que de
# una explicación de estas líneas
##INICIO METODOS LIBRERIA
# plotting the points 
plt.plot(x, y)
# naming the x axis
plt.xlabel('Meses')
# naming the y axis
plt.ylabel('Población')  
# giving a title to my graph
plt.title('Población Mensual de Hormigas') 
plt.savefig("grafico_hormigas.jpg")
## FIN METODOS LIBRERIA
bitacora.close()