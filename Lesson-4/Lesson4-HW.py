# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:38:27 2020

@author: Mimoona Raheel
"""
print("Retirement Plan")
print("~~~~~~~~~~~~~~~~")

#calculate savings by the age of retirement

# Take inputs from user
name=input('Please enter your name:').title() 
birth_year=int(input('Please enter the year you were born:'))

#converting salary to float for calculations
net_salary=float(input('Please enter your salary per month:'))

#converting rent to float for calculations
rent_per_month=float(input('Please enter how much you pay for rent per month:'))

#converting living cost to float for calculations
livig_cost_per_month=float(input('Please enter how much you give out per month:'))

saving_percent_remaining=float(input('Please enter how much percent of your remaining salary you want to save:'))

retirement_age=int(input('Please enter the age of retirement in your country:'))


# here calculations begin:
current_year=2020

# subtracting two variables to get current age
current_age=current_year-birth_year

#subtracting to get years left in retirement 
years_left_retirement=retirement_age-current_age 

# subtracting expenses from salary to get remaining
remaining_salary=net_salary-rent_per_month-livig_cost_per_month 

#calculated saving amount by applying % of remaining salary 
savings_of_remaining=remaining_salary*(saving_percent_remaining/100)
per_year_saving=savings_of_remaining*12

# calculated savings at the age of retirement he will get
savings_by_retirement=per_year_saving*years_left_retirement

total_rent=rent_per_month*12*years_left_retirement
total_living_cost=livig_cost_per_month*12*years_left_retirement


text=('\nThank you {} for your input! Based on the data you provided, by the age of {} your saving will be {} euros.\nYou have {} years ahead to work. During these years you will be paying:\n\t- {} euro for rent in total\n\t- {} euro for basic need in total\n I hope you\'re satisfied with your savings :)')

print(text.format(name,retirement_age,savings_by_retirement,years_left_retirement,total_rent,total_living_cost))






