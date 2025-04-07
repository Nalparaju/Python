#syntax: for var in range(end)
'''
Loop starts with start value '0' and ends with stop value 'n-1' 
'''

print("Loops example")
for i in range(10):
    print(i)

#Printing a loop in single line
print("Loops print in a single line example")
for i in range(10):
    print(i,end=" ")
    #print("x")

#Printing a loop with lists
fruits = ["apple", "banana"]
for i in fruits:
    print(i,end=" ")

#Printing a loop with a string
for i in "ITERATESTRING":
    print(i)

#Printing mutiplication table based on user input
n = int(input())
for i in range(1,11):
    print(n,"*",i,"=",n*i)

