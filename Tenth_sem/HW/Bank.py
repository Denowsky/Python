# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
#  Превратите функции в методы класса, а параметры в свойства. 
# Задания должны решаться через вызов методов экземпляра.

class Bankomat:
    def __init__(self):
        self.balance = 0
        self.transactions = 0
        self.comission = 0
        self.tax = 0.10

    def transaction_check_and_balance(self):
        if self.transactions % 3 == 0:
            procent = self.balance * 0.03
            self.balance += procent
            print(f'Добавлен процент на счёт: {procent}')
        elif self.balance > 5000000:
            self.balance -= self.balance * self.tax
            print(f'Вычтен налог на сверхдоход: {self.tax}')

    def calculate_comission(self, wthdr_mon):
        self.withdrawal_comission = max(30, min(wthdr_mon * 0.015, 600))
        self.balance -= self.withdrawal_comission
        print(f'Комиссия за операцию {self.withdrawal_comission}')

    def display_balance(self):
        print(f"Баланс: {self.balance}")

    def withdraw(self, withdraw_money):
        if withdraw_money % 50 != 0:
            print("Сумма снятия должна быть кратной 50")
        elif withdraw_money > self.balance:
            print("Недостаточно средств на счете.")
        else:
            self.balance -= withdraw_money
            self.transactions += 1
            self.calculate_comission(withdraw_money)
            self.transaction_check_and_balance()
        self.display_balance()

    def deposit(self, amount_money):
        if amount_money % 50 != 0:
            print("Сумма пополнения должна быть кратной 50")
        else:
            self.balance += amount_money
            self.transactions += 1
            self.transaction_check_and_balance()
            self.display_balance()


def main():
    account = Bankomat()

    while True:
        print("\nВыберите действие:")
        print("1. Пополнить счет")
        print("2. Снять со счета")
        print("3. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            amount = int(input("Введите сумму для пополнения, кратную 50: "))
            account.deposit(amount)
        elif choice == "2":
            amount = int(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
