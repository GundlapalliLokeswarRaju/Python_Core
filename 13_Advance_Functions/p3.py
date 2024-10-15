# map(), filter(),Reduce()
# These are the built in functions. there are designed with  arguments.
# 1. Function , 2. Iterables
# if you are the modify the data then goto the map function.
#
# Task 1:- map(function, iterable)
l1 = [10, 20, 30, 40, 50, 60]
def d1(n):
    return n*2
m = map(d1, l1)
print(m) # <map object at 0x000001B001E1E530>
print(list(m)) # [20, 40, 60, 80, 100, 12

# Task 2:
l1 = [10,20,30,40,50]
l = lambda x:x*2
m = map(l, l1)
print(m) # <map object at 0x000001D20937E530>
print(list(m)) # [20, 40, 60, 80, 100]

# Task 3:-
print(list(map(lambda x:x*2,[10,20,30,40,50,60]))) # [20, 40, 60, 80, 100, 120]

# Task 4:-
print(list(map(lambda a,b:a*b,[10,20,30],[10,20,30]))) # [100, 400, 900]


