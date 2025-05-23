# Abstraction
'''
Hiding internal details and exposes only required information 
abstraction can be implemented by using abstract classes and abstract methods'''

# Cannot create an object for abstract class
# Abstract method - Abstract class lo unna methods eh abstract method
# Defined by using a decorator @abstractmethod
# Implement cheyalsina avasram ledu!! chesina kuda override chesestundi

#%%
from abc import ABC,abstractmethod
#ABC --> Abstract base class
#abc defines a module that provides abstract base class
#ABC a class from abc module deniki ante oka base class ni create cheskodaniki.

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("Vechile is called")

class Car(Vehicle):
    def start(self):
        print("Car is started")

#This is not possible as abstract methods cannot be called using an object.
#vechile = Vehicle()
#vechile.start()

car = Car()
car.start()

# %%
# But you can do this ok!!
from abc import ABC,abstractmethod
#ABC --> Abstract base class
#abc defines a module that provides abstract base class
#ABC a class from abc module deniki ante oka base class ni create cheskodaniki.

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("Vechile is called")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car is started")

# This is not possible as abstract methods cannot be called using an object.
#vechile = Vehicle()
#vechile.start()

# This is possible to call abstract class method by using super in the non abstract class child method
car = Car()
car.start()

# %%
