from abc import ABC,abstractmethod
class Vehicle:
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def fuel(self,ftype):
        pass

class Car(Vehicle):
    def start(self):
        print("car started")
    
    def stop(self):
        print("car stopped")
    def fuel(self,msg):
        print("car uses",msg)
    
class Bike(Vehicle):
    def __init__(self, name, type1, speed,tyres,milege) -> None:
        self.name=name
        self.type1=type1
        self.speed=speed
        self.tyres=tyres
        self.milege=milege

    def start(self):
        print("\n")
        print(self.name,"Bike started ")
        print("Milege of this bike is:",self.milege)
        print("Number of tyres are:",self.tyres)
    def stop(self):
        print(self.name," bike stopped ")
    def fuel(self,msg):
        print("bike uses",msg)

# Car1=Car("Wagonr","2nd model",20,"white",4)
# Car1.start()
# Car1.stop()
Bike1=Bike("Bullet","normal",35,2,40)
Bike1.start()
Bike1.stop()
Bike1.fuel("petrol")
c1=Car()
c1.start()
c1.stop()
c1.fuel("petrol")