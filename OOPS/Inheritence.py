class Animal:
    def barks(self):
        print("Animal barks")
class dog(Animal):
    def dog_bark(self):
        print("Dog barks")
d1=dog()
d1.barks()
d1.dog_bark()

# inheriten and constructor with super keyword
class Animal1:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("name is : ",self.name)
class Cow(Animal1):
    def __init__(self, name,price):
        super().__init__(name)
        self.price=price
    def display(self):
        print("price is",self.price)

c=Cow("Cow1",25000)
c.show()
c.display()

    