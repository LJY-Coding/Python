from bank_account_v2 import BankAccount
# Create a user class
class User:
    # Initialize the user's basic info
    def __init__(self, user_name: str, email: str):
        self.user = user_name
        self.email = email
        self.account = BankAccount(0.2, 0)

    # def make_deposit(self, amount):
    #     if len(self.account) >= 1:
    #         print("Which account you want to make a deposit to: {}".format(self.account))
    #         self.account.deposit(amount)
    #         return self
    #     else:
    #         pass

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self
    
user1 = User("Tony Stark", "tony.stark@gmail.com")
user1.display_user_balance()