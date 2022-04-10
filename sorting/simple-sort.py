# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 11:33:49 2022

@author: bernardogoltz
"""

import numpy as np 

np.random.seed(10)
elementos = np.random.randint(10,100,100)

maior = 0 

for i in range(len(elementos)):
    if elementos[i] > elementos[maior]:
        maior = i
    
print("O maior é o indice {}, que é {}".format(maior,elementos[maior]))

