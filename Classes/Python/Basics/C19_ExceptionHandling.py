#Exception Handling
'''An unexpected event occurs during the execution of a program which disrupts the flow'''
#examples:
'''
1. Zero division error
2. Memory out of bond exception
'''

#Blocks of exception
'''
1. Try
2. Except
3. Finally
4. Else (optional)'''

#Errors - Can be corrected not handled, exceptions are handled.
'''
1. Syntax errors
2. Indentation error
'''

# try, except, else, finally keyword/block
try:
    a = int(input())
    b = int(input())
    print(a/b)
except ZeroDivisionError:
    print("Cant divide with Zero")
else:
    print("No Exception")
finally:
    print("Executed this line")


