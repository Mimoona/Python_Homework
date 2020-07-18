# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:08:35 2020

@author: Mimoona Raheel
"""
print("\nExercise 1: Healthy Food Check")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

fruits=["apple","banana","mango","pineapple"]
vegetables=["cucumber","tomato","spinach","potato"]
info=input("write a food: ")

if info not in fruits and info not in vegetables:
  print('its unhealthy food.Dont eat it')
else:
    print('you can eat it.it\'s healthy')
    
 #%%
 
print("\nExcercise 2: Encyclopedia")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

dictionary = {'India':'New Delhi',
              'United Kingdom':'London',
              'Germany':'Berlin',
              'Nigeria':'Abuja',
              'France':'Paris' }
user_value = input('Pick a country: ')
user_value = user_value.title()
if user_value in dictionary:
        output = dictionary[user_value]
        print(f'The capital city of {user_value} is',output)
else:
    print('sorry, i don\'t know the capital of',user_value)

#%%   
 
print("\nExercise 3: Calculator")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

possible_operations = ["sum", "difference", "multiplication", "division"]
print(possible_operations)

user_choice = input('Which operation would you like to do? ')
while user_choice != "close":
  if user_choice in possible_operations:
    a = int(input('what\'s the first number? '))
    b = int(input('what\'s the second number? '))
    if user_choice == possible_operations[0]:
      result = a + b
      print('The sum is: ',result)
    elif user_choice == possible_operations[1]:
      result = a - b
      print('The difference is: ',result)
    elif user_choice == possible_operations[2]:
      result = a * b
      print('The multiplication result is: ',result)
    elif user_choice == possible_operations[3]:
      result = a / b
      print('Result of division is: ',round(result,2))
  else:
     print('This operation is not available')
  user_choice = input('Which operation would you like to do? ')      
      
print('Thank you!')

#%%

print("\nExcercise 4: Fizz Buzz")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

i=1
while i <= 100:
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

print("\nExercise 5: Guess my number between 0-20")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

from random import randint
#generate random number
random_num = randint(0,20)
#print(random_num)

# user have chances
no_of_guess= 3

#execute the loop 3 times
while no_of_guess > 0: 
    guess_num = int(input('Enter a number: '))
    
    if guess_num > random_num:
        print('wrong guess, Go lower')
    elif guess_num< random_num:
            print('wrong guess, Go higher')
    elif guess_num == random_num:
        print('Congratulations your guess is right')
        #if user guess right before getting out of attempts just exit the loop
        break
    no_of_guess -=1
else:   
    print('out of attempts, try next time')
 
 #%%   
 
print("\nExercise 5: Guess my number between 0-20 (another way)")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

from random import randint
#generate random number
random_num = randint(0,20)
#print(random_num)

guess_num = int(input('Enter a number: '))

#execute loop infinitely
while random_num != guess_num: 
    if guess_num > random_num:
        print('wrong guess, Go lower')
    elif guess_num< random_num:
            print('wrong guess, Go higher')
            
    guess_num = int(input('Enter a number: '))   
print('Congratulations your guess is right')


                           