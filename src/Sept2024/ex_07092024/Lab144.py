#Static Method: A static method is a method that belongs to a class
#rather than an instance of a class


class O:

    @staticmethod
    def sum(a, b):
        return a + b

class MathOperations(O):

    def div(self, a, b):
        return a / b

    def mul(self, a, b):
        return a * b

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

#Non-static in nature: Object creation is mandatory
obj_ref = MathOperations()
output = obj_ref.div(10,5)
output2 = obj_ref.mul(10,5)
print(output)
print(output2)

#Static methods can be called directly without the object.
print(MathOperations.sum(10,5))
print(MathOperations.sub(10,5))
print(O.sum(4,5))