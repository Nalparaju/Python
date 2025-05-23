#Attributes
'''
1. Instance attributes
2. Class attributes
3. Static attributes
4. Private attributes
'''

#Instance Attributes:
'''
Belong to indvidual instance of a class
Defined using self.varaibleName inside the __init__ method'''

class Student:
    schoolName = "KTS"          #Class Variable     - This will never change
    pass



#Class Attributes:
'''
Belong to the class itself, not instances
Shared among all the instances of the class
Defined or intialised in the class but outside of __init__ method
'''
class Student:
    def __init__(self, name):   
        self.name = name        #Instance Variable  - This will change 


#Static attributes
'''
Class attributes
Accessed inside the static methods
Do not depend on class or self

Bonus: Static methods are defined using "@staticmethod" decorator'''

#Private attributes
'''
Indicated by a "__"(Double underscore) - "__attribute"
Not directly accissible outside the class
Can be accessed, using a special syntax :
    _ClassName__attribute
'''
#Example 1
class PrivateAttributeExample:
    def __init__(self, balance):
        self.__balance = balance

account = PrivateAttributeExample(1000)
print(account._PrivateAttributeExample__balance)

#Example 2: Getter method
class PrivateAttributeExample:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    
account = PrivateAttributeExample(1000)
print(account.get_balance())

#----------------------------------------------------------------------------------------------------------------------------
#Class Methods
'''Class method is a method that operates on class itself, rather than the instances
--> class instances ni within the class eh modify cheyali ante @classmethod ani use chesi "cls" ane parameter ni pass chestam andulo

defined using @classmethod
It takes the cls as first parameter instead of self
Can modify class attribute
'''

class School:
    SchoolName = "Krishnaveni Talent School"
    def __init__(self,name):
        self.name = name

    @classmethod
    def change_SchoolName(cls,new_schooolname):
        cls.SchoolName = new_schooolname

#Changing schoolname using class method
School.change_SchoolName("MVR")
print(School.SchoolName)

#changing SchoolName directly
School.SchoolName = "MVR"
print(School.SchoolName)

#Changing Schoolname of an object
obj1 = School("MVR")
print(obj1.SchoolName)

#Static Methods
'''
Static method is a method that does not required access to either instance or class
No need to use self, or creating an object
'''
class Math:
    @staticmethod
    def add(x,y):
        return x +y
    def mutliply(x,y):
        return x*y

print(Math.add(2,3))
print(Math.mutliply(2,3))

#----------------------------------------------------------------------------------------------------------------------------
#Encapsulation
'''
1. Capsule - Container or Protective shell
2. En      - Inside the container or protective shell 

The process enclosing something within a protective shell is called encapsulation
Internal data/methods ni direct access ivakunda protect cheyadanike manam encapsulation use chestamu
'''