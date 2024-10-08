#Multiple inheritance

class Father:
    key = "ABC"
    __password = "private"

    def __show_password(self):
        print(self.__password)

    def father_money(self):
        return 5

    def home(self):
        return"This father's money"

    def show_everything(self):
        self.__show_password()

class Mother:

    def mother_money(self):
        return 2

    def home(self):
        return"This is mother's money"

class Son(Mother, Father):
    pass

class Son2(Father, Mother):
    pass

s = Son()
print(s.father_money())
print(s.mother_money())
print(s.home())
print(s.key)
s.show_everything()