class A:
    def method(A):
        return"Method A"

class B:
    def method(B):
        return"Method B"

class C(B,A):
    pass

c = C()
print(c.method())

