
import copy
import datetime
import time

time = datetime.datetime
class MyClass:
    zip_list = []
    def __init__(self, value, text) -> None:
        self.value = value
        self.text = text
        self.zip_list = copy.deepcopy(self.__class__.zip_list)
        self.__class__.zip_list.append(tuple((value, text)))

    def __str__(self) -> str:
        return f'{self.value} {self.text} | {self.zip_list}'
    
a = MyClass(21, 'aweasd')
b = MyClass(24, 'asdgv')
c = MyClass(45, 'gbcvbfb')

print(a)
print(b)
print(c)