# Encapsulation :-
# encapsulation is the method of wrapping the data and their method into a single unit.
# Encapsulation is a fundamental concept in object-oriented programming(OOP) that involves building data (attributes) and methods (functions) that operate on the data into a single unit, typically a class. This concept helps in achieving data hiding and abstraction, which are essential for creating modular and maintainable code.

class Product(object):
    # instance method/ special method/ constructor
    def __init__(self,Product_Name,Product_Model,Product_Cost):
        self.pname = Product_Name # Public
        self.__pmodel = Product_Model # Private
        self.__pcost = Product_Cost # Private
        # print(self.pname,self.__pmodel,self.__pcost) # Mi Xiomi 1000

    def Display(self):
        print(self.pname,self.__pmodel,self.__pcost)

p = Product("Mi","Xiomi",1000) # Mi Xiomi 1000
p.Display()

print(p.pname)
# print(p.__pmodel) Attribute Error
# print(p.__pcost) Attribute Error

# mangling
print(p.pname)
# object Ref_className_PrivateAttribute

print(p._Product__pmodel) # Xiomi
print(p._Product__pcost) # 1000

# Task : Private method

class Hotel:
    def __init__(self):
        self.__BookRoom()
        self.__Orderfood()
    @staticmethod
    def __BookRoom():
        print("Room Booked Successfully")

    @staticmethod
    def __Orderfood():
        print("Food order successfully")

Hotel()
# Room Booked Successfully
# Food order successfully