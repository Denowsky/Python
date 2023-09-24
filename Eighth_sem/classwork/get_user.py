# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться

import json
import os

path_str = f'{os.getcwd()}\\Eighth_sem\classwork\\'

def load_json(js_file_name):
    if os.path.exists(f'{os.getcwd()}\\{js_file_name}.json'):
        with open(f'{os.getcwd()}\\{js_file_name}.json', "r") as f_jsn:
            data = json.load(f_jsn, parse_int=int)
    else:
        data = {}
        print("No")
    return data

def write_to_json(js_file_name, data):
    file = open(f'{js_file_name}.json', "w")
    json.dump(data, file, indent=2, sort_keys= True)
    file.close()


def get_inp_data(f_name):
    os.chdir(path_str)
    data = load_json(f_name)
    while True:
        name = input("Введите имя: ")
        if not name:
            print("Ошибка имени")
            break
        _id = input("Введите ID: ")
        level = int(input("Введите уровень от 1 до 7: "))
        if 7 < level < 1:
            print("Ошибка уровня")
            break
        if data:
            for value in data.values():
                if _id in value.keys():
                    print("Ошибка ID")
                    break
        print(data)
        data.setdefault(level, {_id:name})
        write_to_json(f_name, data)

get_inp_data("p2")

