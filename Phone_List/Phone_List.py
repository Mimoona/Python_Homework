# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:58:36 2020

@author: ReDI
"""

###########################################################################
##
##                            Phone List
##
###########################################################################


phone_numbers = {'Peter': '+49 1234567', 'Eva': '+49 9863456'}
possible_countries = {
    "germany": "+49",
    "france": "+33",
    "spain": "+34",
    "greece": "+30",
    "pakistan": "+92"
}


def valid_prefix(prefix):
    valid = False
    #print(valid)
    # TODO: check if prefix
    # 1. Starts with "+"
    # 2. Has two characters following the "+" sign (you only need to chek if the string has in total 3 characters)
    if len(prefix) == 3 and prefix[0] == '+':
        valid = True
            
    return valid


def valid_number(number):
    valid = True
    # TODO: check if number has 7 digits (you should check if all characters are valid numbers 0-9)
    valid_numbers = ['0','1','2','3','4','5','6','7','8','9']
    if len(number) == 7 :
        for i in number:
            if i not in valid_numbers:
                valid = False
                break
    else: 
        valid = False
    return valid


def check_country(country):
    valid = False
    if country not in possible_countries:
        print('Country not recognized')  
        return valid
    else:
        valid = True
    return valid


# Main Code:
    
user_name = ''
while True:
    print('\n-----------Welcome------------')
    user_name = input('Please enter your name: ').title()
    if user_name =='Stop':
        break
    # Below are the lines related to Task 2, later changed the program asking country instead of prefix
    #prefix = input('Enter the country code: ')
    #while valid_prefix(prefix)==False:
        #prefix = input('Enter the country code again(e.g +23): ')
        
    country = input('Enter country: ').lower() 
    
    # Here prefix get the value TRUE or FALSE from function
    prefix = check_country(country)
    
    # If country name does not exist in list then start from begining
    if prefix == False:
        continue
    else:
        # variable 'prefix' name didn't change because its working with previous tasks
        # Here 'prefix' get the value (country code) from dictionary 
        prefix = possible_countries[country]   
        
    phone_number = input('Your phone number: ')
    while valid_number(phone_number) == False:
        phone_number = input('Enter a valid 7 digit number: ') 

    
    complete_number = prefix +' '+ phone_number
    phone_numbers[user_name] = complete_number

    print(phone_numbers)


number_file = open("numbers.txt",'w')
content = str(phone_numbers)
number_file.write(content)
number_file.close()


