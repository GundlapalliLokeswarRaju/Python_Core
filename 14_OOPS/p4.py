# hierarchical inheritance
# when more than one derived class from a single base class.
# icici, Bank, Axis Bank, SBI Bank, RBI
class grand_parent:
    def d1(self):
        print("d1 method")
class parent(grand_parent):
    def d2(self):
        print("d2 method")
class child_one(grand_parent):
    def d3(self):
        print("d3 method")
class child_two(grand_parent):
    def d4(self):
        print("d4 method")

g = grand_parent()
g.d1()
# d1 method
p = parent()
p.d1()
p.d2()
# d1 method
# d2 method
c1 = child_one()
c1.d3()
c1.d1()
# d3 method
# d1 method

c2 = child_two()
c2.d1()
c2.d4()
# d1 method
# d4 method1






