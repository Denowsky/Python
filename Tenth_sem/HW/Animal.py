
class Animal:
    def __init__(self, name, a_type = __name__, specific = None):
        self.name = name
        self.a_type = a_type
        self.specific = specific
    def get_animal(self):
        return f'{self.name}, {self.a_type}, {self.specific}'


class Dog(Animal):
    def __init__(self, name, a_type=__name__, specific = str):
        super().__init__(name, a_type, specific)
        self.specific = specific


class Cat(Animal):
    def __init__(self, name, a_type=__name__, specific = str):
        super().__init__(name, a_type, specific)
        self.specific = specific