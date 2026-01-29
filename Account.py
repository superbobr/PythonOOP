from dataclasses import dataclass


@dataclass(frozen=True)
class Transaction:
    amount: float
    description: str


class AccountError(Exception):
    pass


class TransactionError(AccountError):
    pass


class Account:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self._initial_balance = initial_balance
        self._transactions = []

    @property
    def balance(self):
        return self._initial_balance + sum(self._transactions)

    def add_transaction(self, transaction: Transaction):
        if self.balance + transaction.amount < 0:
            raise TransactionError("Транзакция невозможна: недостаточно средств.")

        if isinstance(transaction, Transaction):
            self._transactions.append(transaction.amount)

    @classmethod
    def from_csv(cls, csv_string: str):
        data = csv_string.split(',')
        return cls(data[0], float(data[1]))

    def __len__(self):
        return len(self._transactions)

    def __str__(self):
        return f"Счет {self.owner}"

    def __repr__(self):
        return f"Account(owner='{self.owner}', initial_balance={self.balance})"