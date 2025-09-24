"""Create a Wallet class with the following features:

a private attribute __balance,
access to the balance is provided via a @property decorator,
the balance can only be modified through a @balance.setter, and only if the new value is non-negative."""


class Wallet:
    """Create a Wallet class"""
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return f'Баланс = {self.__balance}'

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self.__balance = balance

wallet = Wallet()

wallet.balance = (int(input()))
wallet.balance = (int(input()))
print(wallet.balance)