# task 2: diff b/w pop() and remove()
# pop()
# pop can remove element from right side
l2 = [10, 20, 30, 40, 50]
print(l2.pop())  # 50
print(l2)  # [10, 20, 30, 40]
print(l2.pop())  # 40
print(l2)  # [10, 20, 30]
print(l2.pop())  # 30
print(l2)  # [10, 20]

# pop(index)
l3 = [10, 20, 30, 40, 50]
#      0   1   2   3   4
l3.pop(2)
print(l3)  # [10, 20, 40, 50]

# remove(element)
# remove,it can use to remove an items or elements
l4 = [10, 20, 3, 40, 50]
#     e1  e2  e3  e4  e5
#     i1  i2  i3  i4  i5
l4.remove(3)
print(l4)  # [10, 20, 40, 50]



lis = [int(input("0 index: ")),int(input("1 index: ")),int(input("2 index: ")),int(input("3 index: ")),int(input("4 index: ")),int(input("5 index: ")),int(input("6 index: ")),int(input("7 index: ")),int(input("8 index: ")),int(input("9 index: ")),int(input("10 index: ")),]
print(lis)
lis.pop(5)
print(lis)


