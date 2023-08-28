from random import randint
my_num = randint(0, 1000)

attempts = 10

while attempts > 0:
    your_num = int(input("Попробуй отгадать число: "))
    if your_num == my_num:
        print(f'Ты угадал, моё число: {my_num}')
        break
    else:
        attempts -= 1
        if your_num > my_num:
            print("Твоё число больше моего.")
        else:
            print("Твоё число меньше моего.")
        print("У тебя осталось {} попыток.".format(attempts))

if attempts == 0:
    print("Моё число было: {}".format(my_num))