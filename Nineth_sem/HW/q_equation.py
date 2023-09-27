from typing import Callable
import csv


def my_decorator(func: Callable):
    def wrapper():
        result = []
        data = []
        with open('file_01.csv', 'r') as fr:
            csv_reader = csv.reader(fr)
            for line in csv_reader:
                data.append(line)
        for row in data:
            result.append(func(int(row[0]), int(row[1]), (int(row[2]))))
        with open('file_02.csv', 'w', newline='', encoding="UTF-8") as fw:
            csv_writer = csv.writer(fw)
            csv_writer.writerow(result)
    return wrapper

@my_decorator
def quadratic_equations(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return 'Нет решений'

quadratic_equations()