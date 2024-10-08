# global keyword

#
def get_product_details():

    product_id = 101
    product_name = "Apple"
    product_price = 20000.0

    print(product_id,product_name,product_price)
get_product_details()

def get_product_details():
    global product_id
    product_id = 101
    product_name = "Apple"
    product_price = 20000.0

    print(product_id,product_name,product_price)
get_product_details()
print(product_id)
