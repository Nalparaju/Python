#Lambda Functions
'''
Defination: Lambda function is an anonymous function.
Keyword: lambda

Properties:
Written in single line, 
It can take multiple arguments but only one expression
'''
#Syntax:
'''lambda arguments: expression'''

'''
arguments: These are passed when function is called
expression: Single operation performed and returned 
'''

square = lambda x: x**2
print(square(5))

addition = lambda a,b:a+b
print(addition(5,4))

'''-------------------------------------------------------------------'''
#Higher Order functions
''' On 2 cases we call a function as 
1. A function that takes another function as an argument
2. A function that returns a function'''

#Built-in higher order functions
''' Two built-in higher order functions
1. Map      >> Applies a given function to every element in an iterable
2. Filter   >> It keeps only element that satisfy a condition
'''

#Map Syntax:
'''map(function,iterable)'''

#example:
numbers = [1,3,4,5]
square = map(lambda x: x**2, numbers)
print(list(square))




#Filter Syntax:
'''filter(function,iterable)'''
print("All numbers:",numbers)
even = filter(lambda x:x%2==0,numbers)
print(list(even))

