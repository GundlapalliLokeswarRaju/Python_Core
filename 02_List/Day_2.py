# List
# We can create list using square bracket [], and object list()
# It will maintain order, and also it allows duplicates
# In list we can store any data types
# In list all the items/elements we store them in index based position. (index starts from 0)

# task: insertion order, duplicates
l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(l1)  # [10, 20, 30, 40, 50, 60, 70, 80, 90]

l1 = list([10, 20, 30, 40, 50, 60, 70, 80, 90, 30, 40, 50])
print(l1)
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 30, 40 ,50]

# task 2: in list we store any data type

l2 = [10, 10.0, True, 10j, 'NameOne']
print(l2)  # [10, 10.0, True, 10j, 'NameOne']

# task 3: find the element using index position
l3 = [10, 20, 30, 40, 50, 60, 20, 70, 80]
#      0   1   2   3   4   5   6   7   8
print(l3[6], l3[3])  # 20 40

print(l1[5])  # 60
# task 4: find the length of the list
l4 = [10, 20, 30, 40, 50, 60, 20, 70, 80]
#      0   1   2   3   4   5   6   7   8 : index
#      1   2   3   4   5   6   7   8   9 : Length (len())
print(len(l4))  # 9

# task 5: best practices
# when we pass data type it will be return the class name
# when we pass object it will be the default value
l5 = [int, float, bool, complex, str, list, tuple, set, frozenset, map, bytes, range]
print(
    l5)  # [<class 'int'>, <class 'float'>, <class 'bool'>, <class 'complex'>, <class 'str'>, <class 'list'>, <class 'tuple'>, <class 'set'>, <class 'frozenset'>, <class 'map'>, <class 'bytes'>, <class 'range'>]
l6 = [int(), float(), bool(), complex(), str(), list(), tuple(), set(), frozenset(), bytes()]
print(l6)  # [0, 0.0, False, 0j, '', [], (), set(), frozenset(), b'']

# task 6: can you multply both list given

l1 = [10, 20, 30, 40, 50]
l2 = [10, 20, 30, 40, 50]
print(l1 * l2)  # can't multiply sequence by non-int of type 'list'

# task 7: can you multiple the given list by any value
# repetition
l7 = [10, 20, 30, 40, 50]
print(l7 * 1)  # [10, 20, 30, 40, 50]
print(l7 * 2)  # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
print(l7 * 3)  # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

# task 8: can add both list given
# concatenation
l8 = [10, 20, 30, 40, 50]
l9 = [10, 20, 30, 40, 50]
print(l8 + l9)  # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

# task 9: how to get the half portion of the data from the list
# slicing
# variable [start(0): end(-1): step-over(1)]
l9 = [10, 20, 30, 40, 50, 10, 20, 60, 70, 80, 90]
#      0   1   2   3   4   5   6   7   8   9  10

print(l9[0:5])  # [10, 20, 30, 40, 50]

print(l9[0:5:2])  # [10, 30, 50]

# task 10 : perform slicing on negative numbers
# diff b/w list and tuple

# Task 11 : list is mutable/unsafe
l11 = [10, 20, 30, 40, 50]
l11[0] = 100
print(l11)

# Task 12 :  tuple is immutable/ safe
l12 = (10, 20, 30, 40, 50)
l12[0] = 100
print(l12)  # TypeError: 'tuple' object does not support item assignment

