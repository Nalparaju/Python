#Method Overriding
'''
- Child class method parent class method ni override cheste run time polymorphism antam'''

# %%
class A:
    #By default its called
    def __init__(self):
        print("Parent Init function")
    
    #This is called when super class is called in the child
    def show(self):
        print("Parent class")

class B(A):
    def show(self):
        super().show()
        print("Child class")

a = B()
a.show()