from math import pi

class Circle:
    def __init__(self, rad):
        self.rad = rad

    def length(self):
        return 2*self.rad * pi

    def area(self):
        return self.rad ** 2 * pi
    
circle_01 = Circle(2)
print(f'{circle_01.length() = }, {circle_01.area() = }')