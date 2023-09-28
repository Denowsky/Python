
class Rectangle:
    def __init__(self, side_a, side_b = None):
        self.side_a = side_a
        self.side_b = side_b

    def perimetr(self):
        return self.side_a + self.side_b

    def area(self):
        return self.side_a * self.side_b
    
