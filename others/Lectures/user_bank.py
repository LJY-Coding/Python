from bank_account import BankAccount
import re
# Create a user class
class User:
    # Initialize the user's basic info
    def __init__(self, user_name: str, email: str):
        self.name = user_name
        self.email = email
        self.accounts = {}

    def open_account(self, int_rate = 0.2, balance = 0, account_name = "Checking"):
        count = 0
        for key in self.accounts:
            if re.match(f"^{account_name}", key):
                count += 1
        if count != 0:
            account_name += f" {count}"
        self.accounts[account_name] = BankAccount(int_rate, balance)
        return self

    @staticmethod
    def specify_account(accounts, operation):
        print(f"Which account you want to {operation}? {accounts.__dict__}")
        account_name = input()
        if account_name.lower() in list((accounts.keys()).lower()):
            return account_name
        else:
            print("Please enter a valid account")
            specify_account()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        account_info = ""
        print(f"{self.name}'s Accounts:")
        for account_name, account in self.accounts.items():
            account_info += f"{account_name}: ${account.balance} \n"
        print(account_info)
        return self

user1 = User("Tony Stark", "tony@mail.com")
user1.open_account().open_account().display_user_balance()