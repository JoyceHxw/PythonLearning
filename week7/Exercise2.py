import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def perimeter(self):
        c=round(math.pi*2*self.radius,2)
        return c
    
    def area(self):
        s=round(math.pi*self.radius**2,2)
        return s

circle=Circle(6)
print(circle.perimeter())
print(circle.area())