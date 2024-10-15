s = (i ** 2 for i in tuple(range(1, 10)))
print(s) # <generator object <genexpr> at 0x000001E702590580>
print(tuple(s)) # (1, 4, 9, 16, 25, 36, 49, 64, 81)