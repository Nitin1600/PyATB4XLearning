class Car:

    model = None
    name = None
    password = 123

    def __init__(self):
        self.password = "amith"

    def change_password(self):
        print(self.password)

obj_ref = Car()
print(obj_ref.password)
obj_ref.change_password()