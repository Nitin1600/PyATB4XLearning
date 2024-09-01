class Person:
    name = None
    id = None
    age = None
    email = None
    height = None
    address = None
    native = None
    location = None
    color = None

    def talk(self):
        print("I am talking")

    def sleep(self,name):
        print("I am a method!!")
        print("sleep",name)

    def sleep2(self,name):
        print("I am a method!!")
        return None

    def walk(self):
        print("I am walking")

    def walk_reference(self):
        return"I am walking"

tushar = Person()
tushar.name = "tushar"
print(tushar.name)
tushar.talk()

rajyalakshmi = Person()
rajyalakshmi.name = "rajyalakshmi"
print(rajyalakshmi.name)
rajyalakshmi.talk()
