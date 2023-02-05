class BankAccount:
    accounts = []
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)


    # increases the account balance by the given amount
    def deposit(self, amount):
        if amount < 0:
            print("Your deposit amount is invalid")
        else:
            self.balance += amount
        return self

    # decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if amount < 0 or self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    # print to the console: eg. "Balance: $100"
    def display_account_info(self):
        balance = f"Balance: ${self.balance}"
        return balance

    # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
        else:
            print("You don't have money in your account")
        return self
