# Variable holds and stores the value
# python :
# function : Global V and Local V
# OOPS : Class V, Static V, Instance V
# Create a function and pass global variable and local variable
# Scope: Global V scope in the file
user_name = "lokesh" # global V

def user_details():
    # we can access global variable in the function scope and in the file scope
    # local variable are declare the inside the function
    # scope of the local v is inside the function
    user_email = "lokesh@gmail.com" # Local V
    print("Global V inside",user_name)
    print("local v : ", user_name)

user_details()

# we declare global v outside the function
print("Global V outside: ",)
