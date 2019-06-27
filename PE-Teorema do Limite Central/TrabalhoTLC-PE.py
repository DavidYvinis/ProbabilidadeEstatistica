# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
#from statistic import *
from scipy import stats
import random
import matplotlib.pyplot as plt
import numpy as np

ls = []
xs = []
w = 0
#quanto mais repetições, mais o grafico fica em formato de sino
for rep in range(10):
    y = 0
    z = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
        w = w + x 
    
    
    z = y / 10
   #print("Y vale:", y)
   #print("A media é:", z)
    
    
    ls.append(y)
    xs.insert(rep, y)
      
#quando se tem um n impar de elementos, a mediana é o elemento do meio
#quando se tem um n par de elementos, somamos os dois do meio e dividimos por 2
#colocar os dois elementos centrais da lista de acordo com a qtd de rep
#median = (xs[x]+xs[x+1])/2
#media é a soma total dos elementos divido pela quantida de amostras
#media = w / k
#moda é o numero que se repete mais vezes dentro da amostra

media = np.mean(xs)
mediana = np.median(xs)
moda = stats.mode(xs)

#print("Elementos da Lista XS :", xs)    
print("O total é:", w)
print("A media amostral é:", media)
print("A mediana é:", mediana)
print("A moda é:", moda)


plt.hist(ls, bins=(40));

