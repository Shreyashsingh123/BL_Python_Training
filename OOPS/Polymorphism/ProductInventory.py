class Product:
    def __init__(self,id,name,price,quantity):
        self.id=id
        self.name=name
        self.price=price
        self.quantity=quantity
    def display(self):
        return f"Id: {self.id} Name: {self.name} price: {self.price} Quantity: {self.quantity}"
    def update(self,new_quan):
        self.quantity=new_quan

class Inventory:
    def __init__(self):
        self.dict={}
    def add_Product(self,product):
        if product.id not in self.dict:
            self.dict[product.id]=product
            print("product added successfully")
        else:
            print("product is present")
    def update(self,id,quantity):
        if id in self.dict:
            self.dict[id].update(quantity)
            print("contact updtaed successfully")
        else:
            print("id not present")
    def delete(self,id):
        if id in self.dict:
            del self.dict[id]
            print("Contact delted successfully")
        else:
            print("id not present")
    def displayAll(self):
        if not self.dict:
            print("no product is available")
        else:
            for i in self.dict.values():
                print(i.display())
    def searchId(self,id):
        if id not in self.dict:
            print("Invalid id not present here")
        else:
            print(self.dict[id].display())


p1=Product(1,"iphone",85000,10)
p2=Product(2,"redmi",12000,8)
p3=Product(3,"mi",12500,6)

I1=Inventory()
I1.add_Product(p1)
I1.add_Product(p2)
I1.add_Product(p3)
I1.displayAll()
I1.delete(2)
print("deleted details of id 2")
I1.displayAll()
I1.update(1,25)
print("Updtaed quantity of id 1")
I1.displayAll()
I1.searchId(1)


