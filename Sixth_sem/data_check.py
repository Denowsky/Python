from datetime import datetime

def check_date_function(date):
    try:
        valid_date = datetime.strptime(date, '%d.%m.%Y')
        print(f'Дата {date} существует')
        answer = input("Проверить на вискосность? Д/Н(Y/N)")
        match answer.lower():
            case "д" | "y":
                if 1 <= valid_date.year <= 9999:
                    _check_leap(valid_date.year)
                else:
                    print("Неверный год. Год должен быть в диапазоне от 1 до 9999.")
            case "н" | "n":
                print("Работа завершена")
            case _:
                print("Команда не распознана, работа завершена")
    except ValueError:
        print(f'Дата {date} не существует')

def _check_leap(year):
    if year%4==year%100==year%400:
        print(f'Год {year} является високосным')
    else:
        print(f'Год {year} не является високосным')

if __name__ == "__main__":
    date_str = input("Введите дату в формате DD.MM.YYYY: ")

    check_date_function(date_str)