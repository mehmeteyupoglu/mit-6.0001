# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:55:59 2020

@author: Mehmet Eyüpoğlu
"""

def is_even(y): 
    return y % 2 == 0

print(is_even(6))

def even_or_odd(y): 
    for i in range(y+1): 
        if i % 2 == 0: 
            print(i, "Even")
        else: 
            print(i, "Odd")
    return ""     
print(even_or_odd(20))
