
class Animal:
    def __init__(self, name, a_type):
        self.name = name
        self.a_type = a_type
    def get_animal(self):
        return f'{self.name}, {self.a_type}'


class Dog(Animal):
    def __init__(self, name, a_type, bark):
        super().__init__(name, a_type)
        self.bark = bark
    def get_bark(self):
        return self.bark


class Cat(Animal):
    def __init__(self, name, a_type, meow):
        super().__init__(name, a_type)
        self.meow = meow
    def get_meow(self):
        return self.meow

