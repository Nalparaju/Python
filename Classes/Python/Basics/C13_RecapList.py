#List
'''
creating: [] or lis()
indexing: +ve and -ve
          0.....n-1
         -n......-1

Slicing: Start,Stop,Step
Defaults: 0,    1,  1

Modifying list: using index list1[2] = 1

Adding a particular element in index using 'insert' function
Adding a particular element in the end using 'append' function

remove() vs del vs pop() vs clear()

Remove will be removed based on value
pop    will remove based on 'index'(parameter), if not mentioned deletes last element in the list and returns at the same time
del    will remove based on index but will not return a value
clear  will remove all the elements in the list
        
sort vs sorted:

sort:   This will have the list sorted, also allows a parameter to set "reverse = true/false"
sorted:  will return a value that can be stored in a variable
'''

#List methods:
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