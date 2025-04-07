#Features of python
'''
1. Procedural programming
2. Object oriented programming
3. Functional programming'''

#Concepts in OOPS
'''
1. Class
2. Object
3. Polymorphism
4. Inheritence
5. Abstraction
6. Encapsulation'''

#Class:
'''Blue print for creating objects''' 
'''Class is defined in Pascal case (This is not mandatory but a rule)'''

#Object:
'''Object is an instance of a class'''

#Example 1:
class messagePass:
    def message(self):
        print("hello!!")

c1 = messagePass()
c1.message()

#Example 2:
class Car:
    def carTypes(self, brand, model):
        self.brand = brand
        self.model = model
        print(brand,model)
c1 = Car()
c1.carTypes("Ninja","Bike")

#Example 3:
class Car4:
    brand = "BMW"
print(Car4.brand)

#What is neccesity of Object oriented programming?
'''To perform operations with efficiency by using Encapsulation, Abstraction, Inheritence, Polymorphism'''

#Pass
'''Pass is a keyword to create an empty class'''
class ClassName:
    pass

class Car:
    pass

# Name here is called an attribute
car = Car()
car.Name = "Elantra"
car.Company = "Hyundai"
print(car.Name)

#self - A default parameter
'''Represents the current instance of a class'''
'''Oka class lo unna methods, class lo ne access cheskodaniki self use avtundi'''

#__init__
'''A special methods that runs automatically when a new object created'''

# Class variables vs Instance variables
class Student:
    schoolName = "KTS"          #Class Variable     - This will never change
    def __init__(self, name):   
        self.name = name        #Instance Variable  - This will change 

student1 = Student("Pranith")
student2 = Student("Vamshi")
print(student1.schoolName, student1.name)
print(student2.schoolName, student2.name)