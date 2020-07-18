# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:44:40 2020

@author: Mimoona Raheel
"""

print("Exercise 1: Fizz Buzz (again! But with a for loop)")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(1,100):
    if (i%3==0 and i%5==0):
        print('FizzBuzzz')
    elif (i%3)==0:
        print('Fizzz')
    elif(i%5)==0:
        print('Buzzz')
    else:
        print(i)
    i+=1

#%%
print("\nExercise 2:")
print("~~~~~~~~~~~~~")

print("multiples of 5:")
for i in range (5,105,5):
    print(i)
    
print("mutiple of 5 backward")
for i in range (100,0,-5):
    print(i)
    

#%%

print("\nExercise 3:") 
print("~~~~~~~~~~~~~")

numbers = [54, 23, 11, 3, 20, 7]
sum = 0
for num in numbers:
    sum += num
print(f" The sum of numbers in the list is",sum)

#%%

print("\nExercise 4:")
print("~~~~~~~~~~~~~")
numbers = {2, 56, 4, 29, 7}

#convert set to list and assume at index '0' the value is highest
big_num = list(numbers)[0]

for num in numbers:
    if num > big_num:
        big_num = num
print(f'highest number is ',big_num)
    

#%%

print('\nExcercise 5:')
print("~~~~~~~~~~~~")

list=['abc', 4, 3.2, [19, 1, 23], '12', 2, 2, 1.0, 3]
new_list= []

for i in list:
  if type(i) == int:
    new_list.append(i*i)
print('output =',new_list)

#%%

print("\nExcercise 5: (with List Comprehension )")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
new_list=[i*i for i in list if type(i)==int]
print(new_list)

#%%

print('\nExcercise 6: Scrabble Score')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
score={"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
       "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
       "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
       "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
       "x": 8, "z": 10, " ":0}
       
word =input('Enter a word: ')
word = word.lower()
sum = 0
for char in word:
  sum += score[char]
print('Scrabble Score:', sum)
