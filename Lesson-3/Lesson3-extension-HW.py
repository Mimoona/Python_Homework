# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:18:35 2020

@author: Mimoona Raheel
"""

import random
import math

print("Excercise 1:")
print("~~~~~~~~~~~")

water=500
each_container=37
number_containers=water//each_container
print('Number of Containers =',number_containers)
water_wasted=water%each_container
print('Total water wasted =',water_wasted)

#%%

print("\nExcercise 2:")
print("~~~~~~~~~~~~")

# generate random number
num=random.randint(0,100)
print(f"random number is:",num)
print("random number divided by 2 is {}".format(num/2))
print("The difference between random number power two and the number is", num**2 - num)

#%%

print("Excercise 3:")
print("~~~~~~~~~~~~")

# Quadratic formula
a=1 
b=-9 
c=8 
solve_root=(b**2)-(4*a*c) 

solve_root=math.sqrt(solve_root) 

root_x1=(-b+solve_root)/(2*a)  

print('The value of x1=', root_x1 ) 

root_x2=(-b-solve_root)/(2*a) 

print ('The value of x2=', root_x2) 

#check 

x=root_x1 

print('with root_x1, we get:', x**2-9*x+8 ) 

x=root_x2 

print('with root_x2, we get:', x**2-9*x+8 ) 