# method overriding
# Two classes use inheritance and same method and same arguments. called method overriding.
class Parent:
    def d1(self,a,b):
        print("parent:",a,b)

class Child(Parent):
    def d1(self,a,b):
        print("Child: ",a, b)

c = Child()
c.d1(10,30)
p = Parent()
print(p.d1(10,20))