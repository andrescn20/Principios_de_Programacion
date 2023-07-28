
# importing the required module
import matplotlib.pyplot as plt
import datetime 

bitacora = open('bitacora_hormigas.txt' , 'w')
bitacora.write('------------------------------------\n')
fecha = datetime.datetime.now()
bitacora.write(f'Fecha de Estudio: {fecha}\n')


##Definimos los meses que se van a estudiar y la población al inicio del estudio
meses_de_estudio = int(input('Ingrese la cantidad de meses a estudiar: '))
poblacion_inicial = int(input('Ingrese la poblacion actual: '))

bitacora.write(f'Meses de estudio: {meses_de_estudio}\n')
bitacora.write(f'Poblacion al inicio del estudio: {poblacion_inicial}\n')


##Para los ejes:
x = []
y = []

##La población final de cada mes es al mismo tiempo la inicial del siguiente
poblacion_final = poblacion_inicial

## Definimos un ciclo que simila los meses transcurridos
for mes in range(1, meses_de_estudio+1):
 ##Definimos las reglas del ciclo de vida de las hormigas

    ##La tasa de crecimiento regular es de 40%
    tasa_de_crecimiento = 1.40
    ##Si hay sobrpoblación (> 28000), la tasa se redefine en 31%
    if(poblacion_final > 28000):
        tasa_de_crecimiento = 1.31
    
    ##Todos los meses, la población crece en el % determinado
    poblacion_final = poblacion_final*tasa_de_crecimiento

    ##Todos los meses, el oso hormiguero se come 7000 hormigas
    if(poblacion_final <= 7000):
        ##Si hay menos de 7000, entonces se las come todas. 
        poblacion_final = 0
    elif(poblacion_final > 7000): 
        poblacion_final = poblacion_final - 7000
    x.append(mes)
    y.append(round(poblacion_final))

poblacion_final = round(poblacion_final)

bitacora.write(f'Poblacion al final del estudio: {poblacion_final}\n')

bitacora.write(f'Datos ejes coordenados de grafica de Poblacion\n')
bitacora.write(f'Eje x: {x} \n')
bitacora.write(f'Eje y: {y}\n')
bitacora.write('FIN DEL ESTUDIO\n')

# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('Meses')
# naming the y axis
plt.ylabel('Población')
  
# giving a title to my graph
plt.title('Población Mensual de Hormigas')
  
# function to show the plot
# plt.show()
plt.savefig("hormigas.jpg")

bitacora.close()
