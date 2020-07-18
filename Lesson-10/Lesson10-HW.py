# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:34:09 2020

@author: Mimoona Raheel
"""
print('Excercise 1: Accept or reject the user name')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

users_list = ["Ahmed","Yong","Sudhir","Julie"]
user_name = input('Enter your name: ').title()

if user_name in users_list:
    print('Welcome', user_name)
else:
    print('Sorry your name not found')
    
    
#%%

print('\nExcercise 2:Keep trying until name found in list')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

users_list = ["Ahmed","Yong","Sudhir","Julie"]
user_name = input('Enter your name: ').title()

while user_name not in users_list:
    print('Sorry your name not found, please try again')
    user_name = input('Enter your name: ').title()
else:
    print('Welcome', user_name)
    
    
    #%%
    
print('\nExcercise 3:Accept or reject password')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

users_list = ["Ahmed","Yong","Sudhir","Julie"]
passwords = {"Ahmed":"a123",
              "Yong": "b123",
              "Sudhir":"c123",
              "Julie":"d123"}

user_name = input('Enter your name: ').title()

while user_name not in users_list:
    print('Sorry your name not found, please try again')
    user_name = input('Enter your name: ').title()
else:    
    print('Welcome', user_name)
    user_pswd = input('Please enter your password: ')
    
    if user_pswd == passwords[user_name]:
        print('Welcome! you have entered the correct password ')
    else:
        print('Wrong Password')
     

  #%%          

print('\nExcercise 4:')
print("~~~~~~~~~~~~~~")

passwords = {"Ahmed":"a123",
              "Yong": "b123",
              "Sudhir":"c123",
              "Julie":"d123"}

blocked_list=[]


# Infinite loop
while True:
    print('-----------New Session-----------')
    user_name = input('Enter your name: ').title()
    
    # Get correct username
    
    while user_name not in passwords:
        user_name = input('Sorry your name not found, please try again: ').title()
        
        if user_name in blocked_list:
            print('Sorry, Your account has been blocked temporary')
            continue
    else:
        print('Welcome', user_name)
    
    # Check for correct password
    count = 3
    while True:
        user_pswd = input('Please enter your password: ')
        count-=1
        if user_pswd != passwords[user_name]:
            print("Sorry, wrong password.")
        
            # Block account after tries
            if count == 0:
                blocked_list.append(user_name)
                print('\nSorry, your account has been blocked')
                break
        else:
            print('Welcome! you have entered the correct password ')
            break

            
            
    
    
    






