# Решить задания, которые не успели решить на семинаре.
# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

from Animal import Dog, Cat

kot = Cat("Felix", "Meow!")
g_boy = Dog("Chappi", "Bark-bark!")

print(kot.get_animal() + ", " + kot.get_meow()) # Felix, Cat, Meow!
print(g_boy.get_animal() + ", " + g_boy.get_bark()) # Chappi, Dog, Bark-bark!

