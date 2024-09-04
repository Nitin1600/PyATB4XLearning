# #Take input and create a class in python:
#
# class Person():
#
#     def __init__(self):
#         self.name = input("Enter your name: \n")
#         self.age = input("Enter your age: \n")
#         self.phone = input("Enter your phone: \n")
#         self.occupation = input("Enter your occupation: \n")
#
#     def name_of_the_function_to_display(self):
#         print(f"Name is {self.name}")
#         print(f"Age is {self.age}")
#         print(f"Phone is {self.phone}")
#         print(f"Occupation is {self.occupation}")
#
# #create an object:
# person1 = Person()
#
# #Call the display function:
# person1.name_of_the_function_to_display()

#Take input and create a class in python:

class Person():

    def __init__(self):
        self.name = input("Enter your name: \n")
        self.age = input("Enter your age: \n")
        self.phone = input("Enter your phone: \n")
        self.occupation = input("Enter your occupation: \n")

    def name_of_the_function_to_display(self):
        print(f"Name is {self.name}.",f"Age is {self.age}.",f"Phone is {self.phone}.",f"Occupation is {self.occupation}.")

#create an object:
person1 = Person()

#Call the display function:
person1.name_of_the_function_to_display()