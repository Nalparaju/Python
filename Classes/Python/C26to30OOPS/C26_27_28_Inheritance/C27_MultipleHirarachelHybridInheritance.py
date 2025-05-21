# Mutliple Inheritance - Multiple base, single derived
'''Mutliple parent classes and single child classes'''

class Student:
    def study(self):
        print("studying")

class Male:
    def read(self):
        print("Boy reading")

class Boy(Student,Male):
    pass


b = Boy()
b.read()


#Note: this is not method overriding!!
'''Priority: 
Child class - First Parent class in inheritance(class parameters) - Then Second Parent class'''
#Method Resolution Order(mro) -- Manam multiple classes inherit cheskunapudu eh class lo check cheskovali enti ani
class A:
    def show(self):
        print("method in class A")
class B:
    def show(self):
        print("method in class B")
class C(A,B):
    def show(self):
        super().show()
        print("method in class C")

c=C()
c. show()

# Hirarecheal inheritance
class A:
    def show(self):
        print("method in A")

class B(A):
    def show(self):
        print("method in B")

class C(A):
    def show(self):
        super().show()
        print("method in C")

c = C()
c.show()

#Hybrid inheritance
class A:
    def show(self):
        print("method in A")

class B(A):
    def show(self):
        super().show()
        print("method in B")

class C(A):
    def show(self):
        super().show()
        print("method in C")

class D(B,C):
    def show(self):
        super().show()
        print("method in D")

d = D()
d.show()
