# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 
# 📌У класса должны быть методы birthday для увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор. 
# 📌Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

class Person:
    def __init__(self, name, second_name, age):
        self.name = name
        self.second_name = second_name
        self.__age = age
    
    def show_name(self):
        return f'{self.name = }, {self.second_name = }'
    
    def birthday(self):
        self.__age += 1
    
    def show_age(self):
        return self.__age

patrick = Person("Patrick", "Seastar", 26)

print(patrick.show_name(), patrick.show_age())
patrick.birthday()
print(patrick.show_age())
