import uuid

from abc import ABC

class BankAccount(ABC):
    def __init__(self) -> None:
        self._id = uuid.uuid4()
        self._balance = 0

        # TODO: Refact
        self.history = []

    @property
    def balance(self):
        return self._balance

    def _increase_balance(self, amount: float):
        self._balance += amount  

    def _decrease_balance(self, amount: float):
        self._balance -= amount

    @property
    def id(self):
        return self._id

    def _validate_amount(self, amount: float):
        if amount <= 0:
            raise ValueError("Invalid amount for deposit, must be a positive number")

        if not isinstance(amount, (int, float)):
            raise TypeError("Invalid type for amount, must be a numeric value")

    def withdraw(self, amount: float):

        self._validate_amount(amount)

        if amount > self._balance:
            raise Exception("Invalid amount value, must be less than of total balance")
        
        self._decrease_balance(amount)
        self.history.append({"type": "withdraw", "amount": amount})

    def deposit(self, amount: float):
        self._validate_amount(amount)
        self._increase_balance(amount)
        self.history.append({"type": "deposit", "amount": amount})

class BankTransferManager:
    def __init__(self):
        ...

    def transfer(self, sender: BankAccount, receive: BankAccount, amount: float):
        sender._decrease_balance(amount)
        receive._increase_balance(amount)

class CheckingAccount(BankAccount):
    ...

class SavingsAccount(BankAccount):
    ...
