# Iterables:- sequence of elements and collection of elements
c = "Hello Python"
for i in c:
    print(i)
# H
# e
# l
# l
# o
#
# P
# y
# t
# h
# o
# n
# So list is an iterable

a = 10
for i in a:
    print(i) # TypeError: 'int' object is not iterable
# int is not an iterable

b = 20.02
for i in b:
    print(i) # TypeError: 'float' object is not iterable
# So float is a not iterable
from bokeh.sampledata.periodic_table import elements

# What is iterator ?
# iterator is an object. it contains two methods iter() and next() method.
#
l1 = [10, 20, 30, 40]
print(l1.__iter__()) # <list_iterator object at 0x000001BC0927E710>
print(dir(l1))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
# '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul = l__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
# '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
#
l = l1.__iter__()
print(l.__next__()) # 10
print(l.__next__()) # 20
print(l.__next__()) # 30
print(l.__next__()) # 40
print(l.__next__()) # Traceback StopIteration

l = [10, 20, 30, 40, 50]
l1 = iter(l)
print(next(l1)) # 10
print(next(l1)) # 20
print(next(l1)) # 30

l1 = [10,20,30,40,50,60,70]
results = iter(l1)
while True:
    try :
        elements = next(results)
        print(elements)
    except StopIteration:
        break

# 10
# 20
# 30
# 40
# 50
# 60
# 70