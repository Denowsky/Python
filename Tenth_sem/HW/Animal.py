
class Animal:
    def __init__(self, name, a_type = None):
        self.name = name
        self.a_type = a_type
    def get_animal(self):
        return f'{self.name}, {self.a_type}'


class Dog(Animal):
    def __init__(self, name, bark):
        super().__init__(name)
        self.bark = bark
        a_type = Dog.__name__
        self.a_type = a_type
    def get_bark(self):
        return self.bark

class Cat(Animal):
    def __init__(self, name, meow):
        super().__init__(name)
        self.meow = meow
        a_type = Cat.__name__
        self.a_type = a_type
    def get_meow(self):
        return self.meow

