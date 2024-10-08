# Closure
# Closures are even higher order functions
# Closures rely on the nested functions
# The inner functions uses variables that are defined in the outer functions. These are called as free variables.
# Even after the outer functions has completed its execution, the inner function retains access to the free variables.

# # Task 1:
# def d1():

#     x = 10
#     print('d1 Scope: ',x)
#     def d2():
#         y = 20
#         print('d2 Scope: ', x)
#         print('d2 Scope: ', y)
#     return d2
# d=d1()
# d()
# print("Before")
# d()
# del d1
# print("After")
# d()
# print(d.__name__)

# # Task 2:
# def d1():
#     a = 10
#     print(a)
# d = d1
# d() # 10
# print(d.__closure__) # None
#

# # Task 3:
# def d1(a,b):
#     c = 30
#     d = 40
#     print("Scope d1: ",c)
#     def d2():
#         print('Scope d2: ', a)
#         print('Scope d2: ', b)
#         print('Scope d2: ', c)
#         print('Scope d2: ', d)
#         print(hex(id(a)),hex(id(b)),hex(id(c)),hex(id(d))) # 0x20c99ed0210 0x20c99ed0350 0x20c99ed0490 0x20c99ed05d0
#     return d2
# d = d1(10,20)
# d()
# print(d.__closure__) # (<cell at 0x000001B832355E10: int object at 0x000001B8321F0210>, <cell at 0x000001B832357640: int object at 0x000001B8321F0350>, <cell at 0x000001B832357700: int object at 0x000001B8321F0490>, <cell at 0x000001B832357790: int object at 0x000001B8321F05D0>)
# print(d.__code__.co_freevars) # ('a', 'b', 'c', 'd')


