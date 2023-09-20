import os
import random as rnd
from string import ascii_lowercase

def create_file(name: str, lines=10):
    with open(name, "w", encoding="utf-8") as file:
        for _ in range(lines):
            a = rnd.randint(-1000, 1000)
            b = rnd.uniform(-1000, 1000)
            file.write(f'{a} | {b}\n')

def generate_name(size_min=4, size_max=7):
    vowels = set('euioa')
    consonants = set(ascii_lowercase).difference(vowels)
    len_name = rnd.randint(size_min, size_max)
    name = ''
    for i in range(len_name):
        name += rnd.choice(list(vowels)) if i % 2 else rnd.choice(list(consonants))
    return name.title()

def create_files(directory):
    count = int(input("Сколько файлов создать?: "))
    file_type = "." + input("Введите расширение файла: ")
    for i in range(count):
        name = generate_name()
        create_file(os.path.join(directory, name + file_type))

def rename_files(directory, name_range=[3, 6]):
    os.chdir(directory)
    files_list = [entry.name for entry in os.scandir(directory) if entry.is_file()]
    if not files_list:
        print(f'В директории "{directory}" нет файлов.')
        return
    print(f'В директории "{directory}" есть файлы: {files_list}')
    answer = input('Желаете их переименовать? (Y/N): ')
    if answer.lower() == "y":
        file_type = "." + input("Введите расширение файла: ")
        for index, file in enumerate(files_list, start=1):
            name_parts = file.split(".")
            ranged_name = name_parts[0][name_range[0]:name_range[1]]
            number = "_" + str(index)
            new_name = input(f'Введите новое имя для {name_parts[0]}: ')
            os.rename(file, ranged_name + new_name + number + file_type)
    elif answer.lower() == "n":
        print("Возвращение в меню")
    else:
        print("Команда не распознана. Завершение работы")

def main(directory):
    while True:
        print("Выберите пункт меню:")
        print("1. Создать файлы.")
        print("2. Переименовать файлы.")
        print("3. Выход.")
        choice = input("Введите номер пункта: ")
        if choice == "1":
            create_files(directory)
        elif choice == "2":
            rename_files(directory)
        elif choice == "3":
            print("Работа окончена, выход...")
            break
        else:
            print("Команда не распознана")

if __name__ == "__main__":
    main("Seventh_sem/files/")