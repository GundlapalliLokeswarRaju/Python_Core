import cmath
# 1. Write a python program for print 4 multiples in given list
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
b = []
for i in a:
    if i%4 == 0:
        b.append(i)
print(b)

#
# 2. print prime numbers in given list
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 89, 12, 32, 43, 86, 223, 232,123, 553,2424]

new_prime = []
not_prime = []
for a in num:
    if a==1 or a == 0:
        not_prime.append(a)
        continue

    for j in range(2,a//2+1):
        if a%j == 0:
            not_prime.append(a)
            break
    else:
        new_prime.append(a)
print("Prime_List = ",new_prime)
print("Not_Prime = ",not_prime)

# 3. check given number is prime or not
count = 0
num = int(input("Enter Number: "))
for i in range(1,num+1):
    if num%i==0:
        count += 1
if count ==2:
    print("prime")
else:
    print("not prime")

# 4. write a program to print first 100 prime numbers
a = []
for i in range(2,10000):
    for j in range(2, 10000):
        if i%j == 0:
            break
    if  i == j:
        a.append(i)

print(a[0:100])

# 5. print fibonacci series in list formate
first_num = 0
second_num = 1
a = [0, 1]
num = int(input("Enter a number: "))

for i in range(0,num+1):
    next_digit = first_num + second_num
    first_num = second_num
    second_num = next_digit
    i += 1
    a.append(next_digit)
print(a)

# 6. How to remove duplicates in the list
a = [10,20,330,22,32,11,11,22,11]
b = set(a)
print(sorted(list(b)))

# 7. print factorial of the number
num = int(input("Enter Number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
    print(i,'=',fact)

# 8. Find the square root of the number

num = int(input("Enter Number: "))
print(num ** 0.5)

# 9. Find the area of the triangle
height = int(input("H: "))
Base = int(input("B: "))
print(1/2*(height*Base))

# 10. Find the values of Quadratic Equations
# The formula of the Quadratic equation is (-b +-(b**2 - 4*a*c)** 0.5)/(2*a)
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

d = (b**2 - 4*a*c)

sol_1 = (-b +cmath.sqrt(d))/(2*a)
sol_2 = (-b -cmath.sqrt(d))/(2*a)

print(sol_1)
print(sol_2)

# How to find Factorial
import math


a = math.factorial(10)
print(a)


# python program for simple interest

p = float(input("Price: "))
t = int(input("Time: "))
r = int(input("Rate: "))
interest = p * t * r / 100
print("interest: ",interest)
print("Total amount = ",p+interest)

# compound Interest
A = p*(1 + r/100)**t
int = A - p
print(int) #26824.179456254555, 34019.54549126804


# To check Given number is Arm strong number or not
n = 153 # to assign a value n = 153
a = n # assigning input value to the 'a' variable
count = 0
while n != 0:
    r = n % 10
    count = count + (r ** 3)
    n //= 10
print(count == a)
#
# To Find Area of Circle
r = int(input("Enter radius of circle: "))
area = 3.142*(r*r)
print(area)

# Python program to print all prime numbers in an interval

l1=[]
prime = []
not_prime = []
while True:
    l1.append(int(input("Enter Number: ")))
    repeat = input(f"If you are continue or not.? Yes/No ").lower()
    if repeat != 'y':
        break
print(l1)
for i in l1:
    if i == 0 or i ==1:
        not_prime.append(i)
        continue
    for j in range(2,i//2+1):
        if i%j == 0:
            not_prime.append(i)
            break
    else:
        prime.append(i)
print("Not Prime: ",not_prime)
print("Prime: ",prime)

# Python program for n-th Fibonacci number
num = int(input("Enter a Number: "))
First_number = 0
Second_number = 1
for i in range(0,num+1):
    next_num = First_number + Second_number
    First_number = Second_number
    Second_number = next_num
print(next_num)

# Python program for how to check if a given number is fibonacci number?
num = int(input("Enter a Number: "))
First_number = 0
Second_number = 1
a = []
for i in range(0,num+1):
    next_num = First_number + Second_number
    First_number = Second_number
    Second_number = next_num
    a.append(next_num)
print(num in a)

# Program to print ASCII Value of a character
a = 'g'
print("The ASCII Number",ord(a))
# ASCII - American Standard Code for Information Interchange

# Python Program for Sum of squares of first natural numbers

num = int(input("Enter Number: "))
count = 0
for i in range(1,num+1):
    count = count+(i**2)
print(count)

# Python Program for cube sum of first n natural numbers

num = int(input("Enter Number: "))
count = 0
for i in range(1,num+1):
    count = count+(i**3)
print(count)
