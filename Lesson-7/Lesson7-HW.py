# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:51:08 2020

@author: Mimoona Raheel
"""

print("Exercise 1:")
print("~~~~~~~~~~~")
number_1=input('Please enter a number:')
number_2=input('Please enter another number:')

if number_1 > number_2:
  print(f'{number_1} is bigger than {number_2}.')
else:
  print(f'{number_2} is bigger than {number_1}.')

#%%

print("\nExercise:2")
print("~~~~~~~~~~~~")

number=int(input('Please enter a number:'))
if (number%2) == 0:
  print(f'Number {number} you have entered is an even.')
else:
  print(f'Number {number} you have entered is an odd.')

#%%

print("\nExercise 3:")
print("~~~~~~~~~~~~~")

name = input('What is your First Name? ')
surname = input(f'{name} please write your surname. ')
if name[0] == surname[0]:
  print(f'Hello {name} {surname}, your first name and surname starts with the same letter.')
else:
  print(f'Hello {name} {surname}, your first name and surname doesn\'t start with the same letter.')

#%%

print("\nExercise:4")
print("~~~~~~~~~~~~")

length_name = len(name)
length_surname = len(surname)
total_letters = length_name+length_surname
print('Printing the count of characters in user name')
print(total_letters)
if (total_letters%3 == 0):
  print(f'Your full name has {total_letters} characters and it is divisible by 3')
else:
  print(f'Your full name has {total_letters} characters and it is not divisible by 3')

#%%

print("\nExercise:5")
print("~~~~~~~~~~~~~")

print('Let see if your name has even number of characters.')
if (length_name%2 == 0 and length_surname%2 == 0):
  print('Total number of characters in your full name is even')
else:
  print('Total number of characters in your full name is odd')
	