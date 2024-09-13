#Hybrid inheritance

#Multiple levels of inheritance
#such as single, multiple and multilevel

class A: #Father
    def methodA(self):
        return"Method A"

class B(A): #Pramod
    def methodB(self):
        return "Method B"

class C(A): #Lucky
    def methodC(self):
        return "Method C"

class D(B,C):#Sister  #Multplr, multilevel - MRO(Method Resolution Order
    def methodD(self):
        return"Method D"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())
