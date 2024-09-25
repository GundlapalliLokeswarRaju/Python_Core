# count(), clear(), sort()
# count : Finding the same occurrences
l1 = [10, 20, 30, 40, 50, 10, 20, 30]
print(l1.count(10))

print(l1.count(50))

print(l1.count(100))


l1.clear() # clear the entire List
print(l1)

#Sort()

l1 = ['b','a','r','o']
#insertion order
print(l1)
l1.sort()
print(l1)
l1.sort(reverse = True)
print(l1)