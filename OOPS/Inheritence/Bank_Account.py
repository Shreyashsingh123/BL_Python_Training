from abc import ABC,abstractmethod
class Bank:
    def __init__(self,Accnum,balance):
        self.Acc=Accnum
        self.__balance=balance
    def getbal(self):
        return self.__balance
    def set_bal(self,new_bal):
        self.__balance=new_bal
    @abstractmethod
    def deposit(self,amt):
        pass
    @abstractmethod
    def withdraw(self,amt):
        pass
    @abstractmethod
    def check_bal(self):
        pass
class Saving(Bank):
    def __init__(self, Accnum, balance):
        super().__init__(Accnum, balance)
    def intrest(self):
        amt=self.getbal()+self.getbal()*0.1
        self.set_bal(amt)
        print("Amount after adding interest is: ",self.getbal())
    def deposit(self,amt):
        a=self.getbal()+amt
        self.set_bal(a)
        print(amt," deposited successfully in Saving account")
        print("Available balance is",self.getbal())
    def withdraw(self,amt):
        if amt<=self.getbal():
            new_amt=self.getbal()-amt
            self.set_bal(new_amt)
            print(amt," withdrawan successfully")
            print("Balance is",self.getbal())
        else:
            print("Insufficient balance")
    def check_bal(self):
        print("Available balance is",self.getbal())

class Current(Bank):
    def __init__(self, Accnum, balance):
        super().__init__(Accnum, balance)

    def deposit(self,amt):
        a=self.getbal()+amt
        print(amt," deposited successfully in Current account")
        self.set_bal(a)

    def withdraw(self,amt):
        if amt<=self.getbal():
            a=self.getbal()-amt
            self.set_bal(a)
            print(amt," withdrawan successfully from curent acc")
            print("Updated Balance is",self.getbal())
        else:
            print("Insufficient balance")
    def check_bal(self):
        print("Available balance is",self.getbal())

s1=Saving(12345,5000)
s2=Current(123,2500)
ls=[s1,s2]
s1.intrest()
for i in ls:
    i.deposit(1000)
    i.withdraw(1500)
    i.check_bal()