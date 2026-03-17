class Contact:
    def __init__(self,name,phone,city):
        self.name=name
        self.city=city
        self.phone=phone
    def display(self):
        print(f"Name: {self.name} Phone: {self.phone} City: {self.city}")
    def update(self,city=None,phone=None):
        if city:
            self.city=city
        if phone:
            self.phone=phone

    # def sort_name(self):
    #     self.
class Address_Book:
    def __init__(self):
        self.dict={}
    def add(self,contact):
        if contact.name not in self.dict:
            self.dict[contact.name]=contact
            print("contact added successfully")
        else:
            print("contact already present")
    def update(self,name,city=None,phone=None):
        if name not in self.dict:
            print("Contact not present")
        else:
            self.dict[name].update(city,phone)
    def delete(self,name):
        if name not in self.dict:
            print("Contact not present")
        else:
            del self.dict[name]
            print("Contact deleted success")
    def search_name(self,name):
        if name not in self.dict:
            print("not found conatact")
        else:
            self.dict[name].display()
    def search_city(self,city):
        flag=False
        for i in self.dict.values():
            if i.city.lower()==city.lower():
                i.display()
                flag=True
        if not flag:
            print("No contact found")

    def displayAll(self):
        if not self.dict:
            print("Empty dict")

        else:
            for i in self.dict.values():
                i.display()
        
c1=Contact("ram",2356,"varanasi")
c2=Contact("abc",2563,"Prayagraj")
c3=Contact("asd",1818,"vns")

a1=Address_Book()
ls=[c1,c2,c3]
for i in ls:
    a1.add(i)
a1.displayAll()
a1.search_name("ram")
a1.update("ram",city="Ayodhya")
a1.displayAll()
a1.delete("asd")
a1.displayAll()
a1.search_city("Ayodhya")


