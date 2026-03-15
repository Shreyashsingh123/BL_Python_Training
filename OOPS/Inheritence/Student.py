class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
       pass
    def ispass(self):
        for i in self.marks:
            if i<40:
                print("Fail")
                break
        print("Pass")

class Student1(Student):
    def __init__(self, name, roll, marks):
        super().__init__(name, roll, marks)
    def display(self):
        print("My name is :",self.name)
        print("Roll no is:" ,self.roll)
        print("Marks is:",self.marks)
    def avg(self):
        a=0
        for i in self.marks:
            a+=i
        a/=len(self.marks)
        print("Average of arks is:",a)


St1=Student1("Harsh",26,[59,52,50])
St1.display()
St1.ispass()
St1.avg()

        