def check_for_simpleNum(num):
    if num < 1 or num > 100000:
        return "Неверный ввод"
    for i in range(2, num):
        if num % i == 0:
            return f'Число {num} является составным'
    return f'Число {num} простое'
        
print(check_for_simpleNum(int(input("Введите число: "))))