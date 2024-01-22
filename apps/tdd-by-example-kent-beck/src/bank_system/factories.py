from src.bank_system.models.bank import (
        CheckingAccount, 
        SavingsAccount
)

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

