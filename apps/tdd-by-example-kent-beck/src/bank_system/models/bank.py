import uuid

from abc import ABC

class BankAccount(ABC):
    def __init__(self) -> None:
        self._id = uuid.uuid4()
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @property
    def id(self):
        return self._id

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Invalid amount for deposit, must be a positive number")

        if not isinstance(amount, (int, float)):
            raise TypeError("Invalid type for amount, must be a numeric value")
        
        # TODO: shoud avoid change _balance directly
        self._balance += amount

class CheckingAccount(BankAccount):
    ...

class SavingsAccount(BankAccount):
    ...

class AccountTypeDoesNotExist(Exception):
    ...

class FactoryBankAccount:
    @staticmethod
    def create_bank_account(account_type: str):
        if account_type == "checking":
            return CheckingAccount()
        elif account_type == "savings":
            return SavingsAccount()
        else:
            raise AccountTypeDoesNotExist()
