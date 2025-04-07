#Types of Operators
'''
1. Arthematic operators
2. Assignment operators
3. Comparision operators
4. Logical operators
5. Bitwise operators
6. Ternaty operators
7. Membership operators
8. Identity operators'''

#1. Arthematic operators
'''
Addition (+)
Substraction (-)
Multiplication (*)
Division (/)
Floor Division (//)
Modulo Division (%)
Exponential (**) '''
a = 5
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#2. Assignment operators
'''
=
+=
-=
*=
/=
//=
**='''

print("# Example 1")
x = 10
x += 5
print(x)

print("# Example 2")
str1 = "Sai"
str1 += "Pranith"
print(str1)
'''
Note: String performs concatination and repetation, 
Which means only can perform += and **'''

#3. Comparision operators (No need examples, You know this)
'''
==
!=
<
>
>=
<='''

#4. Logical operators
'''
and 
or 
not'''

print("# Example 1")
x = 10
y = 5
print(x > y and y > 3)
print (x < y or y > 3)
print (not(x>5))

#5. Membership operators - are used to test if a value is present in or not present in a sequence(string, tuple, set, range)
#Note: If you declare a value and its in a sequence, then it will return true
'''
in
not in'''
print("# Example 1")
print('a' in 'apple')
print('b' in 'apple')
print('b' not in 'apple')

r1= range(10)
print(100 in r1)

#6. Identity operators - are used to compare memory locations of two variables
'''
is
is not'''
a = 10
b = 10
c = "pranith"
print(a is b or b is c)
print(a is b and b is not c)

#7. Bitwise operators
'''
bitwise and    &
bitwise or     |
bitwise not    ~
bitwise xor    ^
left shift     <<
right shift    >>'''

#   8,      4,      2,      1
#  2^3     2^2     2^1     2^0

#0      0000
#1      0001
#2      0010
#3      0011
#4      0100
#5      0101
#6      0110
#7      0111
#8      1000
#9      1001
#...........
#16     

print('Example #1 Bitwise AND (&)')
a,b = 3,5
print(a&b)

#o/p: 1 for bitwise 'and' (If only two digits are 1 then only 1 else 0)
'''
Solution:
3   =   0011
5   =   0101
--------------
        0001 (which means 2^0)
--------------'''

print('Example #1 Bitwise OR (|)')
a,b = 6,3
print(a|b)

'''
Solution:
6   =   0110
3   =   0011
--------------
        0111 (4+2+1)
--------------'''

print('Example #1 Bitwise XOR (^)')
a,b = 5,3
print(a^b)

'''
Solution: (o/p if two bits are different then 1 or 0)
5   =   0101
3   =   0011
--------------
        0110 (4+2)
--------------'''


print('Example #1 Bitwise Not (~)')
a = 5
print(~a)

'''
Solution: -6
~n  = -(n+1)
which means ~a  =   -(5+1) = -6'''

print('Example #1 Rightshift (>>)')
a = 5
print(a>>1);

'''
Solution: 2
a       0101    a>>1
--------------
        0010    = 2
--------------'''

print('Example #1 Leftshift (<<)')
a = 5
print(a<<1);

'''
Solution: 10
a       0101    a<<1
--------------
        1010    = 10
--------------'''

#8. Membership operators
