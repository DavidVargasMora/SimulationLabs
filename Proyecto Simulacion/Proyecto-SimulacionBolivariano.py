
# coding: utf-8

# In[54]:

# Test de Chi cuadrado contrastando los valores tomados junto con una distribucion exponencial
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.pylab import hist, show


def chicuadrado(k,param):
    data=[]
    suma=[]
    val=0.0
    arreglo=[0.53,2.45,3.42,0.41,0.52,3.20,0.39,0.45,0.42,0.34,1.05,2.08,0.34,2.16,2.19,0.58,3.50,1.08,1.25,4.05,3.30,0.33,0.55,0.48,1.35,0.48,1.20,0.56,1.03,3.10,4.06,2.06,1.24,1.22,2.50,0.53,1.30,0.46,2.02,1.51,0.39,3.22,0.40,0.38,1.14,1.03,0.54,2.48,1.06,1.07]

    acumula=0.0
    media=0.0 
    for p in range(len(arreglo)):
        acumula+=arreglo[p]
    media=acumula/len(arreglo)
    lamda=1/media
    print "lamda: ",lamda
    print "media: ",media
    punI=0.0
    ei=(len(arreglo)+0.0)/(k+0.0)
    p=(1+0.0)/(k+0.0)
    print "p: ",p
    puntosIni=[]
    for i in range(len(arreglo)):
        punI=0.0
        for j in range(k):
            puntosIni.append(round(punI,2))
            if(j<k-1):
                punF=calculaAi(lamda,(j+1),p)
            else:
                punF=1000000
            if arreglo[i]>punI and arreglo[i]<=punF:
                data.append(round(punI,2))
            punI=punF
    valFinal=0.0
    tot=0.0
    arregloHist=[]
    for n in range(k):
        valFinal+=(((data.count(puntosIni[n])-ei)**2)/ei)
        tot+=data.count(puntosIni[n])
        arregloHist.append(data.count(puntosIni[n]))
        print "cantidad para primer intervalo: ",data.count(puntosIni[n])
    print "valor Final: ",valFinal
    print "Cantidad de valores: ",tot
    plt.hist(arregloHist)
    plt.show()
    if(valFinal<=param):
        print "No se puede descartar que los datos se ajustan a una distribucion exponencial con lamda=",lamda
    else:
        print "Los datos no se ajustan a una distribucion exponencial"
def calculaAi(lamda,i,p):
    return ((-1+0.0)/(lamda+0.0))*math.log(1-((i*p)+0.0))

chicuadrado(182,212.3039)


# In[ ]:



