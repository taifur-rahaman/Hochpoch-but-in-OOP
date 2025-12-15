from math import pi

class Circle:
    def __init__(self, radius = 0):
        self.radius = radius
    
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            raise ValueError("Negative Radius isn't Allowed")
        elif new_radius == 0:
            raise ValueError("You are Giving a Point")
        else:
            self._radius = new_radius
    
    def area(self):
        return pi*pow(self._radius, 2)
    
    def perimeter(self):
        return 2*pi*self._radius