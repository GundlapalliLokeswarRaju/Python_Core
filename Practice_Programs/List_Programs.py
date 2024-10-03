# 1. Python program to interchange first and last elements in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
my_list[0],my_list[19] = my_list[19],my_list[0]
print(my_list)

# 2. Python Program to swap two elements in a list

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
ps_1, ps_2 = 1, 3
list[ps_1],list[ps_2] = list[ps_2],list[ps_1]
print(list)
b=[]
a = [[0,1,2],[1,2,3],[2,3,4]]
for i in a:
     if sum(i)!=3:
         b.append(i)
print(b)
import black.lines
from sympy.codegen.ast import continue_, break_

