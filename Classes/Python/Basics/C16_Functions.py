#Functions:
'''
A block of code, which is organised, reusable and to perform a specific task.
'''

#Usecases:
'''
1. Code reusability
2. Modularity
3. Avoid redundancy
4. Easy debugging
'''

#Types of functions:
''' 4 Types of functions
1. Built-in methods
2. User defined methods
3. Lambda functions
4. Recursive functions
'''

##Types of Arguments
'''
1. Positional arguments
2. Default arguments
3. Keyword argument
4. Variable length (or) Arbitary argument    >>> Two Types:  (*args, *kwargs)
'''

#Syntax: for defining a function
'''
def function_name(parameters):
    ##Code##
    return value (#this is optional)
'''

#Syntax: for function calling
'''
function_name(arguments)
'''

#Examples for user defined funcion:
print("Example for defining a function")
def greet():
    print("Hello Pranith")

print("Example calling a function")
greet()

print("Example for addition using function")
def addition(a,b): #a,b are called parameters
    return a+b

a = addition(3,4) 
print(a)
#Where as while calling the function we say a,b values are arguments


#Example for recursive function: A function calling itself
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Recursive function example - Factorial method")
f = factorial(5)
print(f)

factorialInput = int(input("Enter number to find the factorial"))
f = factorial(factorialInput)
print(f)

#Lambda Functions
'''
Defination: An anonymous function, written in single line.'''