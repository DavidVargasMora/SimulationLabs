
# coding: utf-8

# In[3]:

# Test de Chi cuadrado contrastando los valores tomados junto con una distribucion exponencial
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.pylab import hist, show


def chicuadrado(k,param):
    data=[]  #Arreglo utilizado para el conteo de valores que estan contenidos en un determinado intervalo (bean)
    val=0.0
    arreglo=[1.56,0.25,1.55,2.02,0.45,0.53,1.24,0.53,1.05,2.5,0.39,2.37,2.52,0.57,0.40,0.35,1.13,1.21,0.42,0.43,1.41,1.03,0.51,0.29,1.39,1.16,0.52,3.11,3.29,0.35,0.42,1.14,1.10,1.22,1.16,2.3,2.42,1.2,1.05,0.38,0.45,2.32,1.19]
     #En este arreglo es donde se almacenan los tiempos de servicio en formato minutos.segundos
    acumula=0.0
    media=0.0 
    for p in range(len(arreglo)):
        acumula+=arreglo[p]      
    media=acumula/len(arreglo)   
    lamda=1/media
    print "lamda: ",lamda
    print "media: ",(1/lamda)   #Se calcula la media de la distribucion exponencial como 1/lambda
    punI=0.0
    ei=(len(arreglo)+0.0)/(k+0.0) #Se calcula el valor esperado de la districion como el numero de datos que existen en el arreglo sonbre el numero de beans
    
    p=(1+0.0)/(k+0.0)   #Se calcula la probabilidad de cada bean , considerando que todos los beans son equiprobables
    print "p: ",p
    puntosIni=[]   #Arreglo utilizado para recorrer el vector que almacena los datos que caen en un bean
    for i in range(len(arreglo)): #Bucle para recorrer cada dato del vector de tiempos
        punI=0.0
        for j in range(k):   # Bucle para recorrer los intervalos posibles (beans) en el que podria contener el dato
            puntosIni.append(round(punI,3)) #Almacenas las posiciones iniciales de cada rango (bean)
            if(j<k-1):     #Condicion utilizada para saber si esta en el ultimo bean, ya que el ultimo valor ai limite debe ser un numero muy grande (infinito)
                punF=calculaAi(lamda,(j+1),p)
            else:
                punF=1000000    #Valor grande que tiende a infinito
            if arreglo[i]>punI and arreglo[i]<=punF:  #Condicion que evalua el bean al que corresponde el tiempo 
                data.append(round(punI,3))    #Almacena las posiciones iniciales para despues ser recorrido por el metodo Count() y contar todas las posiciones iniciales que coincidan en el arreglo
            punI=punF
    valFinal=0.0
    tot=0.0
    arregloHist=[]  #Arreglo utilizado para generar el histograma
    for n in range(k):  
        valFinal+=(((data.count(puntosIni[n])-ei)**2)/ei)   #Calcula el valor del test de chi cuadrado
        tot+=data.count(puntosIni[n])
        arregloHist.append(data.count(puntosIni[n]))
        print "cantidad para primer intervalo: ",data.count(puntosIni[n])
    print "valor Chi cuadrado: ",valFinal
    plt.hist(arregloHist)
    plt.show()
   
    if(valFinal<=param):   #Evalua si dicho valor es menor que el de la tabla de chi cuadrado con un error del 5 % y 180 grados de libertad
        print "No se puede descartar que los datos se ajustan a una distribucion exponencial con lamda=",lamda
    else:
        print "Los datos no se ajustan a una distribucion exponencial"
def calculaAi(lamda,i,p):   #Metodo que calcula los ai (valores extremos) de cada bean. Esto por medio del despeje matematica de la funcion de distribucion acumulada
    return ((-1+0.0)/(lamda+0.0))*math.log(1-((i*p)+0.0))

chicuadrado(182,212.3039)


# In[ ]:



