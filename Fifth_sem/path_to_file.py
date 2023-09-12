import os

def split_path(file_path):
    file_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    name, extension = os.path.splitext(file_name)
    return (file_dir, name, extension)

file_path = "/абсолютный/путь/до/файла/файл.txt"
result = split_path(file_path)
print(result)