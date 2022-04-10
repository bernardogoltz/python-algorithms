# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 00:08:52 2022

@title: Bubble Sort
@author: bernardogoltz

"""

def bubble_sort(unlist):
    
    n = len(unlist)
    
    for j in range(n-1):
        for i in range(n-1):
        
            if unlist[i] > unlist[i+1]:
                unlist[i] , unlist[i+1] = unlist[i+1] , unlist[i]
            
test_list = [4,5,1,2,46,7,1]
bubble_sort(test_list)

    
