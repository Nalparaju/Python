#Sets: Set is an unordered, mutable collection of unique items
'''
1. Unordered
2. Unique (will not allow duplicates)
3. Mutable
4. No Indexing and No Slicing
'''
#Sets can be denoted using '{}' flower brackets and by using 'set()' constructor
'''Note: Any list/tuple can be converted by using set(), by default it will remove the duplicate values'''

#Creation:
print("Sets example for syntax")
numbers = {1,2,3,4,5}
print(numbers)

print("sets removes duplicate values and sorts the values")
a = {1,2,2,2,31,1,3,2,4,0,1,9,5}
print(a)

print("Converting lists to sets and set() take care of duplicates")
list1 = [0,9,8,2,9,8,2,3,5]
convertToSets = set(list1)
print(convertToSets)
convertSetsToList = list(convertToSets)
print(convertSetsToList)

#Accessing Sets
'''This can be done using loops as sets is "unordered" we cannot use index to access'''

print("Accessing sets using loops")
for i in a:
    print (i);

#Methods/functions can use for sets
'''
1. .add()       >>> To add single element
2. .update()    >>> To add multiple elements
3. .remove()    >>> To remove an element, but raises an error if element doesnt exist
4. .discard()   >>> To remove an element and will not raise any error if element doesnt exist
5. .pop()       >>> Removes a random element from the set
6. .clear()     >>> Removes all elements
'''

print(numbers, "Pre Adding using .add()")
numbers.add(9)
print(numbers)

numbers.update([4,3,2],(1,9,28),[1,2,3])
print(numbers, "Post Adding mutiple using .update())")

#Creating an empty set:
set1 = set()
print(set1)

print(numbers, "Pre using .remove()")
numbers.remove(2)
print(numbers)

print(numbers, "Pre using .discard()")
numbers.discard(29)
print(numbers)

print(numbers, "Pre using .pop()")
item = numbers.pop()
print(numbers)
print("Removed Item:", item)

