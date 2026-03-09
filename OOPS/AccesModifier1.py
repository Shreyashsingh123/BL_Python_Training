class Person:
    __name="Anonymous"
    def __hello(self):
        # private method 
        print("hello person")
    def welcome(self):
        self.__hello()
p1=Person()
p1.welcome()
# p1.__hello()    it will show error as cannot access private member outside the class

# protected 

class Person2:
    def __init__(self,age):
        self._age=age
class Student(Person2):
    def display(self):
        print("Age is: ",self._age)
s=Student(25)
s.display()