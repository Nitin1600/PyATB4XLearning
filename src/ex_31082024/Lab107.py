class Dog:
    name = None
    breed = None
    color = None

    def walk(self):
        print("walks_more")

    def bark(self):
        print("barks_less")

    def food(self,food):
        print(food)

dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.walk()

print("-------------------")

dog2 = Dog()
print(dog2.name)
dog2.name = "Mow"
print(dog2.name)

dog3 = dog1