#Assignment 1:
#assumed a course of 15 weeks
weeks=15
classes=2
hours_class=2
total_hours=weeks*classes*hours_class
print(f"we will spend {total_hours} hours learning Python")



#Assignment 2:phone bill send to customer

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



#Assignment 3:
number1=55
number2=13
result= number1-number2
print('The difference is :',result)
#another way:
#print('The difference is :',55-13)


#Assignment4:
print(10-4+0.5*(-3)/2)
