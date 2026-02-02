from collections import defaultdict


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, amount):
        self.balance += amount

    def payment(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        print("Не хватает средств на балансе. Пополните счет")
        return False


class Cart:
    def __init__(self, user):
        self.user = user
        self.goods = defaultdict(int)
        self.__total = 0

    def add(self, product, quantity=1):
        # Ключом теперь является сам объект product
        self.goods[product] += quantity
        self.__total += product.price * quantity

    def remove(self, product, quantity=1):
        current_qty = self.goods[product]
        to_remove = min(quantity, current_qty)

        self.goods[product] -= to_remove
        self.__total -= product.price * to_remove

        if self.goods[product] <= 0:
            del self.goods[product]

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.total):
            print("Заказ оплачен")
        else:
            print("Проблема с оплатой")

    def print_check(self):
        print("---Your check---")
        sorted_products = sorted(self.goods.items(), key=lambda x: x[0].name)
        for prod, qty in sorted_products:
            print(f"{prod.name} {prod.price} {qty} {prod.price * qty}")
        print(f"---Total: {self.total}---")