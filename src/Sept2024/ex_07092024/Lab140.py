#Abstraction
#Abstraction - OOPS
#Hiding the details and showing what is required

class Father:
    def __init__(self, name):
        self.name = name

    def loan(self):
        pass

class Pramod(Father):
    def loan(self):
        print("Paid the loan")

pramod = Pramod("1L")
pramod.loan()