#Types of Arguments:

#Positional Arguments:
def greet(name = "Unknown" ,age = 00):
    print("Hello",name,",","Your age is",age)
greet("Pranith",27)

#Keyword Arguments:
greet(age=27,name="Pranith")

#Default Arguments: (assigns a default value to the parameter)
greet()

#Variable length Arguments or Arbitary arguments:
'''
1. *args
2. **kwargs'''

# *args (or) non keywords variable length arguments:
'''When you dont know specific parameters needed for a function, we use *args'''
def addition(*num):
    sumOfNums = sum(num)
    print(sumOfNums)

addition(1,3,4)
addition(3,4,56,234,5,67,98,-45,-87,56)

# **kwargs (or) keywords variable length arguments:
'''ee function oka dictionary laga accept chestundi,
Number of arguments enno telidu kani return lo keyword and value kavali annapudu idi use chestam'''
def kwArgs_Example(**arguments):
    for key,value in arguments.items():
        #Just printing
        #print(key,value)
        #Printing in a readable format
        print(key,":",value,",",end=" ")

kwArgs_Example(Name = "Pranith", Age = 20, Course = "Machine Learning")