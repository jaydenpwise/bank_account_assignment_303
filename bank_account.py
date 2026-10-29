# bank_account.py
# The BankAccount class for the banking program.

import random


class BankAccount:
    """Represents a simple bank account for one customer."""

    def __init__(self, customer_name):
        """Creates a new account with a random account number and a $0.00 balance."""
        self.customer_name = customer_name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.0

    def deposit(self, amount):
        """Adds money to the account. Returns True if the deposit worked."""
        # Deposits must be a positive amount
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        """Takes money out of the account. Returns True if the withdrawal worked.

        The customer cannot withdraw more money than they have.
        """
        # Withdrawals must be positive and no more than the balance
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def get_formatted_balance(self):
        """Returns the balance as a dollar amount with two decimal places."""
        return "${:,.2f}".format(self.balance)

    def display_info(self):
        """Displays the customer's name, account number, and current balance."""
        print("Name: " + self.customer_name)
        print("Account #: " + str(self.account_number))
        print("Balance: " + self.get_formatted_balance())
