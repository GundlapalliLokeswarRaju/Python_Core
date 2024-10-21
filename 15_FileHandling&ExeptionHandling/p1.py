# # FileHandling & Exception Handling
# # Exception Handling
# # Exception:- an unwanted exception that disturbs the normal flow of program is called exception.
# from dask.dataframe.io.demo import names
#
# # a = 10
# # b = 0
# # print("before")
# # print(a/b) # ZeroDivisionError: division by zero
# # print("after")
#
# # try, except, finally keywords
# try:
#     a = 10
#     b = 0
#     print("before")
#     print(a/b)
# except ZeroDivisionError as e:
#     print(e)
# print("after")
#
# # before
# # division by zero
# # after
#
# # try block is used for business logic
# # except block is used for to handle the exceptions
# # finally block is used for closing the connections.
# # Task 1: create file and insert the data.
# f = None
# try:
#     f = open('one.txt','w')
#     s = input('enter  some text: ')
#     f.write(s)
#     print("file created and data inserted")
# except FileNotFoundError as e:
#     print("exception is: ",e)
#
# finally:
#     f.close()
# #
# #
#
# # Task2: Read the data from file.
# f = None
# try:
#     f = open('one.txt','r')
#     s = f.read()
#     print(s) # hi hello how are you guys. don't be fear.
#
# except FileNotFoundError as e:
#     print("Exception ", e)
# finally:
#     f.close()
# # Task 3:- write and read the data using writelines method.
#
# f = None
# try:
#     f = open('list.txt','w')
#     s = input("Enter Text Here: ")
#     f.writelines(s)
#     print("Data inserted")
#
#     f = open('list.txt','r')
#     for i in f:
#         print(i) # hi this is lokesh. and I am from kadapa district. I complete my b.tech in the year of 2020 to 2024 in guntur. i am from computer science background. i got 74% percentage in my all semisters.
# except FileNotFoundError as e:
#     print("Exception ", e)
#
# finally:
#     f.close()
from nbformat.current import reads
from numba.cuda.printimpl import print_item

# # Task 4:- Write and read the data using writelines method, but don't use finally block.
#
# try:
#     with open('list.txt','w') as f:
#         l1 = ['NameOne','NameTwo','NameThree','NameFour']
#         f.writelines('\n'.join(l1))
#         print('Data inserted')
#
#     with open('list.txt','r')as f:
#         for i in f:
#             print(i.strip())
#
#
# except FileNotFoundError as e:
#     print("exception is: ",e)
#
# # Tell(): tell this method returns the current position of the file.
#
# try:
#     f = None
#     try:
#         f = open('two.txt','w')
#         s = input("Enter Text here: ")
#         f.write(s)
#     except FileNotFoundError as e:
#         print("Exception is: ",e)
#     finally:
#         f.close()
#
#     try:
#         f = open("Two.txt","r")
#         print(f.tell())
#         print(f.read())
#         print(f.tell())
#
#     except FileNotFoundError as e:
#         print("Exception is: ",e)
#
#     finally:
#         f.close()
# except FileNotFoundError as e:
#     print("Exception is: ",e)
#


# Task 6:- How to tranger data from one to other file.

try:
    f = open('list.txt','r')
    data = f.read()
    f1 = open('list_two.txt','w')
    f1.write(data)
    print("file is created")
    f.close()
    f1.close()

except FileNotFoundError as e:
    print('Exception :',e)

try:
    f = open('list_two.txt','r')
    rwe = f.read()
    print(rwe)


except FileNotFoundError as e:
    print('Exception',e)