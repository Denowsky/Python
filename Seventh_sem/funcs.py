import os
import random as rnd
from string import ascii_lowercase

WORK_DIRECTORY = os.getcwd()

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
    os.chdir(WORK_DIRECTORY + directory)
    count = int(input("Сколько файлов создать?: "))
    file_type = "." + input("Введите расширение файла: ")
    for i in range(count):
        name = func_generate_name()
        func_append(name + file_type)

def func_make_sorted(directory):
    os.chdir(WORK_DIRECTORY + directory)
    folders_dict = {"text" : 'txt, docx, doc, nd',
                    "video" : 'avi, gpeg3, mp4',
                    "script" : 'py, java, sma, lua'}
    folders_list = os.listdir()
    for folder in folders_dict.keys():
        if folder not in folders_list:
            os.mkdir(str(folder))
    for file in folders_list:
        name = file.split(".")
        if len(name) > 1:
            for key in folders_dict.keys():
                if name[1] in folders_dict.get(key):
                    os.replace(file, os.getcwd()+ "\\" + key + "\\" + file)

def func_rename(directory, name_range=[3, 6]):
    os.chdir(WORK_DIRECTORY + directory)
    all_files = os.listdir()
    files_list = []
    for file in all_files:
        if len(file.split("."))>1:
            files_list.append(file)
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
                                \n3. Отсортировать файлы\n4. Выход\nВыберите пункт меню: "))
        match menu_answer:
            case 1:
                func_create_file(directory)
            case 2:
                func_rename(directory)
            case 3:
                func_make_sorted(directory)
            case 4:
                print("Работа окончена, выход...")
                status = False
            case _:
                print("Команда не распознана")
    return

if __name__ == "__main__":
    work_directory = '\\Seventh_sem\\files\\'

    menu(work_directory)