class GF:
    def car(self):
        return "Old Car"

class F(GF):
    pass
    # def car(self):
    # return "Honda Civic"

class S(F):
    pass
    # def car(self):
    # return "lambo"

son = S()
print(son.car())