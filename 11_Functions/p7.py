# # # Decorator
# # Decorators are a powerful and flexible way to modify the behavior of functions or methods
#
# # # Task 1: Normal Function
# #
# # def d1(func):
# #     print(func)
# #
# # d1("Hello Python") # Hello Python
# # d = d1
# # print(d.__name__) # d1
# # d("hello Java") # hello Java
# #
#
# # Task 2:
# def d1(func):
#     def d2():
#         return "Hello Java", func()
#     return d2
# @d1
# def d3():
#     return "Hello Python"
# # d = d1(d3)
# # print(d())
# print(d3()) # ('Hello Java', 'Hello Python')
# #
# # Task 3:
# def d1(func):
#     def d2(a,b):
#         return func(a+b)
#     return d2
#
# @d1
#
# def d3(c):
#     return c
# d = d3
# print(d(10,30)) # 40
#
# def d4(c):
#     return c
# d = d1(d4)
# print(d(10,20)) # 30
# #
# Task 4: Need to Log in and Logout, Use if else and input function based on Decorator
#
# def d1(options):
#     options = {'Login', 'Logout'}
#     if options == 'login':
#
#         def login(email, password):
#             email = input("email: ")
#             password = input("password: ")
#             if email == 'lokeshgundlapalli@gmail.com' and password == 'lokesh9324':
#                 return "Login Successful"
#             else:
#                 return "incorrect email or password"
#         return login
#     elif options == 'logout':
#         def logout():
#             return "Logout Successful"
#         return logout
# @d1
# def d2(func):
#      pass
#
# print(d2())

# Decorator to decide between login and logout based on the user input
def d1(options):
    def d2(func):
        def d3():
            if options == 'login':
                return login()
            elif options == 'logout':
                return logout()
            else:
                return "Invalid action"
        return d3
    return d2

# Login function
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email == 'lokeshgundlapalli@gmail.com' and password == 'lokeshraju':
        return "Login Successful"
    else:
        return "Incorrect email or password"

# Logout function
def logout():
    return "Logout Successful"


options = input("Do you want to 'login' or 'logout'? ").lower()

@d1(options)
def d5():
    pass  # This function doesn't need to do anything, as the logic is in the decorator

# Calling the decorated function to perform the action
print(d5())













