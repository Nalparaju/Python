#Six types of Data types available in python
'''
1. Numeric - int, float, complex
2. Sequence - string, list, tuple, range
3. Mapping - dictionary(key value pair)
4. Sets - set, frozenSet
5. Binary - bytes, byteArray
6. Boolean - bool
'''

##--------------------Numeric-------------------------
#Integer datatype is immutable, A Data which cant be changed until unless removed or rewrote is called immutable.
#Supports arthmetic opertaions
#Depends on memory size
age = 27
year = 2025

#Floating
temperature = 36.4

#Complex
cp_1 = 4 + 5j;


##--------------------Sequence------------------------
#string
name = "PythonClass"

#List
#Lists are denoted using square brackets, lists are mutable, ordered(sorting)
fruits = ["Apple", "Orange", "Banana"]
numbers = [1,2,3,4]
mixedDataType = [1, "stringDataType", True, 3.46]
print(mixedDataType);

#Tuple
#Tuples are denoted with paranthesis '()'
#Tuple are immutable
actors = ("pk","mb")

#Range
range1 = range(10)
print(range1)
# this Prints as (0,9) -> which means a whole number of 0 to 9 number

range2 = range(10,45)
print(range2)
# this Prints as (10,45) -> which means a whole number of 10 to 44 number


##---------------------Mapping-------------------------
#Dictionary
student ={
    "Name" : "Sai",
    "Age"  : 27,
    "City" : "Hyderabad"
}

print(student);


##--------------------Sets-----------------------------
#Sets are mutable and unordered
#Can't store duplicates, Only unique values can be stored
#Denoted with '{}'
unique_number = {1,2,3,4}
emptySet_isDenotedAs = set()

#FrozenSets
frozensets = frozenset(["a", "e", "i", "o", "u"])


##------------------Boolean----------------------------
#It will have only two values -> True/False
Is_Sunny = True
Is_Student = True

is_equal = (5==5)
print(is_equal)
