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
guess = int(input("Enter a number between 1 and 100: "))

random_num = random.randint(low, high)

while guess != random_num: 
    print("#"*20)
    print("guess:", guess)
    
    if guess < random_num: 
        guess = int(input("Your guess is low. Try a higher number: "))
    else: 
        guess = int(input("Your guess is high. Try a lower number: "))
        
       
    number_of_guesses += 1 
    

print("The number is :", random_num, " and the number of guesses", number_of_guesses)
        
