# Task 3:-
from abc import ABC, abstractmethod

from tensorflow.compiler.tf2xla.python.xla import self_adjoint_eig


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# concrete class

class CreditCardPayments(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using credit card")

# concrete class
class PayPalPayments(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Paypal")

# Object
payment1 = CreditCardPayments()
payment2 = PayPalPayments()
# payment1.pay(100)
# payment2.pay(200)

# Client code
def process_payment(payment_method,amount):
    payment_method.pay(amount)

process_payment(payment1,12231)
process_payment(payment2,31233)