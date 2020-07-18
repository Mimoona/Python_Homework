
"""
Created on Wed Jun 10 10:19:24 2020

@author: Mimoona
"""

# -----------------------------------
# Homework lesson 15
#------------------------------------

# Homework class
class Homework:
    

    def __init__(self,title):
        self.title = title
        self.count_students = 0
        self.count_done = 0
        
    
    def status(self):
        print('current status\n--------------')
        print('Undone: ',self.count_students-self.count_done)
        print('Done: ',self.count_done)
        print()
                
        
# Student class
class Student:
    
    def __init__(self, new_id, student_name):
        self.student_id = new_id
        self.name = student_name
        self.grade = ''
        
   
    def finnish_homework(self,homework):
        print('{} has finished {}'.format(self.name,homework.title))
        print()
        homework.count_done += 1
        
        
    def show_grade(self):
        print('{} got {} grade!'.format(self.name,self.grade))
        

# Teacher class
class Teacher:
    
    def __init__(self,teacher_name):
        self.name = teacher_name
        self.students = []
    
    
    def create_homework(self, title):
        home_work = Homework(title) 
        return home_work
        
    
    def assign_student(self, student):
        if student not in (self.students):  
            self.students.append(student)
        
        
    def dispatch_homework(self, homework):
        for obj in self.students:
            print('{} dispatched to {}'.format(homework.title,obj.name))
            homework.count_students += 1
            print()
    
    
    def show_students(self):
        
        for obj in self.students:
            print('Name: {} and ID: {}'.format(obj.name,obj.student_id))
            print()
        
    def assign_grade(self,student,std_grade):
        student.grade = std_grade
        


# created teacher object    
mehdi = Teacher('Mehdi')


#created students objects
paola = Student(123, 'Paola')
wael = Student(456, 'Wael')


# add paola to mehdi's students' list
mehdi.assign_student(paola) # here paola is object


# display mehdi's students list
mehdi.show_students() # Should print: Paola

# add wael to mehdi's students' list
mehdi.assign_student(wael) # wael is an object


# display mehdi's students list
mehdi.show_students() # Should print: Paola, Wael



# create a new homework using the Teacher.create_homework method
homework = mehdi.create_homework('Lesson 15') #created a object homework


# display homework status
homework.status() # Should print: Undone: 0, done: 0


# dispatch the created homework to all students assigned to mehdi
mehdi.dispatch_homework(homework) 


# display homeeork status
homework.status() # Should print: Undone: 2, Done: 0


# trigger paola to finnish homework
paola.finnish_homework(homework)


# grade assigned to paola
mehdi.assign_grade(paola,'A')


# display homeeork status
homework.status() # Should print: Undone: 1, Done: 1


# trigger wael to finnish homework
wael.finnish_homework(homework)


# grade assigned to wael
mehdi.assign_grade(wael,'A')


# display homeeork status
homework.status() # Shoud print: Undone: 0, Done: 2


paola.show_grade()
wael.show_grade()



