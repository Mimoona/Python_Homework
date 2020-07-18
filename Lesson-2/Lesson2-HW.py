# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:24:43 2020

@author: Mimoona Raheel
"""

print("Excercise 1:")
print("~~~~~~~~~~~~~")
#assumed a course of 15 weeks
weeks=15
classes_week=2
hours_class=2
hours_home = 2*7
hour_per_week = classes_week*hours_class + hours_home
total_hours=weeks*hour_per_week
print(f"we will spend {total_hours} hours learning Python")

#%%

print("\nExcercise 2: Phone bill send to customer")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# assumed cost per minute=.25
cost_per_unit=0.25
#assumed minutes consumed
minutes_consumed=1000
# total cost
invoiced= cost_per_unit*minutes_consumed
# 10% discount
invoiced=invoiced-(10/100)*invoiced
# payment made by customer
recieved=90
# amount outstanding
outstanding=invoiced-recieved

text=("Dear customer, your invoice of {} is due. {} is the last date to pay your bill. Please contact us at {}.\nDetails are below:\n   Total invoiced= {}\n   Recieved= {}\n   outstanding= {}")
print(text.format(outstanding,"15.04.2020","00491234567",invoiced,recieved,outstanding))

#%%

print("\nExcercise 3:")
print("~~~~~~~~~~~~")
number1=55
number2=13
result= number1-number2
print('The difference is :',result)
#another way:
#print('The difference is :',55-13)

#%%

print("\nExcercise 4:")
print("~~~~~~~~~~~~~")
print(10-4+0.5*(-3)/2)
