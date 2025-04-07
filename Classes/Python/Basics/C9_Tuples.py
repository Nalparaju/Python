#Tuples
'''Tuple is a sequence datatype, which is ordered, heterogeneous, immutable and allows duplicates
1. Ordered          -   The elements are defined as an ordered manner, that does not change
2. Heterogeneous    -   This allows to store different type of data types/ Can contain different data types
3. Immutable        -   Once created, you cannot change, add, or remove items in it
'''

#How to create Tuples
#Syntax: Using paranthesis
print("Using paranthesis")
my_tuple = (1,2,3,4)
print(my_tuple)
print(type(my_tuple))

#Syntax: Using no paranthesis
print("Using no paranthesis")
my_tuple2 = 1,2,3,4,5,6
print(my_tuple2)
print(type(my_tuple2))

#Note:
'''Why to use paranthesis - It is used for readability when creating nested tuples.'''

#Tuple constructor:
#Syntax: tuple()    >>> This is used for type conversion
a = tuple([1,"2",3,4])
print(a)
print(type(a))

# Tuple cannot be like 'my_tuple = (1)'
'''
This is intialization of the tuple above cannot be considered as a single tuple as the compiler it self considers it as an 'Int'
'''
my_tup = (1)
print(my_tup)
print(type(my_tup))

#To display Single tuple:
# Syntax:
my_tuple3 = (1,)
print(my_tuple3)
print(type(my_tuple3))

#Empty tuple creation
empty_tuple = ()
print(type(empty_tuple))

#How to access Tuples
''' Using Indexing
1. Positive indexing    >>> Starts from 0   >>> Left to right
2. Negative indexing    >>> Starts from -1  >>> Right to left
3. Slicing
'''
#Example
print("Example Tuple")
n = (1,3,5,2,45,78,90)
print(n[0:2])

#Nested Tuples#################
print("Nested Tuple example")
''' A tuple inside a tuple is called nested tuple'''
nested = (1,("pranith",24),3)
print(nested[0])
print(nested[1])
print(nested[1][0])
print(nested[1][1])
print(nested[2])

#Tuple Operations
# Oka tuple ni list laga extend cheskolemu, only copy chesi vere variable lo matrame store cheskogalam
'''
1. Concatination    -   Merging two tuples   >>> +
2. Repetation       -   Copying n times      >>> *
'''    
#Concationation Example
print("Concationation Example")
a = (1,4,2)
b = ("pranith",2,"24")
c = a+b
print(c)

#Repetation Example
print("Repetation Example")
d = (1,3)
e = d * 3
print(e)

#length - len()     >>> Returns the lenght of tuple
print(len(a))

#count -   count(x)
print(e.count(1))

#index(x)            >>> Returns the index of the value 'x'
print(e.index(1))

#unpacking tuples
print("Unpacking tuples example")
packed = 1,2,3
a,b,c = packed
print(a,b)
print(c)

#Note: If supposek, we have more values in the packed but less variable to unpack and store
#Syntax: a, *b, c = packed
#Result: 1, [1,2,3], 4
print("Unpacking tuples example2")
packed2 = 1,2,3,4,5,"pranith","apple",6
d, *e, f = packed2
print (d,e,f)
g, h, *k = packed2
print(g,h,k)

#Considering performance - List or Tuple which one is fast
''' Tuples are faster than list as its nature is immutable and doesnt waste time in changing like lists'''

m = (1,3,4,5,9)
a,_,b,_,c = m
print(a)
print(b)
# '_' notation means skip the variable alocation

w,x,y = m[0::2]
print(w)
print(x)
print(y)