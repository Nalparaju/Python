#Access Specifiers
'''
1. Public       - Accessible from anywhere, inside/outside the class or in subclass or anywhere
2. Protected    - Using "_" single underscore in prefix, Can be used/accessible within class or subclass
3. Private      - Using "__" double underscore in prefix
'''

#Getter and Setter methods
'''
Getter methods  - Accessors - retrives the value of a private attribute
Setter methods  - Mutators  - modifies the value of a private attribute
'''

class GetSetterExample:
    def __init__(self,name):
        self.__name = name
    
    #Getter method
    def get_name(self):
        return self.__name
    #Setter method
    def set_name(self,name):
        self.__name = name

#getting a value from private variable
obj = GetSetterExample("Pranith")
print(obj.get_name())

#Setting a value in private variable
obj.set_name("Sai Pranith Nalparaju")
print(obj.get_name())

#----------------------------------------------------------------------------------------------------------------------------
#Inheritance
'''
Super Class    - Parent class
Sub class      - child class

Syntax -
            class childClassName(Parent class):
'''
