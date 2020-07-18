# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:27:16 2020

@author: Mimoona Raheel
"""
print("Excercise 1:")
print("~~~~~~~~~~~~~~")

def stats(list1):
    print("max value is ", max(list1))
        
    print("min value is ",min(list1))
    
    print("length of the list is ",len(list1))

    print("sum of list is ",sum(list1))
   
    print("average value is ",sum(list1)/len(list1))
    
stats([3,11,18,20])

#%%

print("\nExcercise 2:")
print("~~~~~~~~~~~~~~")

def even_elements(list2):
    list_even = []
    for number in list2:
        if number%2 == 0:
            list_even.append(number)
            
    print(list_even)
    
# other way to do with list comprehension
#list_even= ["number" for number in list2 if number%2==0]
         

# call the function
even_elements([3,4,5,6,7,11,12,13,14])
        
#%%

print("\nExcercise 3:")
print("~~~~~~~~~~~~~~")

print("part 1")
print("~~~~~~~")

def list_benefits():

    list3 = ["More organized code","More readable code","Easier code re-use",
             "Allowing programmers to share and connect code together"]
    return list3
   
#call the function
my_list = list_benefits()
print(my_list)

print("\npart 2")
print("~~~~~~~")
def build_sentence(str1):
    final = (str1 + " is a benefit of functions!")
    return final

#call the function   
result = build_sentence("More organized code")
print(result)

print("\npart 3")
print("~~~~~~~")

def name_the_benefits_of_functions():
    
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
            print(build_sentence(benefit))

#call the function     
name_the_benefits_of_functions()
    

#%%

print("\nExcercise 4:")
print("~~~~~~~~~~~~~~")

def prime_check(number):
    
    # starting division check by 2  
    divisor = 2
    while divisor < number:
        if number%divisor == 0:
            return False
        divisor+=1
    return True

print(prime_check(int(input("Write a number: "))))

#%%

print("\nExcercise 5:")
print("~~~~~~~~~~~~~~")

def check_pal(user_word):
    word = user_word.lower().replace(" ","")
    if word == "":
        print("Empty word")
        return
    # used reversed method and convert to list otherwise it gives ids
    reverse_word = list(reversed(word))
    for i in range(len(word)):
        if word[i] != reverse_word[i]:
            print(user_word + " is not a palindrome !!!")
            return
    # in case  i = len(word)-1:
    print(user_word + " is a palindrome !!!")
            
check_pal(input("Enter a word: "))

#%%

print("\nExcercise 6:")
print("~~~~~~~~~~~~~~")

def factorial(n):
    if n==1:
        return n
    return n * factorial(n-1)

number = int(input("Enter a number: "))
answer = factorial(number)
print(str(number) + "! is" , answer)



