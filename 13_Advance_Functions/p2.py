# Generators
# Generator is also iterator
# By using generators we can create our own iterations
# In generators we can use yield keyword
# In generator we don't use return keyword

# Task 1:
def d1():
    return 10
    return 20 # This code is unreachable
    return 30 # This code is unreachable
print(d1()) # 10

# Task 2:
def d2():
    yield 10
    yield 20
    yield 30
d = d2()
print(d) # <generator object d2 at 0x0000013C376D0580>
print(next(d)) # 10
print(next(d)) # 20
print(next(d)) # 30
print(next(d)) # StopIteration

def d4(n):
    for i in range(n):
        yield i
d = d4(100)
print(next(d))
print(next(d))
print(next(d))
# 0
# 1
# 2
