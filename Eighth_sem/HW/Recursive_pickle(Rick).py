# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директори
import os
import json
import csv
import pickle


def write_to_json(file_name, data):
    file = open(f'{file_name}.json', "w", encoding="utf-8")
    json.dump(data, file, indent=2, ensure_ascii=False)
    file.close()

def write_to_csv(directory, file_name, data: dict):
    data_to_write = data.get(directory)
    file = open(f'{file_name}.csv', "w", encoding="utf-8")
    writer = csv.DictWriter(file, fieldnames=data_to_write[0])
    writer.writeheader()
    for _dict in data_to_write:
        writer.writerow(_dict)
    file.close()

def write_to_pickle(directory, file_name, data: dict):
    data_to_write = data.get(directory)
    file = open(f'{file_name}.pickle', "wb")
    for _dict in data_to_write:
        pickle.dump(_dict, file)
    file.close()

    
def walk_through(directory, name):
    dirs = []
    for dir_path, dir_name, file_name in os.walk(directory):
        dirs.append({"Родительская директория": dir_path,
                     "Директории": dir_name,
                     "Файлы": file_name})
    result = {directory: dirs}
    write_to_json(name, result)
    write_to_csv(directory, name, result)
    write_to_pickle(directory, name, result)

path_file = "c:/Users/Densa/OneDrive/Документы/pth/Eighth_sem/HW/file"
walk_through(os.getcwd(), path_file)
