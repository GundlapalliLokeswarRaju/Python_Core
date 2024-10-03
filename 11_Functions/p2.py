# Basics Functions
# 1. Create a function with zero arguments
# 2. Create a function with arguments
# 3. Create a function and pass default values
# 4. Create a function and arbitrary-arguments
# 5. Create a function and add return keyword
# 6. Create a function and pass global variables and local variables
# 7. Create a function and global keyword
from holoviews.core.dimension import redim


# 1. create a function with zero arguments
def d1():
    print("Hello World")
d1()
d1()
d1()

# 2. create a function with arguments
def d2(a, b):
    print(a, b)

d2(10, 20)
d2(100, 43)

# 3. create a function and pass default values

def d3(Username,pincode=523929):
    print(Username,pincode)

d3("Lokesh")
d3("Raju")
d3("Gundlapalli",516501)

# 4. create a function and pass arbitrary-arguments

def d4(color):
    print(color)
d4("red")
d4("orange")
def d4(*color):
    print(color)

d4("red","orange","pink")
# if single * use to get tuple
# if double ** use to get dictionary
def d4(**color):
     print(color)

d4(a="Orange",b="Apple",c="Banana")

# Create a function and add return keyword
def d5():
    return "Hello World"

print(d5())

def d5():
    return print("Hello World")

d5()

def d5():
    l1 = [ 10, 20, 30, 40, 50]
    return len(l1)

print(d5())