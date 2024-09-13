#Method overriding - Same name in both parent and child
#Child always overrides the parent functions
#Super means call my parent function

class Grandfather:
    x = 10
    def home(self):
        print("Old home")

class Father(Grandfather):
    a = 10
    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)

class Son(Father):
    b = 10
    def home(self):
        super().home() #Father behaviour by super()
        print(super().a) #Father attributes by super()
        print("No home")
        print(self.b)

        #Self - Me
        #Super - Father, Parent, Super Class

pramod = Son()
pramod.home()
print(pramod.x)