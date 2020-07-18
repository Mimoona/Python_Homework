# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 06:52:58 2020

@author: Mimoona Raheel
"""

print('Excercise: 1 and 2')
print("~~~~~~~~~~~~~~~~~")

class Rectangle:
    width = 0
    height = 0
    color = 'White'
        
    def set_dimensions(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        
    def set_color(self, new_color):
       self.color = new_color
        
    def info_printing(self):
        print('Width is:', self.width ,'|' ' Height is:', self.height,'|' ' Color is: ',self.color )
        
shape = Rectangle()
#print(shape.width,shape.height,shape.color)
shape.set_dimensions(7,5)
shape.set_color('Blue')
shape.info_printing()

#%%

print('Excercise: 3')
print("~~~~~~~~~~~~~")

class Rectangle:
    width = 0
    height = 0
    color = 'White'
    
    def __init__(self, new_width, new_height, new_color):
        self.width = new_width
        self.height = new_height
        self.color = new_color
        
   
    def info_printing(self):
        print('Width is:', self.width ,'|' ' Height is:', self.height,'|' ' Color is: ',self.color )
        
shape = Rectangle(10,7,'Green')
shape.info_printing()






