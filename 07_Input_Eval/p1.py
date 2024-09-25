# input() build-in function
# The nature of input is string
# Task1: Enter Your name:


user_name = input("Enter your name:")
print("your name is:", user_name)

# task 2:
user_name = input("Enter your name: ")
pass_word = input("Enter your password: ")

#Control Statements
# condition

if user_name == "sai" and pass_word == "Kiran":
    print("Logic Success")
else:
    print("Logic Failure")

# eval() build-in function
# the nature of eval is a data type casting.
# Task: Bank
user_name = input("Enter your name: ")
user_email = input("Enter your email: ")
user_account_no = 39445050140
user_contact = int(input("Enter your contact no:"))
user_balance = float(input("Enter your balance"))
print(user_name,user_email,user_account_no,user_balance,user_contact)
print(type(user_name),type(user_email),type(user_account_no),type(user_contact),type(user_balance))


# task 4: eval()
user_name = input("Enter your name: ")
user_email = input("Enter your email: ")
user_account_no = input("Enter your account number: ")
user_contact = input("Enter your contact no:")
user_balance = input("Enter your balance")

u_account_no = eval(user_account_no)
u_contact = eval(user_contact)
u_balance = eval(user_balance)
print(user_name,user_email,user_account_no,user_balance,user_contact)
print(type(user_name),type(user_email),type(user_account_no),type(user_contact),type(user_balance))

# Task 5: Addition
# if we perform addition using input() it concat the data
# if we perform addition using eval() it add the data.

a = input("Enter a: ") # 10
b = input("Enter b: ") #20
print(a+b) #1020

aa = eval(a)
bb = eval(b)
print(aa+bb) # 30

# Task 6: List
i1 = input("Enter List: ")
print(i1, type(i1))

e1 = eval(i1)
print(e1,type(e1))


l1 = [input('0 Index: '),input('1 Index: '),int(input("2nd Index: ")),input("3rd Index: ")]
print(l1, type(l1))

# Task 7: tuple
t1 = (input('0 Index: '),input('1 Index: '),int(input("2nd Index: ")),input("3rd Index: "))
print(t1, type(t1))

# Task 8: Set
s1 = {input('0 Index: '),input('1 Index: '),int(input("2nd Index: ")),input("3rd Index: ")}
print(s1, type(s1))

# Task 9: Dictionary

D1 = {
    'a1':input("Enter First value: "),
    'b1':input("Ënter Second value: ")

}
print(D1, type(D1))