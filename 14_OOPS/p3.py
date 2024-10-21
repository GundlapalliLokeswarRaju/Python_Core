# Multiple Inheritance
# A class can be derived from more than one base class, this type of inheritance is called multiple inheritance

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

class parent:
    def d4(self):
        print("d4 is instance method")

class child(parent,grand_parent):
    def d5(self):
        print("d5 is instance method")


# 5 methods
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

# one method
p = parent()
p.d4()
# d4 is instance method

# 3 methods
g = grand_parent()
g.d1()
g.d3()
g.d2()

# d1 instance method
# d3 is class method
# d2 is static method