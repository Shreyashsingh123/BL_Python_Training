class Car:
    def __init__(self,color,milege,tyres):
        self.color=color
        self.tyres=tyres
        self.milege=milege
    def mil(self):
        print("car milege is:",self.milege)

car1=Car("Blue",22,4)
print("Car color is: {}".format(car1.color))
# format means it value comes in {} given earlier before writing .format
print("Car have {} tyres".format(car1.tyres))
car1.mil()