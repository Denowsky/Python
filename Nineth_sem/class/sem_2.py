# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.
import random as rnd
from typing import Callable

def decor(func: Callable):
    def wrapper(*args, **kwargs):
        a, b, *_ = args
        if a not in range(1, 101):
            print(f"Число {a} вне диапазона, я поставлю сам")
            a = rnd.randint(1, 100)
        if b not in range(1, 11):
            print(f"Число {b} вне диапазона, я поставлю сам")
            b = rnd.randint(1, 10)
        
        return func(a, b)
    return wrapper

@decor
def inner(a: int, b: int):
    print(f"У тебя {b} попытки угадать число")
    while b:
        guess = int(input("Введите число: "))
        if guess > a:
            print(f"Загаданное число меньше {guess}")
        elif guess < a:
            print(f"Загаданное число больше {guess}")
        else:
            print(f"Число угадано {a}")
            break
        b-=1
        print(f"Осталось {b} попыток")
    else:
        print(f"Попыток не осталось, число {a}")
