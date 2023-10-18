import os
import logging
from collections import namedtuple

FileInfo = namedtuple(
    'FileInfo', ['name', 'extension', 'flag', 'parent_directory'])

logging.basicConfig(filename='file_info.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', encoding="UTF-8")


def collect_directory_info(directory_path):
    for root, dirs, files in os.walk(directory_path):
            for directory in dirs:
                flag = "Каталог"
                parent_directory = os.path.basename(root)
                directory_info = FileInfo(directory, '', flag, parent_directory)
                log_message = f"Имя: {directory_info.name}, Флаг каталога: {directory_info.flag}, Родительский каталог: {directory_info.parent_directory}"
                logging.info(log_message)
            for file in files:
                if len(file.split("."))>1:
                    file_name_ext, file_extension = os.path.splitext(file)
                    file_name = file_name_ext.split(".")[0]
                    flag = "Файл"
                    parent_directory = os.path.basename(root)
                    file_info = FileInfo(
                        file_name, file_extension, flag, parent_directory)
                    log_message = f"Имя: {file_info.name}, Расширение: {file_info.extension}, Флаг каталога: {file_info.flag}, Родительский каталог: {file_info.parent_directory}"
                    logging.info(log_message)


if __name__ == "__main__":
    directory_path = input("Введите путь к директории: ")

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        collect_directory_info(directory_path)
        print("Информация о содержимом директории сохранена в файле 'file_info.log'.")
    else:
        print("Указанный путь не является директорией или не существует.")
