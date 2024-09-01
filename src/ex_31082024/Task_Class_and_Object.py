from multiprocessing.connection import address_type


class Employee:

    name = None
    age = None
    phone = None
    address = None
    eid = None

    def __init__(self,name,age,phone_num,address,eid):
        self.name = name
        self.age = age
        self.phone_num = phone_num
        self.address = address
        self.eid = eid

    def walk(self):
        print("Walks")

    def talk(self):
        print("Talks")

employee1 = Employee(input("Enter name: "), int(input("Enter age: ")), int(input("Enter phone num: ")), input("Enter address: "), input("Enter eid: "))
print(employee1.name)
print(employee1.age)
print(employee1.phone_num)
print(employee1.address)
print(employee1.eid)
employee1.walk()
employee1.talk()

print("--------------------")
print("--------------------")

employee2 = Employee(input("Enter name: "), int(input("Enter age: ")), int(input("Enter phone num: ")), input("Enter address: "), input("Enter eid: "))
print(employee2.name)
print(employee2.age)
print(employee2.phone_num)
print(employee2.address)
print(employee2.eid)
employee2.walk()
employee2.talk()