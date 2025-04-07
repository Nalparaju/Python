#Set operations
'''To manipulate effectively we use set operations, we use two sets to perform set operations
1. Union
2. Intersection
3. Difference
4. Symmetric difference'''

#1. Union:
''' To display unique values from two sets
Syntax: Below symbols are used to perform union
    '|' or 'union()'
'''
print("Sets - Union Example")
a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a|b)
print(a.union(b))

#2. Intersection:
''' To display common values from two sets
Syntax: Below symbols are used to perform intersection
    '&' or 'intersection()'
'''
print("Sets - Intersection Example")
print(a&b)
print(a.intersection(b))

#3. Difference:
''' To display first mentioned set and removes common elements present in a and b
Syntax: Below symbols are used to perform difference
    '-' or 'difference()'
'''
print("Sets - Difference Example")
print(a)
print(b)
'''Output:
{1, 2, 3, 4, 5}
{3, 4, 5, 6, 7}'''

# Ila cheste emaitadi ante, a and b lo unna common element delete chesi only a set eh print chestadi
print(" a - b, elements in a not in b") 
print(a-b)

#Okavela ila reverse lo b-a cheste, b and a lo common elements delete chesi only b set eh print chestadi
print(" b - a, elements in b not in a")
print(b-a)

#4. Symmetric difference
''' To Display only uncommon values and ignores common values
Syntax: Below symbols are used to perform difference
    '^' or 'symmetric_difference()'
'''

print("Sets - Symmetric difference")
print(a^b)
print(b.symmetric_difference(a))

#Sets - Subset and SuperSet
''' Symbols of subset and superset
1. Subset   -   All elements of one set existing in another
    Syntax: '<=' or 'a.issubset(b)'

2. Superset -   One set contains all elements of another
    Syntax: '>=' or 'b.issuperset(a)'

Note: Emptyset is a subset of any set, which means any set will be superset of empty set.'''

# 'x' is subset of 'y' and 'y' is superset of 'x'
'''Idi konchm confusing topic vinu okasari
1. Ippudu x anedi subset of y kada? 
Enduku?? x lo eh values aite unayo avvani y lo unnai kada!!

2. Then now, y anedi superset of x avtadi
Enduku?? y lo unna values eh x lo unai ankuntam kabbati'''

print("Subset and Supersets example")
x = {1,2}
y = {1,2,3,4,5}
print(x <= y) #Means all elements of one set (x) exists in another (y)
print(y >= x) #Means one set (y) contains all elements of another (x)

#Sets - Disjoint Set
''' If taken two sets, if there is no common value between two sets is called disjoint set
Syntax: a.isdijoint(b)'''

print("Disjoint set example with common element - O/P False as it has common element")
m = {1,2,3}
n = {3,4,5}
print(m.isdisjoint(n))

print("Disjoint set example without common element - O/P True as it doesn't have any common element")
m = {1,2,3}
n = {4,5,6}
print(m.isdisjoint(n))

#-------------------------------------------------------------Important notes-------------------------------------------------------------
'''
1. In other words for Union: The above example gives you an output but doesnt store in a value..right?? 
So you will use A.update(B) >>> This will give unique values and updates in a variable'''
A = {1,2,3}
B = {2,3,4,5}

#Printing with union
print(A.union(B))
print(A)

#Printing after using update
A.update(B)
print(A)

'''
2. Same like above we have another function store intersection in a variable'''
M = {1,2,3,4,5}
N = {3,4,5,6,7,11}

#Printing with intersection
print(M.intersection(N))
print(M)

#Printing after using update
M.intersection_update(N)
print(M)

'''
3. Same like above we have another function store difference in a variable'''
M = {1,2,3,4,5}
N = {3,4,5,6,7,11}

#Printing with difference
print(M.difference(N))
print(M)

#Printing after using update
M.difference_update(N)
print(M)

'''
4. Same like above we have another function store difference in a variable'''
M = {1,2,3,4,5}
N = {3,4,5,6,7,11}

#Printing with symmetric difference
print(M.symmetric_difference(N))
print(M)

#Printing after using update
M.symmetric_difference_update(N)
print(M)