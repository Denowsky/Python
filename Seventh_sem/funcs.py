import os
import random as rnd
from string import ascii_lowercase


def func_append(name: str, lines=10):
    file = open(name, "w", encoding="utf-8")
    for _ in range(lines):
        a = rnd.randint(-1000, 1000)
        b = rnd.uniform(-1000, 1000)
        file.write(f'{a} | {b}\n')
    file.close()


def func_generate_name(size_min=4, size_max=7):
    vowels = set('euioa')
    consonants = set(ascii_lowercase).difference(vowels)
    len_name = rnd.randint(size_min, size_max)
    name = ''
    for i in range(len_name):
        name += rnd.choice(list(vowels)
                           ) if i % 2 else rnd.choice(list(consonants))
    return name.title()


def func_create_file(directory):
    count = int(input("Сколько файлов создать?: "))
    file_type = "." + input("Введите расширение файла: ")
    for i in range(count):
        name = func_generate_name()
        func_append(directory + name + file_type)

def func_make_sorted(directory):
    os.chdir(directory)
    folders_dict = {"text" : 'txt, docx, doc, nd',
                    "video" : 'avi, gpeg3, mp4',
                    "script" : 'py, java, sma, lua'}
    folders_dir = os.chdir("..")
    folders_list = os.listdir(folders_dir)
    print(folders_list)
    for folder in folders_dict.keys():
        if folder not in folders_list:
            os.mkdir(str(folder))
    files_list = os.listdir(directory)
    print(files_list)
    print(folders_dir)
    # for file in files_list:
    #     name = file.split(".")
    #     file_type = "." + name[1]
    #     for folder in folders:
    #         if file_type in folder:
    #             os.replace(f'{name}.{file_type}',f'{folders_dir}{folder}')


def func_rename(directory, name_range=[3, 6]):
    os.chdir(directory)
    files_list = os.listdir()
    answer = input(
        f'В директории "{directory}" есть файлы: {files_list}\nЖелаете их переименовать? Y/N: ')
    match answer.lower():
        case "y":
            for file in files_list:
                name = file.split(".")
                file_type = "." + name[1]
                ranged_name = name[0][name_range[0]:name_range[1]]
                number = "_" + str(files_list.index(file) + 1)
                get_name = input(f'Введите новое имя для {name[0]}: ')
                os.rename(file, ranged_name + get_name + number + file_type)
        case "n":
            print("Возвращение в меню")
            return
        case _:
            print("Команда не распознана. Завершение работы")
            return


def menu(directory):
    status = True
    while status == True:
        menu_answer = int(input("\n1. Создать файл\
                                \n2. Посмотреть список файлов и переименовать их\
                                \n3. Выход\n4. Отсортировать файлы\nВыберите пункт меню: "))
        match menu_answer:
            case 1:
                func_create_file(directory)
            case 2:
                func_rename(directory)
            case 3:
                print("Работа окончена, выход...")
                status = False
            case 4:
                func_make_sorted(directory)
            case _:
                print("Команда не распознана")
    return