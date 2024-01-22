from unittest import TestCase
from src.bank_system.models.bank import (
    BankAccount,
    BankTransferManager,
    FactoryBankAccount,
    CheckingAccount,
    SavingsAccount,
    AccountTypeDoesNotExist,
)

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


class FactoryBankAccountTest(TestCase):
    def test_create_valid_bank_account(self):
        bank_account = FactoryBankAccount.create_bank_account("checking")
        self.assertIsInstance(bank_account, CheckingAccount)
        bank_account = FactoryBankAccount.create_bank_account("savings")
        self.assertIsInstance(bank_account, SavingsAccount)

    def test_create_invalid_type_bank_account(self):
        with self.assertRaises(AccountTypeDoesNotExist):
            FactoryBankAccount.create_bank_account("savingst")
