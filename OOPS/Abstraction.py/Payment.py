from abc import ABC, abstractmethod
# abstract method must be implemented by its child class compulsory
# we can't create object of abstract class
# from abs module import ABC class and from ABC class use abstract method

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCard(Payment):
    def pay(self, amount):
        # if we give more arg here in pay method then abstraction exist but breaks polymorphism 

        print("Paid", amount, "using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class Wallet(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Wallet")

cc = CreditCard()
upi = UPI()
w = Wallet()
payments = [cc, upi, w]
for p in payments:
    p.pay(15000)
    # pay is overrided also same method name diffrent behaviour as object calling 
