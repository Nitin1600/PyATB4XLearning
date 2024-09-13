#Hierarchial Inheritance

class Father:
    def BHK1(self):
        print("1BHK")

class Pramod(Father):
    def BHK2(self):
        print("2BHK")

class Amith(Father):
    def BHK3(self):
        print("3BHK")

class Lucky(Father):
    def no_house(self):
        print("No_house")

pramod = Pramod()
pramod.BHK1()
pramod.BHK2()

amith = Amith()
amith.BHK1()
amith.BHK3()
#amith.BHK2()? This belong to Pramod