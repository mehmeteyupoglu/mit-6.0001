# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:41:28 2020

@author: Mehmet Eyüpoğlu
"""

# cube = 8

# for guess in range(abs(cube + 1)):
#     if guess**3 >= abs(cube): 
#         break
# if guess**3 != abs(cube): 
#     print(cube, "is not a perfect cube")
# else: 
#     if cube < 0: 
#         guess = -guess
#     print("Cube root of '+str(cube)+' is '+str(guess)' " )

# print(len("Hello World!"))
# print("Hello World!"[0])
# print("Hello World!"[-2])

# cube = 8

# for guess in range(abs(cube+1)):
#     if guess ** 3 == cube: 
#         print("Cube: ")

# name = "Mehmet"

# for i in range((len(name))): 
    
#     space = " "
#     print(space*i, name[i])

#######GUESS-AND-CHECK-CUBE-ROOT-EXERCISE#######
cube = 16

for guess in range(cube+1): 
    if guess**3 == cube: 
        print("Cube root of", cube, "is", guess)