# Advanced functions
# 1. Create an Inner Function
# 2. Create a Higher order functions (pre: Functions, Inner function)
# 3. Create a Closure
# 4. Create a Decorator

# create an Inner Function without arguments
#Task 1:
def d1():
    print("d1 function outer function")

    def d2():
        print("d2 is inner function")

    d2()
d1()

# Task 2:
def d1(a,b):
    def d2():
        print(a+b, a-b, a*b, a/b)

    d2()

d1(10,20)

# Higher order function
# Higher order Function takes as an argument(1) or returns a function(1)
# Task 1: Function as argument
def d1(a):
    return a,a,a
print(d1(10)) # (10, 10, 10)

def d1(para1):

    return "d1 function", para1
print(d1(10))

# d1  need to call d2 function
def d1(para1,para2):
    return "d1 function", para1, para2

def d2():
    return "d2 function"

def d3():
    return "d3 function"

d = d1(d2(), d3())
print(d) # ('d1 function', 'd2 function', 'd3 function')

# Task 2: function as argument
def d1(a):

    return a
def d2(x, y):

    return print(x + y)

d1(d2(10, 20)) # 30

# Task 3: Returns a function
# to bring child() functions outside i should get permission from parent()
# by pass a variable to parent () we access child() function
# that variable will point to child directly

def parent():
    print("parent need to give permission to child")

    def child():
        print("child is waiting to get permissions")

    return child

parent() # parent need to give permission to child

p = parent()
p()

# o/p
# parent need to give permission to child
# child is waiting to get permissions

print(p.__name__) # child


# Task 4: returns a function with arguments
def d1(a, b):

    def d2():

        return a+b
    return d2

d = d1(10,20)
print(d()) # 30

# Task 5:
def d1(x):
    def d2(y):
        def d3(z):

            return x+y+z
        return d3
    return d2

d = d1(10)
dd = d(20)
ddd = dd(30)
print(ddd) # 60

d = d1(10)(20)(10)
print(d) # 40

def d1():

    print("This is d1")

    def d2():
        print("This is d2")

    return d2
a=d1()
print(a())

