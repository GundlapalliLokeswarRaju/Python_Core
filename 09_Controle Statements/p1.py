# Types of control statements
# 1. Selection Statements :- if Else elis match
# 2. Iteration statement :- for, while
# 3. Transfer statement :- break and continue
# task 1:- if condition with boolean value

if True:
    print("Condition Passed")
    a = 10
    print(a)
if False:
    print("Condition passed") # the code is unreachable
    b = 20
    print(b)


# TAsk 2:- if condition with operators
a = 5
b = 10
if a<b:
    print("if condition") # if condition
else:
    print("else block")

# Task 3:- Logic operators

user_name = input("Enter Your Name: ")
pass_word = input("Enter Your Pass_word: ")
if user_name == "admin" and pass_word == "admin":
    print("Login Success")
else:
    print("Login Failure")

# test case 1:
# Enter Your Name: lokesh
# Enter Your Pass_word: raaju
# Login Failure
# test case 2:
# Enter Your Name: admin
# Enter Your Pass_word: admin
# Login Success

# Task 4:- Elif

user_salary = float(input("Enter Your Salary: "))
if user_salary <= 10000:
    print("The salary ranges between o and 10000 ",user_salary)
elif user_salary <= 20000:
    print("The salary ranges between 10000 and 20000: ",user_salary)
elif user_salary <= 30000:
    print("The salary ranges between 20000 and 30000: ", user_salary)
elif user_salary <= 40000:
    print("The salary ranges between 30000 and 40000: ", user_salary)
elif user_salary <= 50000:
    print("The salary ranges between 40000 and 50000: ",user_salary)
else:
    print("The salary is more than 50000: ", user_salary)

# Test case :1
# Enter Your Salary: 100000
# The salary is more than 50000:  100000.0
# Test case :2
# Enter Your Salary: 35000
# The salary ranges between 30000 and 40000:  35000.0

# Task 5: match case
# function are used for re-use-ability
status_code = int(input("Status code: "))
match status_code:
    case 200:
        print("OK")
    case 201:
        print("CREATED")
    case 202:
        print("ACCEPTED")
    case 203:
        print("NO CONTENT")
    case _:
        print("No Matching Status Code")

# For Loop:
l1 = [10, 20, 30, 40, 50]
print(l1) # [10, 20, 30, 40, 50]
print(list(l1)) # [10, 20, 30, 40, 50]
for i in l1:
    print(i)

# OUTPUT
# 10
# 20
# 30
# 40
# 50
#
# String
s1 = "Hello World"
for i in s1:
    print(i)
# Output
# H
# e
# l
# l
# o
#
# W
# o
# r
# l
# d

# int,float,complex
a = 10
for i in a:
    print(i) # 'int' object is not iterable


for i in range(10):
    print(i)

for i in range(10,0,-1):
    print(i)

d1 = { 10:20, 20:30, 30:40}
# for i in d1:
#     print(i) # 10 20 30
for i in d1.items():
    print(i)
for i in d1.values():
    print(i)
for i in d1:
    print(i)
# While Loop
# Unreachable call
while False:
    print("Condition check")
while True:
    print("Condition check")

 # Assignment Operators
i = 1
while i<10:

    print(i)
    i+=1


# Reverse Number
i = 10
while i >= 1:
    print(i)
    i -= 1
#

while True:
    user_salary = float(input("Enter Your Salary: "))
    if user_salary <= 10000:
        print("The salary ranges between o and 10000 ",user_salary)
    elif user_salary <= 20000:
        print("The salary ranges between 10000 and 20000: ",user_salary)
    elif user_salary <= 30000:
        print("The salary ranges between 20000 and 30000: ", user_salary)
    elif user_salary <= 40000:
        print("The salary ranges between 30000 and 40000: ", user_salary)
    elif user_salary <= 50000:
        print("The salary ranges between 40000 and 50000: ",user_salary)
    else:
        print("The salary is more than 50000: ", user_salary)

    repeat = input(f"Do you want to continue or stop? Yes/ No ").lower()
    if repeat != 'yes':
        break

l1 = []
while True:
    l1.append(input("Enter a value: "))
    repeat = input(f" Do you want to continue or stop,? yes/no: ").lower()
    if repeat != "y":
        break
print(l1)

# # Break : to stop the iteration
# # Continue : To Skip the iteration
#
for i in range(10):
    if i ==5:
        continue
    elif i == 8:
        break
    print(i)
