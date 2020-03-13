#BucketSort
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import sys

sys.setrecursionlimit(10**9)
lista=[]
tamanhos=[15000,25000,35000,45000,55000]
tempos=[]
def geraLista(tamanho):
  x=[]
  for i in range(tamanho): x.append(i)
  random.shuffle(x)
  return x

def geraListaPiorCaso(tamanho):
  x=[]
  for i in range(tamanho,0,-1):
    x.append(i)
  return x

def bucketsort(lista):
    comprimento = len(lista)
    cesta = [[] for _ in range(comprimento)]
    maior = max(lista)
    tamanho = maior/comprimento

    for i in range(comprimento):
        j = int(lista[i] / tamanho)
        if j != comprimento:
            cesta[j].append(lista[i])
        else:
            cesta[comprimento - 1].append(lista[i])

    for i in range(comprimento):
        insertionsort(cesta[i])

    lista_ordenada = []
    for i in range(comprimento):
        lista_ordenada = lista_ordenada + cesta[i]

    return lista_ordenada


def insertionsort(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and atual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual

for i in tamanhos:
  print("comecei")
  lista=geraLista(i)
  #lista=geraListaPiorCaso(i)
  #print("terminei")
  print("comecei dnv")
  now=time.time()
  lista=bucketsort(lista)
  then=time.time()
  #print(lista)
  print("acabei dnv")
  tempos.append(then-now)
# Plot the data
plt.plot(tamanhos,tempos)
print(tempos)
# Show the plot
plt.show()
