# Functions
# Functions are used for re-use ability
# We have two types of function 1. built-in functions, 2. User-defined function

# why we use functions?
# to store data we have variables, functions, methods, constructors, collections
#
product_id = 101
product_name = "Apple"
product_price = 10000
<<<<<<< HEAD

print(product_id, product_name, product_price)

product_id = 102
product_name = "Banana"
product_price = 1000

=======
print(product_id, product_name, product_price)
#
product_id = 102
product_name = "Banana"
product_price = 1000
>>>>>>> c0139113a5b939023e9f0d28e28fb3890f028b2c
print(product_id, product_name, product_price)

# to declare function in python use def keyword

def product_details(product_id, product_name, product_price):
    print(product_id, product_name, product_price)

# to call function use it using function name

product_details(100,"Apple",1000)
product_details(101,"banana",2000)

# Function Implementation
# Basics Functions
# 1. Create a function with zero arguments
# 2. Create a function with arguments
# 3. Create a function and pass default values
# 4. Create a function and arbitrary-arguments
# 5. Create a function and add return keyword
# 6. Create a function and pass global variables and local variables
# 7. Create a function and global keyword

# Advanced functions
# 1. Create an Inner FUnction
# 2. Create a Higher order functions
# 3. Create a Closure
# 4. Create a Decorator

# Advanced Build in functions(Iterables, Generators,comprehensions)
# Map(), Filters(), Reduce()
