# Simple Bank System

## Introduction

This is a simple banking system that allows users to create accounts, deposit and withdraw money, check their balance, transfer money, view transaction history, and includes overdraft protection.

## User Stories

1. **Create an Account:**
   - As a new customer, I want to be able to create a bank account.
   - Acceptance Criteria:
     - The system should generate a unique account number. [X]
     - Initial account balance should be zero. [X]
   - Tasks:
     1. Implement a `BankAccount` class with properties for account number and balance. [X]
     2. A `BankAccount` has two types of accounts: `CheckingAccount` and `SavingsAccount`. [X]
     3. Utilize the Factory Method design pattern to create different account types. [X]
     4. Write a test to ensure that the account number generated is unique. [X]
     5. Write a test to ensure that the initial account balance is zero. [X]

2. **Deposit Money:**
   - As an account holder, I want to be able to deposit money into my account. [X]
   - Acceptance Criteria: [X]
     - The system should update the account balance accordingly. [X]
   - Tasks:
     1. Add a `deposit` method to the `BankAccount` class. [X]
     2. Implement the Observer design pattern to notify account holders of balance changes.  TODO
     3. Write a test to ensure that the account balance is updated correctly after a deposit. [X]

3. **Withdraw Money:**
   - As an account holder, I want to be able to withdraw money from my account. [X]
   - Acceptance Criteria: 
     - The system should update the account balance accordingly. [X]
     - Withdrawal should not be allowed if the account balance is insufficient. [X]
   - Tasks:
     1. Add a `withdraw` method to the `BankAccount` class. [X]
     2. Apply the Command design pattern to encapsulate withdrawal requests. TODO
     3. Write tests to verify that withdrawals are handled correctly, considering the balance constraints. [X]

4. **Check Balance:**
   - As an account holder, I want to be able to check my account balance.
   - Acceptance Criteria:
     - The system should display the current account balance.
   - Tasks:
     1. Add a `getBalance` method to the `BankAccount` class.
     2. Test `getBalance`

5. **Transfer Money:**
   - As an account holder, I want to be able to transfer money between two accounts.
   - Acceptance Criteria:
     - The system should update the account balances of both sender and receiver.
   - Tasks:
     1. Introduce the Strategy design pattern to handle different transfer strategies (e.g., immediate transfer, scheduled transfer).
     2. Implement a `transfer` method in the `BankAccount` class.
     3. Write tests to verify that funds are transferred correctly between accounts.

6. **Account History:**
   - As an account holder, I want to view the history of transactions on my account.
   - Acceptance Criteria:
     - The system should maintain a log of deposits, withdrawals, and transfers.
   - Tasks:
     1. Implement a transaction history log in the `BankAccount` class.
     2. Use the Observer pattern to update the log on each transaction.
     3. Write tests to ensure that the transaction history is accurate.

7. **Account Overdraft Protection:**
   - As an account holder, I want to have overdraft protection to prevent negative balances.
   - Acceptance Criteria:
     - The system should deny withdrawals that exceed the account balance.
   - Tasks:
     1. Enhance the `withdraw` method to check for overdraft conditions.
     2. Write tests to validate that overdraft protection is working as expected.


## Future Features
- The system should allow users to close their accounts.
- The system should allow users input with more than one currency.
- The system should purchase a tax for each transaction.
- The system should be able to generate a report for all transactions of a day.

## Development Setup

1. Clone the repository: `git clone [repository-url]`

## Run Tests

...
