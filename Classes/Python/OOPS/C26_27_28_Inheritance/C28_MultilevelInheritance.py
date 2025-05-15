#Multilevel Inheritance

# %%
class Student:
    def read(self):
        print("studying")

class Male(Student):
    def read(self):
        print("reading")

class Boy(Male):
    def read(self):
        Male.read(self)
        Student.read(self)
        print("learning")

a = Boy()
a.read()

# %%
#This is an example for attributes with inheritance
class Person:
    def __init__(self,name) :
        self.name=name 

    def work(self):
        print("i can speak")

class Student(Person) :
    def work(self):
        print("i can study")

class Graduate(Student) :
    def __init__(self, name, age): 
        super().__init__(name)
        self.age=age 

    def work(self):
        super().work()
        print("i can research")

grad_1 = Graduate("X",8)
print(grad_1.name)
print(grad_1.age)
# %%
#Note: 
'''
Indaka paina __init__ method lekuna kuda manam methods vadukunam ela?
__init__ method anedi default untadi anni classes lo
enduk ante..!! OBJECT CLASS IS SUPER CLASS FOR ALL CLASSES'''