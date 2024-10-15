# Comprehension :- Comprehension means creating new data from the exiting data.
# List Comprehension
# Set Comprehension
# Dictionary Comprehension
# Generator Comprehension

# List Comprehension
# Task 1: Find the range using list()
l1 = list(range(1, 10))
print(l1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Task 2: Find the square root without using comprehension
for i in range(1,11):
    print(i**2,end=" ") # 1 4 9 16 25 36 49 64 81 100

# Task 3: Find Square root with list comprehension

lis = [i**2 for i in range(1,11)]
print(lis) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Task 4: Using if condition

lis = [i**2 for i in range(1,21) if i%2==0]
print(lis) # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

# task 5: Using nested if condition

lis = [i**2 for i in range(50) if i%2==0 if i%5==0]
print(lis) # [100, 400, 900, 1600, 2500]

# Task 6: if else condition
names = ['admin','admins','admin','adina']
l1 = [i if i == 'admin' else 'Not Admin' for i in names ]
print(l1) # ['admin', 'Not Admin', 'admin', 'Not Admin']

# Task 7: Nested for loop
l = [x+y for x in (1, 2, 3) for y in (3,2,1)]
print(l) # [4, 3, 2, 5, 4, 3, 6, 5, 4]