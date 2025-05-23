#LEGB
'''
1. Local
2. Enclosing
3. Global
4. Built in'''

#Local lo declare cheskunedi
#Loops lo declare cheskunedi
#Global lo declare
#Builtin - len(),print()

x = 5               #Global
def out():
    a = 1           #Eclosing - Ee variable ee function lo enni functions unna kuda access cheskovachu
    def inner():
        b = 2       #Local
        print(b)
    inner()

#Pure Functions
#Impure Functions

#%%
#Pure Function:
'''Within the function, there shouldnt be any kind of manipulation

-> No modifying global variables
-> No Changing parameters
-> No I/O (print statements)
-> No DB calls '''
def square(n):
    n = n**n
    return n

print(square(2))

#%%
#Impure function:
'''Can have side effects, Manipulation can be done'''
#Ex: 1 
a = 0
def addition(z):
    a = z+1
    return a

print(addition(2))

#Ex: 2
import random 
def r():
    return random.randint(1,100)

print(r())

#Ex: 3
def append_item(lst,item):
    lst.append(item)
    return lst

ls = [1,2,3]
print(append_item(ls,2))
# %%

