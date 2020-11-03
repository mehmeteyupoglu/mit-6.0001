# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 09:54:28 2020

@author: Mehmet Eyüpoğlu
"""
"""
Python Classes and Inheritance
"""

class Animal(object): 
    def __init__(self, age): 
        self.age = age
        self.name = None
    def __str__(self): 
        return "Animal: " + str(self.name) + ", " + str(self.age) + " ages."
    
myAnimal = Animal(7)

class Cat(Animal): 
    def speak(self): 
        print("Meow")
    def __str__(self): 
        return "Cat: " + str(self.name) + ", " + str(self.age) + " ages."
    
little_cat = Cat(10)
print(little_cat)
little_cat.speak()