#Dictionary:
''' Is a collection of key value pairs, each key is unique and associated with atleast one value'''

#Syntax for dictionary:
'''
d = {key1: value1, key2: value2}

creating empty dictionary:
1. using    >>> {}
2. using    >>> dict() 

syntax: 
fruits = {"apple":"red", "cherry":"red"}
fruits = dict(apple = "red", cherry = "red")

Sample code:
fruits = {"apple":"red", "cherry":"red"}
print(type(fruits))
print(fruits)

fruits = dict(apple = "red", cherry = "red")
print(type(fruits))
print(fruits)
'''

fruits = {"apple":"red", "cherry":"red"}

#Insert or update Dictionary
'''1. Insert Example'''
print("1. Insert Example")
fruits["orange"] = "orange"
print(fruits)

'''2. Update Example'''
print("2. Update Example")
fruits["apple"] = "green"
print(fruits)

#Accessing values in the dictionary - Using key dictionary will be accessed!! lists and tuples are accessed using index
print(fruits["apple"])

#Drawback for above way of accessing, If there is no key available it will return an error (KeyError: 'pineapple')
#for example: print(fruits["pineapple"])

#To overcome: instead of throwing you can predefine the return result
#If dont want to return anything just get if its available? you can use fruits.get("pineapple")
print(fruits.get("pineapple","unknown"))


#Delete
'''
1. del      - Using del you can delete an element with mentioning key
2. pop()    - Using pop you can delete an element with mentioning key

Note: Difference between del and pop is 
"del removes an element(s) by index/key but wont return anything. 
pop() removes it by index/key and also returns the value"

Spcific to dictionary: If key value is not available for pop(), we can predefine the default value like .get()
Syntax: fruits.pop("apple", None)
'''

print("Del example")
del fruits["orange"]
print(fruits)

print("pop() example1")
a = fruits.pop("apple")
print(a)
print(fruits)

print("pop() example2")
a = fruits.pop("apple","notavailable")
print(a)
print(fruits)