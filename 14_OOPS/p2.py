# Multilevel Inheritance
# in multilevel inheritance is a intermediate class derives properties from base class, and a derived class inherits a properties from intermediate class.
# Like Grandfather -> Father -> Child
class grand_parent:
    # instance method
    def d1(self):
        print("d1 instance method")
    # static method
    @staticmethod
    def d2():
        print("d2 is static method")
    # class method
    @classmethod
    def d3(cls):
        print("d3 is class method")

class parent(grand_parent):
    def d4(self):
        print("d4 is instance method")

class child(parent):
    def d5(self):
        print("d5 is instance method")

c = child()
c.d5()
c.d4()
c.d3()
c.d2()
c.d1()

# d5 is instance method
# d4 is instance method
# d3 is class method
# d2 is static method
# d1 instance method