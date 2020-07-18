# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:24:43 2020

@author: Mimoona Raheel
"""

print("Excercise 1:")
print("~~~~~~~~~~~~")

# variable my_name is string because it contains characters
my_name='Mimoona'
print(type(my_name))

#variable my_age is integer.Usually when we talk about age its whole number. we don't say e.g 21.5    
my_age=25
print(type(my_age))

# price_of_breze is float.Price comes with decimal points
price_of_breze=0.99
print(type(price_of_breze))

#%%

print("\nExcercise 2:")
print("~~~~~~~~~~~~~~")

#1
price_3_books = float('5.0') * 3
print(price_3_books)
print(type(price_3_books))
print()

#2
my_age = 'I am ' + str(26)
print(my_age)
print(type(my_age))
print()

#3
total_bill = 4.45 + 3.30 + float(6) + float('7')
print(total_bill)
print(type(total_bill))

#total_bill = 4.45 + 3.30 + 6 + int('7')
#total_bill = 4.45 + 3.30 + 6 + float('7')
#total_bill = 4.45 + 3.30 + float(6) + int('7')

#%%

print("\nExercise 3:")
print("~~~~~~~~~~~~~")

year= 2020
#conversion to string
year= str(2020)
print(year,'is now of type: ',type(year))

#conversion to integer
year= int(2020)
print(year,'is now of type: ',type(year))

#conversion to float
year= float(2020)
print(year,'is now of type: ',type(year))