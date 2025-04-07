####---------------------------------------Class 7---------------------------------------####

#Modifying List
''' Two methods
1. Append
2. Insert
'''

numbers = [1,2,3,4]

print("Mutable Example")
numbers[2] = 2
print(numbers)

print("Append example")
numbers.append(5)
numbers.append(7)
numbers.append(11)
numbers.append(12)
numbers.append(11)
print(numbers)

print("Insert method")
numbers.insert(0,10)
numbers.insert(100,10)
print(numbers)

#It will remove the first occurrnce in the list [10, 1, 2, 2, 4, 5, 7, 10]
print("Remove example")
numbers.remove(2)
print(numbers)

print("Pop example")
popped = numbers.pop()
print(numbers)
print(popped)

#Del numbers - del is a keyword
print("Delete example")
print(numbers)
del numbers[2]
print(numbers)

#This indexing in the pop does same as del (but a method)
numbers.pop(2)
print(numbers)

#Clear method - Empties all the numbers or values in the list
#numbers.clear()
#print(numbers)

#Sort method - ascending order
numbers.sort()
print(numbers)

#Sort method - descending order
numbers.sort(reverse=True)
print(numbers)

print("Sorted Example")
sorted_List = sorted(numbers)
print(sorted_List)

lst = ["Pranith", "Zebra","Apple"]
lst.sort()
print(lst)