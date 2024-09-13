#Custom Exception - Own

class BalanceLowException(Exception):
    def __init__(self, message):
        self.message = message
        scope().__init__(message)

    balance = 100
    withdraw = int(input("Enter the amount that you want to withdraw\n"))
    if withdraw > balance:
        raise BalanceLowException("Balance is low!!")
    else:
        print("Remain Bal", (balance-withdraw))