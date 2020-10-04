# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:54:25 2020

@author: Mehmet Eyüpoğlu
"""

"""

Guess the number between 0 and 100
"""
import random 

low = 0
high = 100
number_of_guesses = 0
guess = (low + high) // 2

random_num = random.randint(low, high)

while guess != random_num: 
    print("#"*20)
    print("low:", low)
    print("high:", high)
    print("guess:", guess)
    
    if guess < random_num: 
        low = guess
        guess = (low+high) // 2
        print('Guess is below the number. Therefore, low is updated')
    else: 
        print('Guess is above the number. Therefore, high is updated')
        high = guess
        guess = (low + high) // 2 
    print(" "*20)   
    number_of_guesses += 1 
    

print("The number is :", random_num, " and the number of guesses", number_of_guesses)
        
