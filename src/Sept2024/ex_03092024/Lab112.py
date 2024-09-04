class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a -self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

obj_ref = Calc(3,4)
obj_ref2 = Calc(3,4)
obj_ref3 = Calc(3,4)
obj_ref4 = Calc(3,4)

output = obj_ref.sum()
print(output)