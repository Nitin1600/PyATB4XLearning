class Grandparent:
    key_gold = "1kg"
    def grandparent_method(self):
        return "Grandparent's method"

class Father(Grandparent):
    def father_method(self):
        return "Father's method"

class Child(Father):
    mac_m3_apple = "M3 Max"
    def child_method(self):
        return "child's method"

child = Child()
print(child.grandparent_method())