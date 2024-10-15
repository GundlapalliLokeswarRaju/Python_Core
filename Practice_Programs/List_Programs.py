# # 1. Python program to interchange first and last elements in a list
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# my_list[0],my_list[19] = my_list[19],my_list[0]
# print(my_list)
#
# # 2. Python Program to swap two elements in a list
#
# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# ps_1, ps_2 = 1, 3
# list[ps_1],list[ps_2] = list[ps_2],list[ps_1]
# print(list)
# b=[]
# a = [[0,1,2],[1,2,3],[2,3,4]]
# for i in a:
#      if sum(i)!=3:
#          b.append(i)
# print(b)
#
# # 3. Python program to find N largest elements from a list
# data = [4, 5, 1, 2, 3]
# n = int(input("N = "))
# data.sort()
# print(data[-n:])
# # O/P :-
# # N = 2
# # [4, 5]
#
# def nmaxelements(list1,N):
#     final_list = []
#     for i in range(0,N):
#         max1 = max(list1)
#         list1.remove(max1)
#         final_list.append(max1)
#
#     print(final_list)
#
# list1 = [1,2,8,4,9,4,68,45,85,41,35,458,545,5445]
# N = 3
#
# nmaxelements(list1,N) # [5445, 545, 458]
#
# # 4. Python program for print even numbers in a list
# a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20]
# for i in a:
#     if i%2!=0:
#         a.remove(i)
# print(a) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# # example with function
# def even(A):
#     even_list = []
#     for i in A:
#         if i%2 == 0:
#             even_list.append(i)
#     return even_list
# A = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20]
# print(even(A)) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# # 5. Python program for print odd numbers in a list
# a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20]
# b = []
# for i in a:
#     if i%2!=0:
#         b.append(i)
# print(b) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# # example with function
# def odd(A):
#     odd_list = []
#     for i in A:
#         if i%2 != 0:
#             odd_list.append(i)
#     return odd_list
# A = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20]
# print(odd(A)) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# # 6. Python program to print all even numbers in a range
# start = int(input("Start = "))
# end = int(input("End = "))
# for i in range(start,end):
#     if i%2 == 0:
#         print(i,end=" ") # 4 6 8 10 12 14
#
# # 7. python program to print odd numbers in range
# start = int(input("start: "))
# end = int(input("end: "))
# for i in range(start,end):
#     if i%2 != 0:
#         print(i,end=" ")
# # 8. python program for print positive numbers in a list
# lis = [ 1, 2, 3, -1, -5, -10, -11, -123]
# for i in lis:
#     if i<=0:
#         continue
#     print(i,end=" ") # 1 2 3
# # 9. remove multiple elements from a list in python
# lis = [1, 2, 3, 4, 5, 123]
# de = [1, 2, 4]
# for i in de:
#     if i in lis:
#         lis.remove(i)
# print(lis) # [3, 5, 123]
#
# # 10.Remove empty list from a list in python
#
# l1 =[[1,2,3,4],[1,2,3],[ ]]
# for i in l1:
#     if len(i)==0:
#         continue
#     print(i)
# # o/p
# # [1, 2, 3, 4]
# # [1, 2, 3]
#
# # 11. Python|cloning or copying a list
#
# l2 = [10, 20, 30, 40, 50, 60, 70, 80]
# l3 = l2[:]
# print(l2) # [10, 20, 30, 40, 50, 60, 70, 80]
# print(l3) # [10, 20, 30, 40, 50, 60, 70, 80]
#
# # 12. python| count occurrence of an element in a list
# l2 = [1, 2, 3, 1, 2, 5, 6, 8, 9, 10, 3, 1, 2, 1, 3, 2, 10]
# print(l2.count(1)) # 4

# # 13. python| remove empty tuple in a list
#
# lt1 = [(1,2,3),(4,32,1),()]
# a = (1,2,3)
# for i in lt1:
#     if len(i)==0:
#         continue
#     print(i)
# # O/P:
# # (1, 2, 3)
# # (4, 32, 1)

# # 14. Python| Program to print duplicates from a list of integers
#
# l2 = [1, 2, 3, 1, 2, 5, 6, 8, 9, 10, 3, 1, 2, 1, 3, 2, 10]
# l3 = []
# for i in l2:
#     if i not in l3:
#         l3.append(i)
#     else:
#         l2.remove(i)
# print(l3) # [1, 2, 3, 5, 6, 8, 9, 10]
# # Python| Program to print duplicates from a list of integers
#
# l2 = [1, 2, 3, 1, 2, 5, 6, 8, 9, 10, 3, 1, 2, 1, 3, 2, 10]
# print(list(set(l2))) # [1, 2, 3, 5, 6, 8, 9, 10]

# # 15. python program to find cumulative sum of a list
#
# li = [10, 20, 30, 40, 50, 60, 70]
# new = []
# le = len(li)
# count = 0
# for i in range(0,le):
#     count = count+li[i]
#     new.append(count)
#
#
# print(new) # [10, 30, 60, 100, 150, 210, 280]

# 16. sum of number digits in list
a = [12, 13, 15]

b=str(a)
c = []
for i in a:
    count = 0
    for j in str(i):
        count += int(j)
    c.append(count)
print(c)
# [3, 4, 6]