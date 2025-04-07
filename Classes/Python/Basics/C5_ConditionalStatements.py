#Conditions
'''
1. If
2. If else
3. If elif else'''


#Condition If/If-else
'''
Syntax for If:
if condition1:
    #block of Code'''


'''
Syntax for If - else:
if condition1:
    #block of Code
else:
    #block of code'''

print("Example 1 for Condition If/If-else")
a = 2
if a>5:
    print("a is greater than 5");
else:
    print("a is less than 5");


#Condition If - elif - else
'''
Syntax for If - elif - else:
if condition1:
    #block of Code
elif condition2:
    #block of code
else:
    #block of code'''

print("Example 1 for Condition If - elif - else")
x = int(input())
if x < 15:
    print("x is less than 15");
elif x is 15:
    print("x is 15");
else:
    print("x is greater than 15");


#Condition nested If
'''Syntax for If:
if condition1:
    #block of Code

    if condition2:
        #block of Code'''

x = int(input())
if x < 10:
    if x > 5:
        print("x is between 5 and 10")
    else:
        print("x is less than 5");
else:
    print("x is greater than 10");


#Condition Ternary operator
'''
Syntax for Ternary operator:
result = true_value if condition1 else false_value'''

x = int(input())
print("even number") if x%2==0 else print("x is odd number");
