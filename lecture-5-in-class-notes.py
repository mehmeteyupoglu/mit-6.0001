# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 09:54:28 2020

@author: Mehmet Eyüpoğlu
"""

# def factorial(n): 
#     if n == 1: 
#         return 1
#     elif n == 0: 
#         return 0
#     else: 
#         return n * factorial(n-1)
    
# b = factorial(5)
# c = factorial (3)

# print(b, c)
# print(factorial(5))

# def fact(n): 
#     if n == 1: 
#         return 1
#     elif n == 0: 
#         return 0
#     else: 
#         result = 1
#         while n > 0: 
#             result = result * n 
#             n -= 1
#             print("n is", n)
#     return result 
# print(fact(5))

def mult(a,b): 
    if b == 1: 
        return a
    else: 
        return a + mult(a, b-1)
    
print(mult(4,5))