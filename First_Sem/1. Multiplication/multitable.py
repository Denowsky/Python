# Вывод таблицы умножения как на школьной тетради

def make_table():
    table = []
    for i in range(2, 10):
        temp = []
        for j in range(2, 11):
            temp.append(f'{i} x {j} = {i * j}')
        table.append(temp)
    return table

def print_table(array):
    for row in range(len(array[0])):
        for column in array:
            if column != array[-1]:
                print(column[row], end="\t")
            else:
                print(column[row])
    print("\n")

def split_table(array):
    part_1 = array[0: len(array)//2]
    part_2 = array[len(array)//2: len(array)]
    return part_1, part_2
        
multitable = make_table()
tabulation_size = 20
print("ТАБЛИЦА УМНОЖЕНИЯ".center(len(multitable[0])*len(multitable[0][0])//2 + tabulation_size))

part_1, part_2 = split_table(multitable)
print_table(part_1)
print_table(part_2)