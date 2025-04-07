#Loops:
'''
Loop is a block of code, to repeat mutliple time without writing the code.'''

#Types of loops
'''
Entry Control loop
Exit Control loop'''

##Entry Control loops
''' #No Do while loop in python#
1. for loop
2. while loop'''

#Break or Countinue
'''
break       >>> is a keyword to break/stop the loop
continue    >>> is a keyword to skip particular iteration in the loop
'''
print("Break example")
for i in range(1,6):
    if i ==3:
        break
    print(i,end=" ")

print("Continue example")
for i in range(1,6):
    if i ==3:
        continue
    print(i,end=" ")