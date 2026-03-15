class Vehicle:
    def __init__(self,name,type1,speed) -> None:
        self.name=name
        self.type1=type1
        self.speed=speed
    def start(self):
        pass

    def stop(self):
        pass
class Car(Vehicle):
    def __init__(self,name,type1,speed,color,tyres):
        super().__init__(name,type1,speed)
        self.color=color
        self.tyres=tyres
    def start(self):
        print(self.name, " car started")
        print("Number of tyres are:",self.tyres)
        print("Color of car is:",self.color)
    def stop(self):
        print(self.name,"car stopped")
    
class Bike(Vehicle):
    def __init__(self, name, type1, speed,tyres,milege) -> None:
        super().__init__(name, type1, speed)
        self.tyres=tyres
        self.milege=milege
    def start(self):
        print("\n")
        print(self.name,"Bike started ")
        print("Milege of this bike is:",self.milege)
        print("Number of tyres are:",self.tyres)
    def stop(self):
        print(self.name," bike stopped ")


Car1=Car("Wagonr","2nd model",20,"white",4)
Car1.start()
Car1.stop()
Bike1=Bike("Bullet","normal",35,2,40)
Bike1.start()
Bike1.stop()