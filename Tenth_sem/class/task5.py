# 📌Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п. 
# 📌У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. 
# 📌Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, bark):
        super().__init__(name)
        self.bark = bark
    def get_bark(self):
        return self.bark

class Cat(Animal):
    def __init__(self, name, meow):
        super().__init__(name)
        self.meow = meow
    def get_meow(self):
        return self.meow

class Sheep(Animal):
    def __init__(self, name, bleah):
        super().__init__(name)
        self.bleah = bleah
    def get_bleah(self):
        return self.bleah

kotik = Cat("Котек", "Мяу")
print(Cat.get_meow(kotik))
print(Cat.get_bark(kotik))


