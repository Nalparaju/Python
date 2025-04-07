#Built-in exceptions
'''
ZeroDivisionError
ValueError
TypeError
IndexError
KeyError
FileNotFoundError'''

try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("cant divide by zero")
except TypeError:
    print("Invalid entry")
except ValueError:
    print("Invalid datatype")

#Custom Exceptions
#Syntax:

class MyError(Exception):
    pass
try:
    raise MyError("Exception is here")
except MyError as e:
    print(e)


try:
    amount = int(input("Enter amount"))
    balance = 5000
    if amount > 5000:
        print("Insuficient balance")

        dic = {"Name":"Pranith", "Balance": 5000}
        print(dic["Age"])
    else:
        print("Transaction sucessful")
        #print("balance"+balance) #Uncomment this line to see the type error as balance is not "string" it cant concat
        num = [1,2,3,4]
        print(num[2])

except IndexError:
    print("Invalid index")
except KeyError:
    print("Invalid key")
except TypeError:
    print("Invalid type")
except ValueError:
    print("Only whole numbers needed")
finally:
    print("Thank you")


