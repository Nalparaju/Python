'''
1. Pure Functions
# Fucntional should return without changing

2. Immutablity
# To compare previous data and current data

3. First class and higher order functions
# Functions can be assigned to variables and 
# Can be passed as arguments
# Return for another functions
#Oka function ni argument la consider cheyochu leda return kuda cheyochu - Higher order function

4. Function Composition
#Oka function ni combine chesi kuda use cheskovachu ade function composition
# Example'''
def double(x): return x*2
def square(n): return n*n
print(square(double(2)))

'''
5. Refrrential transperency
# Function behaviour ni change cheyakunda modify cheskovadam
An expression can be replaced with its value, without changing the behaviour of the program

6. No side effects 
#Debugging easy avtadi
-> No modifying global variables
-> No Changing parameters
-> No I/O (print statements)
-> No DB calls 

7. Recurssion over loops
# Same function use cheskuntam instead of loops!! Example factorial program.

8. Declarative style
# Focus mainly on what to do!! not how to do.
'''