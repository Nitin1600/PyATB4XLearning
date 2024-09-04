from src.ex_27082024.Lab0073 import make_pizza


class Car:

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting the car of name: " + self.name)
        print("Starting the car of make: " + self.make)
        print("Starting the car of model: " + self.model)

lambo = Car("lambo", "V2", "2024")
lambo.start_engine()

Xuv = Car("Xuv", "V4", "2022")
Xuv.start_engine()