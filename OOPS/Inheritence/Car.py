class Car:
    def __init__(self,windows,tyres,engine):
        self.windows=windows
        self.tyres=tyres
        self.engine=engine
    def drive(self):
        print("Driving car")
        
        # Audi inherits Car its properties and methods

class Audi(Car):
    def __init__(self,windows,tyres,engine,speed):
        super().__init__(windows,tyres,engine)
        self.speed=speed

Car1=Audi(4,4,"Diesel",90)
print("Car ah {} windows".format(Car1.windows))
print("Car has {} tyres".format(Car1.tyres))
print("Engine type of car is",Car1.engine)
print("Speed of car is",Car1.speed)
print(Car1.drive())

