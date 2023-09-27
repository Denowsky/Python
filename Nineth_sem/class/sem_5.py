# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from sem_3 import decor as json_decor
from sem_2 import decor as param_control_decor
from sem_4 import outer as counter

@json_decor
@counter(2)
@param_control_decor
def guess_num(a: int, b: int):
    print(f"У тебя {b} попытки угадать число")
    while b:
        guess = int(input("Введите число: "))
        if guess > a:
            print(f"Загаданное число меньше {guess}")
        elif guess < a:
            print(f"Загаданное число больше {guess}")
        else:
            print(f"Число угадано {a}")
            return f'За {b} попыток число {a} угадано'
        b-=1
        print(f"Осталось {b} попыток")
    else:
        print(f"Попыток не осталось, число {a}")
        return f'Число {a} не угадано'

guess_num(321, 2)