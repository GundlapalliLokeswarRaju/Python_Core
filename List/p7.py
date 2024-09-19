#insert the data without insert()

l1 = [10, 20, 30,40, 50, 60, 70, 80, 90]
#      0   1   2  3   4   5   6   7   8

print(l1)
l1[3] = 400
l1[4] = 500
l1[5] = 600

print(l1)

l1[3:8:1] = 1000, 3000, 1000
print(l1)