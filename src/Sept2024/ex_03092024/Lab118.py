class Person:

    def __init__(self,name):
        self.name = name

    def walk(self):
        return self.name

amith = Person("amith")
pramod = Person("pramod")
print(amith.name)
print(pramod.name)
print("who is walking with the object pramod -> ", pramod.walk())