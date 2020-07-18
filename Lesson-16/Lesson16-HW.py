# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:53:20 2020

@author: Mimoona Raheel
"""

print('Welcome to Bank')

class Bank_Account:
   
    
    def __init__(self,user_name):
        self.name = user_name
        self.balance = 0
        
        
    def deposit(self, amount_in):
        print('\n------- Account:',self.name,'------')
        self.balance += amount_in 
        print(f'You have successfully deposited {amount_in} amount')
    
    
    def withdraw(self,amount_out):
        print('\n --------Account:',self.name,'---------')
        self.balance -= amount_out 
        print(f'Your remaiming balance is:{self.balance} ')

    
class MinimumBalance_Account(Bank_Account):
    
    
    def __init__(self,name,limit):
        super().__init__(name)
        self.limit = limit
        
    def withdraw(self,amount_out):
        print('\n------Account:',self.name,'-------')
        temp = self.balance-amount_out
        if  temp <= self.limit:
            print('Sorry, You have insufficient balance.')
                
        else:
            self.balance -= amount_out 
            print(f'{amount_out} withdrawn successfully,Your remaiming balance is:{self.balance}.')
            
                
    
#a = Bank_Account('Mr.A')
#b = Bank_Account('Mr.B')
c = MinimumBalance_Account('Mr.A',100)
d = MinimumBalance_Account('Mr.B',150)


c.deposit(1000)
c.withdraw(200)

d.deposit(900)
d.withdraw(800)  
    
  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    