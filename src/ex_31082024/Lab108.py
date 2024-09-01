class Dog:
    name = None
    age = None
    breed = None

    def __init__(self,name,age):
        print("Called,object is created!")
        self.name = name
        self.age = age

    def sleep(self):
        print("sleeping")
        print("who is sleeping -> ", self.name, self.age)
        return None

dog1 = Dog("Chow", 10)
print(dog1.name)
dog1.sleep()

dog2 = Dog("Mow", 20)
print(dog2.name)
dog2.sleep()
