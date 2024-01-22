from unittest import TestCase
from src.bank_system.models.bank import (
    BankAccount,
    BankTransferManager,
    CheckingAccount,
    SavingsAccount,
)

from src.bank_system.repositories.bank_account import AccountBankRepository
from src.bank_system.factories import FactoryBankAccount, AccountTypeDoesNotExist

from uuid import UUID


class BankAccounTest(TestCase):
    def setUp(self) -> None:
        self.bank = BankAccount()

    def test_bank_initial_states_instance(self):
        """
        Test system should generate a unique account number
        and initial balance should be zero
        """
        self.assertIsNotNone(self.bank)
        self.assertEqual(self.bank.balance, 0)
        self.assertIsInstance(self.bank.id, UUID)

    def test_bank_deposit_method(self):
        self.bank.deposit(10)
        self.assertEqual(self.bank.balance, 10)

        self.bank.deposit(25)
        self.assertEqual(self.bank.balance, 35)

    def test_deposit_with_negative_quantity(self):
        """
        Test deposit with negative quantity return a ValueError
        because the type is correct but the value is invalid
        """
        with self.assertRaises(ValueError):
            self.bank.deposit(-10)

    def test_deposit_with_str_value(self):
        with self.assertRaises(TypeError):
            self.bank.deposit("10")

    def test_withdraw_method(self):
        self.bank.deposit(20)
        self.bank.withdraw(10)
        self.assertEqual(self.bank.balance, 10)
        self.bank.withdraw(5)
        self.assertEqual(self.bank.balance, 5)

    def test_withdraw_with_negative_input(self):
        with self.assertRaises(ValueError):
            self.bank.withdraw(-10)

    def test_withdraw_with_str_value(self):
        with self.assertRaises(TypeError):
            self.bank.withdraw("10")

    def test_withdraw_with_insufficient_funds(self):
        """
        Test Withdrawal should not be allowed if the account balance is insufficient.
        """
        with self.assertRaises(Exception):
            self.bank.withdraw(20)
            self.assertEqual(self.bank.balance, 0)

class BankAccountTransferOperationTest(TestCase):
    def setUp(self) -> None:
        ...

    def test_transfer_succesfull(self):
        transfer_manager = BankTransferManager()
        account_sender = BankAccount()
        account_receiver = BankAccount()
        
        account_sender.deposit(100)

        transfer_manager.transfer(sender=account_sender, receive=account_receiver, amount=20)

        self.assertEqual(account_sender.balance, 80)
        self.assertEqual(account_receiver.balance, 20)

class AccountBankRepositoryTest(TestCase):
    def test_repository_instance(self):
        acc_bank_repository = AccountBankRepository()
        self.assertEqual(acc_bank_repository.count, 0)

    def test_insert_bank_account(self):
        acc_bank_repository = AccountBankRepository()
        bank_account = BankAccount()
        acc_bank_repository.save(bank_account)
        self.assertEqual(acc_bank_repository.count, 1) 
    
    def test_get_bank_account(self):
        acc_bank_repository = AccountBankRepository()
        bank_account = BankAccount()
            
        bank_account.deposit(100)

        bank_key = acc_bank_repository.save(bank_account)
        result = acc_bank_repository.get(key=bank_key)

        self.assertIsInstance(result, BankAccount)
        self.assertEqual(result, bank_account)

class HistoryTransactionsAccountBankTest(TestCase):
    def test_recent_history_list(self):
        bank_account = BankAccount()
    
        bank_account.deposit(100)
        bank_account.deposit(100)
        bank_account.withdraw(20)

        history = bank_account.history

        self.assertEqual(len(history), 3)
        self.assertEqual(history[0]["type"], "deposit")
        self.assertEqual(history[0]["amount"], 100)
    
    def test_withdraw_transaction_log(self):
        ...

    def test_transfer_transaction_log(self):
        ...

    def test_correct_order_history_by_timestamp(self):
        ...

class FactoryBankAccountTest(TestCase):
    def test_create_valid_bank_account(self):
        bank_account = FactoryBankAccount.create_bank_account("checking")
        self.assertIsInstance(bank_account, CheckingAccount)
        bank_account = FactoryBankAccount.create_bank_account("savings")
        self.assertIsInstance(bank_account, SavingsAccount)

    def test_create_invalid_type_bank_account(self):
        with self.assertRaises(AccountTypeDoesNotExist):
            FactoryBankAccount.create_bank_account("savingst")
