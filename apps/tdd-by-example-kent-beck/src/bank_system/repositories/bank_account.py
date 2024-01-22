from src.bank_system.models.bank import BankAccount

class AccountBankRepository:
    def __init__(self) -> None:
        self._db = {}
    
    @property
    def count(self):
        return len(self._db)
    
    def save(self, bank_acc: BankAccount) -> str:
        key = str(bank_acc.id)
        self._db[key] = bank_acc
        return key

    def get(self, key: str):
        return self._db.get(key)
