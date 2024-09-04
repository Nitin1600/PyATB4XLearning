a = 10

class Person:

    b = 11
    c = 11

    def print_infor(self):
        global a
        a = "Hello"
        print(self.b)
        print(self.c)

obj_ref = Person()
obj_ref.print_infor()
print(a)