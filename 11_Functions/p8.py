# lambda()
# Syntax: lambda argument : Expression
# Task 1:
def d1(a):
    return print(a)
d1(10) # 10

l1 = lambda a : print(a)
l1(10) # 10

# Task 2:
# Normal Function
def d1(a, b):
    return print(a+b, a*b, a-b, a/b)
d1(10, 20) # 30 200 -10 0.5

l1 = lambda a,b : print(a+b, a-b, a*b, a/b)
l1(10,20) # 30 -10 200 0.5

# Task 3: Assign lambda function to a variable
l1 = lambda a,b: a+b
l = l1(10,20)
print(type(l1)) # <class 'function'>
print(l) # 30
print(type(l)) # <class 'int'>

# Task 4: Arbitrary arguments *, **

l1 = lambda *a:print(a)
l1(10,20,30,40,50) # (10, 20, 30, 40, 50)

l2 = lambda **a: print(a)
l2(a=10, b=20, c=30, d=40, e=50) # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

# Task 5: Higher Order Functions
def d1(a=10):
    def d2(b):
        return a+b
    return d2
d = d1()
print(d(20)) # 30

l1 = lambda a = 10:lambda b:a+b
l = l1()
print(l(20)) # 30


# Task 6: lambda using if else condition

l1 = lambda a,b: a if a>b else b
print(l1(5,10)) # 10
print(l1(10,5)) # 10

def d1(a):
    def d2(b):
        if a>b:
            return a
        else:
            return b
    return d2
d = d1(10)(5)
print(d) # 10
