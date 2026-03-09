from abc import ABC, abstractmethod
import math

class size:
    @abstractmethod
    # decorator
    def area(self):
        pass
class cube(size):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**3

class rectangle:
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid
    def area(self):
        return self.len*self.wid
cub=cube(5)
r=rectangle(5,4)

print("Area of cube is ::",cub.area())
print("Area of rectangle is: ",r.area())
