class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"Account balance: {self.balance}")

account = BankAccount()
account.deposit(1000)
account.withdraw(500)
account.show_balance()