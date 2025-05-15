#Inheritance - Main class nundi sub class inherit cheskuntadi
'''
You can use either of this terminology
1. Parent class - Child class
2. Super class - Sub class
3. Base class - Derived class'''

#5 Types
'''
1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchial inheritance
5. Hybrid inheritance'''

#Single inheritance - Single Parent and Single child class

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

obj = Child()
obj.show()
obj.display()


#Method overriding - Parent class lo unna "show" value Child class lo unna show method override chestundi. 
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        print("This is Child class show function")

    def display(self):
        print("This is Child class")

obj = Child()
obj.show()
obj.display()

# %%
#Override avvakunda undali ante:
#Method overriding - Parent class lo unna "show" value Child class lo unna show method override chestundi. 
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        super().show()
        print("This is Child class show function")

    def display(self):
        print("This is Child class")

obj = Child()
obj.show()
obj.display()

# %%
# Mutliple Inheritance - Multiple base, single derived
# Multilevel           - Grand parent class, Then Parent, then child
# Hirarechel           - Single parent, multiple child classes
# Hybrid               - ee paina unna four types lo edain oka 2 kalpeste ade hybrid

class People:
    def __init__ (self,no_fin):
        self.no_legs=2
        self. no_heart=1
        self. no_fin=no_fin
    def eat(self):
        print("people can eat")
    def work(self):
        print ("can work")

class Male(People) :
    def __init__ (self, name, no_fin):
        super().__init__(no_fin)
        self.name=name 
    def eat(self):
        print("male can eat")
    def play(self):
        print("can play")

m = Male("pranith",10)
m.eat()
m.work()
m.play()
print(m.no_legs)
print(m.no_fin)
# %%
