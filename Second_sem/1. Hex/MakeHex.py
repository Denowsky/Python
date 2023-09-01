def make_Hex(number):
    chars = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    result = ''
    while number > 0:
        temp = number % 16
        if temp >= 10 and temp <= 15:
            result += chars.get(temp)
        else:
            result += str(temp)
        number = number//16
    return f'0x{result[::-1]}'

num = int(input("Введите целое число: "))
print('Должно быть: ' + hex(num))
print(f'Получили: {make_Hex(num)}')
