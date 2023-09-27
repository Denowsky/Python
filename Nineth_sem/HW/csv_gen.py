from random import randint as rnd
import os, csv

def csv_filler(_min, _max, file_name):
        file = open(f'{file_name}.csv', 'w', encoding='UTF-8', newline='')
        writer = csv.writer(file)
        for i in range(rnd(100, 1000)):
            a = rnd(_min, _max)
            b = rnd(_min, _max)
            c = rnd(_min, _max)
            result = [a, b, c]
            writer.writerow(result)
        file.close()

csv_filler(1, 100, "file_01")
