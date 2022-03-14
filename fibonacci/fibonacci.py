
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:44:30 2022
@author: bernardogoltz
@title: Sequência de Fibonacci

@description: 
    > Começa em 0 e 1
    > O n+1 é a soma dos 2 antecessores. 
        n0 = 0 
        n1 = 1
        n2 = 1+0 = 0  
        n3= n2+n1
"""

def Fibonacci(n):
    a = 0 
    b = 1

# passos que tratam o tamanho de n, para que a sequência
# seja do tamanho adequado. 

    if n < 0:
        print("[n = {}]".format(n))
        return "[Erro] - A sequência usa somente inteiros positivos"
        # tipagem dinâmica, permite retornar uma string. 
        
    elif n == 0: 
        print("[n = {}]".format(n))
        return a 
    
    elif n == 1:
        # n = 1
        # É premissa da sequência de fibonacci que: n(1) = 1
        # Sabe-se que, no algoritmo b = 1 
        # Se (n == 1) , então,  n = 1
        print("[n = {}]".format(n))
        return b
    
    # A sequência para valores mais interessantes:
        
    else: # else -> positivos maiores que 1.
        print("[n = {}]".format(n))
        for index in range(1,n):  
            c = a + b
            a = b
            b = c 
        return b 
        
x = int(input("Sequência de Fibonacci pra quantos números? "))
y = Fibonacci(x)
print(y)