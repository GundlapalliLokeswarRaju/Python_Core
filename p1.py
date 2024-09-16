product_id = 23456
#product_name = 'eggs'
product_name = ['eggs','banana']
product_price = 100.00
product_quantity = 12

user_name = 'sai kiran'
user_contact = 8374705188
user_address = "hyd"
user_pincode = 516501
print(product_id, product_name, product_price, product_quantity)
print(user_name, user_contact, user_address, user_pincode)

print(type(product_id),type(product_name), type(product_quantity), type(product_price))
#< class 'int'><class 'str'> <class 'int'> <class 'float'>
#when we pass data type in python it returns the class name
print(int, float, bool, complex)
# object: object is instance of a class, class name and object name must be same
# when we pass obejct we get default values

print(int(), float(),bool(), complex())

print(str())

print(list(),tuple(),set(),frozenset()) # [] () set() frozenset()


print(dict()) #{}

print(range(0))#range (0,0)

print (bytes(),bytearray()) # b'' bytearray(b'')

# class: it is a blueprint of a template, in class we have properties and method



