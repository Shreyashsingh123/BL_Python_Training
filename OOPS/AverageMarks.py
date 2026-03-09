class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hii ",self.name," your avg score is  ",sum/3)

    
s1=Students("Harsh",[90,95,98])
s1.average()
