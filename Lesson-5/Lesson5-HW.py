# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:43:25 2020

@author: Mimoona Raheel
"""
print("Excercise:1")
print("~~~~~~~~~~~")
# Part(a)

a = 'hello world'
#endswith function checks if the string 'a' is ending with the word 'world'and save the result in variable 'output'.it returns true
output=a.endswith('world')
print(output)

# it returns false because 'Python' does not match with 'Python is easy'
string1="I am learning Python"
string2="Python is easy"
output=string1.endswith(string2)
print(output)

# Part(b) 

#it returns false
output=a.startswith("world")
print(output)

# it returns true because both strings starts with Python
string1="Python is easy ."
string2="Python "
output=string1.startswith(string2)
print(output)

#%%

print("\nExercise:2")
print("~~~~~~~~~~")

str1 = "I LOVE PYTHON"
# converts the string to lowercase
print(str1.lower())

str1="i love python"
#converts the string to uppercase
print(str1.upper())

str1="I Love Python"
# converts the string lower to upper or upper to lower
print(str1.swapcase()) 