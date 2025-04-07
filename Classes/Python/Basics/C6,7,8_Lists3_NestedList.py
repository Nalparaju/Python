#Nested List

'''List within a list is called sublit/nested list'''
matrix = [
    [1,2,3],
    [5,9,6],
    [4,9,0]
]

'''
    00  01  02  >>> Row 0
    10  11  12  >>> Row 1
    20  21  22  >>> Row 2
    |   |   |   
    C1  C2  C3
'''

print(matrix[0][1])

# List methods
'''
1. append(x)    -   Add's x to the end
2. insert(i, x) -   Add's x at index i
3. remove(x)    -   Removes first occurance of x
4. pop()        -   Removes end/last value from the list
5. pop(i)       -   Removes value at index i
6. clear()      -   Clears all the values in the list
7. sort()       -   Sorts the list
8. sort(reverse = True) - Sorts in the reverse
9. count(x)     -   Counts the number of times x in the list   
10.index(x)     -   Gets the index of x
11.copy()       -   Copies the same list
12.reverse()    -   Reverse the values in the list (but not in sorted order)
'''

#List Differences
'''
1. Sorted       -   Sorted will create a new list
2. Sort         -   Sort will sort the list itself'''

# Count
print("Count example")
numbers = [1,2,3,4,4,8,1,1,3,5,6,7,7]
print(numbers.count(1))
print(numbers.count(100))
print(numbers)

# Index
print("Index example")
print(numbers.index(4))

#If the given input value is not available in the list, then it throws a value error
'''print(numbers.index(100))'''

print("Reverse of a list")
numbers.reverse()
print(numbers)