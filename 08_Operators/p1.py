# 1. Arithmetic operator : +, _, *, /, //, **, %

a = 10
b = 20
c = 30
d = 40

print(a+b) # 30
print(a-b) # -10
print(a*b) # 200
print(c/d) # 0.75 (Co-efficient value)
print(c//d) # 0 (with out floating point of Co-efficient value)
print(d%a) # 0 (Remainder)
print(a%b) # 10
print(d%c) #10

print(2 ** 5) # 32

# 2. Assignment Operators +=, -=, *=, /=, //=, **=, %=

a = 10
b = 20
c = 30
d = 40

a += 1
print(a) # 11
b -= 10  # 10
print(b)
c *= b   # 300
print(c)
d /= c   # 0.1333333333333333
print(d)
a //= d  # 82.0
print(a)
a **= 2 # 6724.0
print(a)

c %= b # 0
print(c)

# 3. Comparison Operator <, >, <=, >=, ==, !=

a = 10
b = 5
c = 20

print(a<b) # False
print(a>b) # True
print(b>c) # False
print(c <= a) # False
print(a>=c) # False
print(2*a==c) # True
print(a!=c) # True

# 4. Logical Operators :- and, or, not
# and : both conditions must be satisfied
# or : even one condition is satisfied
# not : The 'not' operator in Python is a logical operator used to invert the truth value of a given object or expression.
# When applied to a Boolean value, if the operand is True, the result will be False, and vice versa
print(True and False) # False
print(True and True) # True
print(False and True) # False
print(False and False) # False
print(True or False) # True
print(True or True) # True
print(False or True) # True
print(False or False) # False
a = True
print(not a) # False

# # 5. Membership Operator :- in, not in
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(10 in l1) # True
print(100 in l1) # False
print(1000 not in l1) # True
print(5 not in l1) # False

# 6. Identity operator :- is, ==
# IS : IT CHECKS COMPARISON REFERENCE
# == : it checks content comparison

l1 = [10, 20, 30, 40, 50]
l2 = [10, 20, 30, 40, 50]
l3 = l2

print(l1 is l2) # False
print(l2 is l3) # True
print(l2 == l3) # True
print(l1 == l3) # True
print(id(l1),id(l2), id(l3)) #2014948598272 2014948481664 2014948481664
print(id(l2) == id(l3)) # True
