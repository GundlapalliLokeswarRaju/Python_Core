# Constructor overloading
# what is special method/ constructor
# special method is executed at the time object creation.
from torch.fx.experimental.unification.dispatch import dispatch


class Product:
    def __init__(self):
        print("Special method")

# object (object name and class name must be same)
# one class is same but with different arguments.
Product() # Special method

class Product:
    # methods
    @dispatch(int,int)
    def __init__(self,a,b):
        print(a,b)
    @dispatch(int,int,int)
    def __init__(self,a,b,c):
        print(a,b,c)

Product(10,20)
Product(10,20,30)
