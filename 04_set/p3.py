# task 3: clear() and copy()

s1 = {10, 20, 30, 40, 50}
print(s1) #{10, 20, 30, 40, 50}
s1.clear()
print(s1) #set()


s2 = set({10, 20, 30, 40, 50})
s2.copy()
print(s2)# {50, 20, 40, 10, 30}