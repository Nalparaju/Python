#Basic decorators
'''Method ni disturb cheyakunda konchm functionality ni add chestam'''

#What and Why Decorators?
'''It takes another function as input and adds some functionality to it!! 
but doesn't change original functionality and also returns a new function at the end'''

'''To add a logic as extra, without changing the orginal functionality
Used more in Web development, Automation and API's'''

#How does it work?
'''
1. Decorator is a function takes a function as argument
2. Defines an wrapper method to add extra behaviour
3. Calls original method inside the wrapper
4. Return wrapper function'''

#Syntax:
'''
@decorator_name
def functions():
    pass
'''

#Example:
def my_Decorator(func):
    def wrapper():
        print("Before calling orginal function")
        func()
        print("After calling og function")
    return wrapper

@my_Decorator
def funtion():
    print("Hi")

funtion()

''' Output!!
Before calling orginal function
Hi
After calling og function'''

#Its like Authentication and Controller in .Net
'''Authenticate aite ne aa call chey annatu!! oka wrapper pettam    -- This is how decorator is used!!'''

#Function based Decorators with Arguments
#Example:
def repeat(num):
    def my_Decorator(func):
        def wrapper():
            for _ in range(num):
                func()
        return wrapper
    return my_Decorator

@repeat(3)
def funtion():
    print("Hi")

funtion()


#Class based Decorator
#Example
class MyDecorator:
    def __init__(self,func):
        self.func = func
    def __call__(self):
        print("before")
        self.func()
        print("after")

@MyDecorator
def greet():
    print("hello")

greet()
 
#Stacked Decorators
#Example
def repeat_one(func) :
    def wrapper():
        print ("decorator1")
        func()
    return wrapper
def repeat_two (func) :
    def wrapper():
        func()
        print("decorator2")
    return wrapper
@repeat_one 
@repeat_two 

def my_func():
    print ("Hi")

my_func()

#Builtin Decorators - Static, Abstract methods
