# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
import os

path_str = "Eighth_sem\\classwork\\"

print(path_str)
# my_string = "154521.14521|Johan\n"


def parse_txt_to_tuple(name):
    os.chdir(path_str)
    file = open(f'{name}.txt', 'r')
    result = []
    for line in file:
        result.append(line.strip().split("|"))
    file.close()
    return result


def make_json(inp_list):
    tmp_dict = {}
    for item in inp_list:
        tmp_dict.setdefault(float(item[0]), item[1])
    with open("p1.json", "w") as file_json:
        json.dump(tmp_dict, file_json, indent= 2)


make_json(parse_txt_to_tuple("habuba"))
