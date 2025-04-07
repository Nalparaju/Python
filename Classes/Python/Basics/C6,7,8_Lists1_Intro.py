#List
'''
It is a collection of items in a specific order, It can hold any number of items and items can be of any data type'''

#Properties
'''
1. Mutable
2. Ordered
3. Heterogeneous(It can be of any data type/It can hold any data type)
4. Allows duplicates'''

#Syntax for creating List using "[]" square brackets
'''
a = []'''
#Examples:
numbers = [1,2,3,4]
fruits = ["Banana", "Apple", "Cherry"]
numbersAndFruits = [42, "fruit", 4.6, True]
emptyList = []

#Syntax for creating List using "list()" list constructor
#Examples:
a = list((1, 2, 3, 'apple', 4.5))
print(a)


#Accessing - A list can be accessed by using Indexing and Index starts from 0
''' Two Types of Indexing
1. Positive >>> starts from 0 ---> n-1 (This is from Left to right) 
2. Negative <<< starts from -1 --> -n  (This is from Right to left)
'''
#Examples:
print(numbers)
print(numbers[3])
print(numbers[-3])

#Slicing - If we want to use particular sub portion we use slicling/Used if we need a set of range in a list.
#Keywords: start, stop, step
'''
1. start   ---> Default 0  >>> This means include first
2. stop    ---> n(elements)/(n-1)Index  >>> This means exclude last
3. step    ---> default 1'''
#Examples:
print(numbers[0:4:1])
print(numbers[1:4:2])

#Types of slicing
''' Four types of slicing
1. Basic slicing 
2. Omit start
3. Omit stop
4. Using step'''

#Basic Slicing: Only mentioning start and stop
print("Basic")
print(numbers)
print(numbers[0:3])
print(numbers[-5:-3])

#Omit Start: Only mentioning the stop
print("Omit Start")
print(numbers)
print(numbers[:7])

#Omit Stop: Only mentioning the start
print("Omit Stop")
print(numbers)
print(numbers[2:])
print(numbers[-3:])

#Using Step:
print("Slicing")
print(numbers)
print(numbers[0:4:6])
print(numbers[::-1])
print(numbers[-3:-5:-1])
