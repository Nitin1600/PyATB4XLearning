class Calc:

    def __int__(self):
        print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

obj_ref = Calc()

    #a = int(input("Enter the value of a"))

    #b = int(input("Enter the value of b"))

output_sum = obj_ref.sum(4,6)
print(output_sum)

#output_sub = obj_ref.sub(5,6)

#output_mul = obj_ref.mul(6,7)

#output_div = obj_ref.div(8,9)