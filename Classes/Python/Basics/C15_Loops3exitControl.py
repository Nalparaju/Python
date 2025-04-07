#Exit control Loops
''' Do While loop
No built in Do While loop, but we can use while and break
'''

#Note: 
# In while loop if the condition is false, it will not go for the block of code or logic
# In Do while even after condition is false, the block of code will execute 1 more time

#syntax:
'''
do
{
    #Code
}
While(Condition)
'''

queue = 5
while queue > 0:
    print("Cooking Pizza for:",queue)
    queue -= 1
print("Orders delivered!!")

while True:
    password = input()
    if password =="Prani@!":
        print("access given!!")
        break
