# 1. Python program to Find Sum of Array
arr = [12, 13, 14, 15, 16, 17]
print(sum(arr))


# 2. Python program to find the largest number in an array
arr = [12, 13, 15, 121, 342, 21, 123, 131, 4232]
print(max(arr))

# 3. Python program for array rotation

a = [10, 20, 30, 40, 50, 60, 70, 80]
 #  [80, 70, 60, 50, 40, 30, 20, 10]
temp = []
temp.append(a[3])
a.pop(3)
a.extend(temp)
print(a)

# 4. Python Program to split the array and add the first part to the end
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
x = arr[:2]
y = arr[position:]
y.extend(x)
for i in y:
    print(i,end=" ")

# 5. Python Program for Find remainder of array multiplication divided by n
arr = [100, 10, 5, 25, 35, 14]
n = 11
count = 1
for i in arr:
    count *= i
print(count%n)

# 6. Python Program to check if given number is monotonic

arr = [5,15,20,10]
x,y = [],[] # take two empty lists
x.extend(arr)  # to store the items
y.extend(arr) # to store the items
x.sort() # ascending order
y.sort(reverse = True) # Descending order
if x==arr or y == arr:
    print(True)
else:
    print(False)
