class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def confirm_login(self):
        if self.email == "pramod@gmail.com" and self.password == "Pass123":
            print("Allowed to login")
        else:
            print("Not allowed")

email = input("Enter your email \n")
password = input("Enter your password \n")

vwo_obj = VWOLoginPage(email, password)
vwo_obj.confirm_login()

pramod = VWOLoginPage("pramod@gmail.com", "Pass123")
pramod.confirm_login()