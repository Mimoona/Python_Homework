# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:48:32 2020

@author: Mimoona Raheel
"""

print('Excercise 1:')
print("~~~~~~~~~~~~~~")

log = open("excercise1.txt",'w')
for i in range(3):
  text = input("Enter a text:")
  log.write(text + "\n")

log.close()

# Instead of asking users to write 3 lines once, ask everytime if he want to write or stop
# Open the file for appending
log_1 = open("exercise1a.txt",'a')
text = input("Enter a text:")
log_1.write(text + "\n")
while True:
    choice = input("Do you want to add another line (y/n): ").lower()
    if choice == "y":
        text = input("Enter a text:")
        log_1.write(text + "\n")
    else:
        break

log_1.close()

#%%

print('\nExcercise2:')
print("~~~~~~~~~~~~~~")

# Create file, write line, count on number 4
my_file= open("My_File.txt",'w')
content = ("3\na\na\na\n5\n6\n7\nb\n4\n30\n40\nc\nb\n28\n4\n23\na\n4\n20")
my_file.write(content)
my_file.close()

my_file = open("My_File.txt",'r')

# Count lines in file
count_lines = 0

# Count on number 4 in file
count_number = 0

while True:
    #used strip function to remove '\n' from the file,otherwise it will show 0 result when search '4'
    content = my_file.readline().strip()
    #counter at wrong position
    #count_lines +=1
    if content == "":
        break
    elif content == "4":
        count_number +=1
    count_lines +=1
print("This file has {} times 4.".format(count_number))
print("This file has {} lines.".format(count_lines))
my_file.close()


 #%%

print("\nExcercise 3:")
print("~~~~~~~~~~~~~~")

fname1 = "File1.txt"
fname2 = "File2.txt"

# Creating first file
file_1 = open(fname1,'w')
text_1 = ("I\nProgramming\nPython")
file_1.write(text_1)
file_1.close()

# Creating second file
file_2 = open(fname2,'w')
text_2 = ("Love\nin\nLanguage")
file_2.write(text_2)
file_2.close()

file_1 = open(fname1,'r')
file_2 = open(fname2,'r')
while True:
    # read line at each iteration
    line1 = file_1.readline().strip()
    line2 = file_2.readline().strip()
    if line1=="":
        print("\n\nEnd of file reached")
        break
    else:
        # Combine lines from the two file, also remove '\n' at the end at print
        print(line1 + " " + line2, end = " ")

file_1.close()
file_2.close()


#%%
print("\nExcercise 4:")
print("~~~~~~~~~~~~~~")

csv_file = open("shopping_bill.txt",'r')
nitems = 0
tcost = 0
nline = 0

# Cheapest and most expensive item
icheap = 0
iexpensive = 0
# Initial standards for comparison of cheapest and most expensive 
vcheap = 10000.0
vexpensive = 0.0


while True:
  content = csv_file.readline().strip()
  nline += 1
  if content == "":
      break
  elif nline > 1:
      items = content.split(',')
      # print(items)
      nitems += int(items[1])
      tcost += int(items[1]) * float(items[2])
      if float(items[2])<vcheap:
          # updating cheapest item
          icheap = items
          # price of item becomes new standard
          vcheap = float(items[2])
      if float(items[2]) > vexpensive:
          # updating most expensive item
          iexpensive =items
          # price of item becomes new standard
          vexpensive = float(items[2])
csv_file.close()

print("Total number of items:",nitems)
print("Total bill:",tcost)
print("Cheapest item is",icheap[0],"; per unit price is",icheap[2])
print("Most expensive item is",iexpensive[0],"; per unit price is",iexpensive[2])

#%%
print("Excercise 5:")
print("~~~~~~~~~~~~~~")

grades_file = open("grades.csv",'r')
nline = 0
count = 0

st_name = []
st_grade = []
st_fail = []

# get relevant data from the grades file
while True:
    content = grades_file.readline().strip()
    nline += 1
    if content == "":
      break
    elif nline > 1:
      items = content.split(',')
      st_name.append(items[0])
      st_grade.append(items[2])
      st_fail.append(items[3].lower())
      count += 1 #counting students
grades_file.close()

# writing file with names of all students
names_file = open("students.txt",'w')
for i in range(count):
    names_file.write(st_name[i])
    names_file.write("\n")
names_file.close()

# writing file with names of students with A grade
Astud_file = open("A_students.txt",'w')
for i in range(count):
    if st_grade[i]=="A":
        Astud_file.write(st_name[i])
        Astud_file.write("\n")
Astud_file.close()

# writing file with names of students who will not be promoted
Fstud_file = open("see_you_next_year.txt",'w')
for i in range(count):
    if st_fail[i] != "promoted":
        Fstud_file.write(st_name[i])
        Fstud_file.write("\n")
Fstud_file.close()

print("All relevant files written !!!")
