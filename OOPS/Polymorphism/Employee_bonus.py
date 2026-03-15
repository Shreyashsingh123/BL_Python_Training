class Employee:
    def __init__(self,salary) -> None:
        self.salary=salary

    def calculatebonus(self):
        pass
class Manager(Employee):
    def calculatebonus(self):
        bonus=self.salary*(20/100)
        print("Bonus of manager is",bonus)

class Developer(Employee):
    def calculatebonus(self):
        bonus=self.salary*0.1
        print("Bonus of Developer is:", bonus)
class Intern(Employee):
    def calculatebonus(self):
        bonus=self.salary*0.05
        print("Bonus of intern is:",bonus)

m1=Manager(80000)
m1.calculatebonus()
d1=Developer(35000)
d1.calculatebonus()
I1=Intern(20000)
I1.calculatebonus(20000)


        