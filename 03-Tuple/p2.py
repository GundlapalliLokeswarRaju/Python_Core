# tuple vs list

l1 = [ 10, 20, 30, 40, 50, 60, 70, 10, 30]
l1[4] = 38
print(l1) #[10, 20, 30, 40, 38, 60, 70, 10, 30]

t1 = (10, 20, 30, 40, 38, 60, 70, 10, 30)
t1[0] = 300
print(t1) #'tuple' object does not support item assignment
