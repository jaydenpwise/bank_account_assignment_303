# main.py
# A simple banking program that lets a customer manage one bank account.

from bank_account import BankAccount


def get_amount(prompt):
    """Asks for a dollar amount and keeps asking until it is a valid number."""
    while True:
        answer = input(prompt + "\n").strip().replace("$", "").replace(",", "")
        try:
            amount = round(float(answer), 2)
        except ValueError:
            print("Please enter a valid dollar amount.")
            continue

        # Only positive amounts make sense for deposits and withdrawals
        if amount <= 0:
            print("The amount must be greater than $0.00.")
        else:
            return amount


def make_deposit(account):
    """Option 1: asks how much to deposit and adds it to the account."""
    amount = get_amount("How much would you like to deposit?")
    account.deposit(amount)
    print("You deposited ${:,.2f}. New balance: {}".format(amount, account.get_formatted_balance()))


def make_withdrawal(account):
    """Option 2: asks how much to withdraw and removes it if there is enough money."""
    amount = get_amount("How much would you like to withdraw?")
    if account.withdraw(amount):
        print("You withdrew ${:,.2f}. New balance: {}".format(amount, account.get_formatted_balance()))
    else:
        print("Insufficient funds. You only have " + account.get_formatted_balance() + " in your account.")


def view_account_info(account):
    """Option 3: displays the account information."""
    account.display_info()


def display_menu():
    """Shows the list of options."""
    print()
    print("Please choose an option:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")


# Welcome the customer and create their account
print("Welcome to the Bank of Spencer!")
name = input("Please enter your name:\n").strip()
while name == "":
    name = input("Your name cannot be blank. Please enter your name:\n").strip()

customer_account = BankAccount(name)

# Keep showing the menu until the customer chooses to quit
choice = ""
while choice != "4":
    display_menu()
    choice = input().strip()

    if choice == "1":
        make_deposit(customer_account)
    elif choice == "2":
        make_withdrawal(customer_account)
    elif choice == "3":
        view_account_info(customer_account)
    elif choice == "4":
        print("Thank you for your business!")
    else:
        print("Invalid choice. Please try again.")
