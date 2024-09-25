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
