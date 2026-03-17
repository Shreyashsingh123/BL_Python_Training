class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        return f"{self.name},{self.price}"

class cart:
    def __init__(self):
        self.products=[]
    
    def add_Product(self,product):
        self.products.append(product)
        print(f"{product.name} added to cart")
    
    def removeProduct(self,product_name):
        for i in self.products:
            if i.name==product_name:
                self.products.remove(i)
                print(f"{product_name} removed successfully")
                return
            else:
                print("Product not present in cart")
    def calculate(self):
        t=sum(i.price for i in self.products)
        print("total price is",t)
        return
    def show_cart(self):
        if len(self.products)==0:
            print("Cart is empty")
            return
        else:
            for i in self.products:
                print(i.display())

p1=product("mi",50000)
p2=product("redmi",500)
p3=product("vivo",15000)
c1=cart()
c1.add_Product(p1)
c1.add_Product(p2)
c1.add_Product(p3)

c1.show_cart()
c1.removeProduct("mi")
c1.show_cart()
c1.calculate()

                


    