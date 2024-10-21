# Types of variables in OOPS
# 1. Class Variable 2.Static Variable 3.Instance Variable
# Types of Methods in OOPS
# 1. Class Method 2.Static Method 3. Instance Method
from spacy.util import update_exc


# Inheritance:- Achieve properties one class to another class.

# Types:- Single, Multiple, Multilevel, Hybrid, Hierarchical

# Single-Inheritance
# Single inheritance enables a derived class to inherit properties from a parent class.
class Parent:
    # instance method
    def get_id(self): # self is an object in instance method
        print("get_id instance method")
class Child(Parent):
    # instance method
    def update_id(self): # self is an object in instance method
        print("update_id instance method")
# create the object for child Class
# Class name and object name must be same
# c is reference variable

c = Child() # object
c.get_id()
c.update_id()

# get_id instance method
# update_id instance method