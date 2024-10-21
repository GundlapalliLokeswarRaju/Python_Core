# method overloading
# one class is enough for method overloading.
# can have same method name and arguments must be different.

from multipledispatch import dispatch

class Product:
    # methods : instance method, static method, class method
    # instance method
    def product_details(self, product_id, product_name):
        print(product_id, product_name)

    def product_details(self,product_id,product_name,product_price):
        print(product_id,product_name,product_price)


Product().product_details(101,"laptop")


# if we can't use the decorator then type error will be occurred. TypeError: Product.product_details() missing 1 required positional argument: 'product_price'
# Then we use decorator of @dispatch will throw the output.

class Product:
    # methods : instance method, static method, class method
    # instance method
    @dispatch(int,str)
    def product_details(self, product_id, product_name):
        print(product_id, product_name)

    @dispatch(int,str,float)
    def product_details(self,product_id,product_name,product_price):
        print(product_id,product_name,product_price)


Product().product_details(101,"laptop")
Product().product_details(101,"lokesh",109.9)