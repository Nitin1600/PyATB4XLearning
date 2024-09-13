#Method overloading
#Python does not support method over loading
#in the traditinal sense

class MathUtils(object): #Is- A Object #single inheritance
    #Method overloading - not supported

    #def add(self, a, b):
        #return a + b

    #def add(selfself, a, b):
        #return a + b + c

    def add(self, a, b, c=10, d=1):
        return a + b + c + d

math = MathUtils()
op1 = math.add(1,2)
print(op1)