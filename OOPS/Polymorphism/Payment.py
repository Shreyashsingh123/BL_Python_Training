class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Payment of {amount} done using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Payment of {amount} done using UPI")

class Wallet(Payment):
    def pay(self, amount):
        print(f"Payment of {amount} done using Wallet")

# Used Polymorphism as same method works diffrently in diffrent situation as called
         
payment1 =CreditCard()
payment2=UPI()
payment3=Wallet()
payment1.pay(500)
payment2.pay(10)
payment3.pay(1000)
# same method diffrent work method overriding or runtime polymorphism

