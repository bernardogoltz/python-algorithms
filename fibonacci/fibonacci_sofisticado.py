# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:54:29 2022

@author: bernardogoltz
@title: Fibonacci Sofisticado. 

"""

def fibonacci(n):
    
    premissas = (0,1)
    # n(0) = 0
    # n(1) = 1
    
    if n < 0:
        return "Valor inválido."
    
    elif n in premissas:
        return n
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
"""
Testes que não quero deixar aparente no código, mas acho válido documentar. 

print(fibonacci(-1)) >>> invalido
print(fibonacci(0))  >>> 0 
print(fibonacci(1)) >>> 1+0 = 1 

"""

x = int(input("Quantos termos da sequência devem ser calculados?"))
for n in range(x):
    print("n({}) = {}".format(n,fibonacci(n)))