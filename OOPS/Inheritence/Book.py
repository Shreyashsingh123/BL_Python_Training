class Book:
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
    
    # override __str__ method to display how object will be printed
    def __str__(self):
        return f"Name: {self.name}, Author is:{self.author}, Price is:{self.price}"
        
    def __gt__(self,other):
        return self.price>other.price
B1=Book("Virat Story","Shreyash Singh",1800)
print(B1)
# calling print B1 ill automatically call def__str__ method and print details
# if def__str is not overriden then it print in object like this <__main__.Book object at 0x000001DC29D6D150>

B2=Book("python","abc",200)
if B2 >B1:
    # if B2 >B1 it internally calls b1.__gt__(b2) and compares their prices(b1.price we written)
    print("B2 is costly")
else:
    print("B1 is costly")
