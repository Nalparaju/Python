#Method Overloading - This is not possible like how you do it in C#
'''
- You can achieve this by using default arguments and variable length arguments
- Defining multiple methods with same name but different parameters
- Also known as compile time polymorphism
'''
#Why python doesnt support:
class A:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c): #This method overrides first "add" method
        return a+b+c

o = A()
#o.add(1,2)   # This will not work
o.add(1,2,3)  # This will work
#Reason: Python will over first method with second method.

#%%
# So by using default arguments we do it, lets see!!
class A:
    def add(self,a,b,c=0): #This method overrides first "add" method
        return a+b+c

o = A()
print(o.add(1,2))
print(o.add(1,2,3))

# %%
# Using variable length arguments - Okavela manaki enni arguments pass cheyalo teliyanapudu variable length arguments use chestam
'''
1. args
2. kwargs'''

class VariableLengthMethodOverloading:
    def addition(self, *args):
        return sum(args)

ob1 = VariableLengthMethodOverloading()
print(ob1.addition(1,2,4,5))

# %%
#Datatypes use chesi methodoverloading cheyochu - Not really useful in real world

from functools import singledispatch
@singledispatch
def process(data):
    return "default"

@process.register(int)
def _(data):
    return f"returning int value {data}"

@process.register(str)
def _(data):
    return f"returning string value {data}"

print(process(10))
print(process("Pranith"))