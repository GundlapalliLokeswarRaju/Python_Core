# Abstraction
# Abstraction is a process of hiding the data and high-lighting the set of services.
# show-room cars: i20 car(basemodel, mid-level, top-model, top-plus-model.)
# in python we use abstract keyword to make a method as abstract method.
# in python to make abstract class we extend it from abs module.
# Task 1:- abs class contains concern methods and abs methods.
from abc import abstractmethod, ABC

from bokeh.core.has_props import abstract


class Parent(ABC):
    # instance method (abs methods)
    @abstractmethod
    def display(self):
        pass
    # instance method (concrete method)
    def get_data(self):
        print("get method")

class Child(Parent):
    def display(self):
        print("display method")

c = Child()
c.display()
c.get_data()

# Task 2:- In abs class can we create object?
# Ans:- No. Proof
class Test(ABC):
    @abstractmethod
    def d1(self):
        pass
    def d2(self):
        print("d2 method")

Test().d1()
Test().d2()
Test()
# Can't instantiate abstract class Test with abstract method d1