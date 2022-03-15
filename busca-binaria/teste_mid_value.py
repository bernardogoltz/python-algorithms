# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:35:58 2022

@author: bernardogoltz
@title: bninary search
"""


import numpy as np
# testando um módulo de código

A = list(np.random.randn(10).round(2))
A = np.sort(A) 

tamanho = len(A)
 # print("o vetor tem {:d} posições".format(tamanho))

# range(tamanho) = um vetor de numeros inteiros que vai de 0 ao tamanho da lista

"""
for i in range(tamanho):
    print("{} : {}".format(i,A[i]))
"""

for i in range(tamanho):
    mid  = int(tamanho/2)
    
    if i == mid:    
        print("{} item do meio, valor = {}".format(i,A[i]))
    else: 
        print(i)