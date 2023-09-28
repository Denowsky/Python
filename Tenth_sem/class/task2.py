
class Rectangle:
    def __init__(self, side_a, side_b = None):
        self.side_a = side_a
        self.side_b = side_b if side_b else side_a 

    def perimetr(self):
        return 2*(self.side_a + self.side_b)

    def area(self):
        return self.side_a * self.side_b
    
rectangle_01 = Rectangle(2, 5)
print(f'{rectangle_01.perimetr() = }, {rectangle_01.area() = }')
rectangle_02 = Rectangle(4)
print(f'{rectangle_02.perimetr() = }, {rectangle_02.area() = }')