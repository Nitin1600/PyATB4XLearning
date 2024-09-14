# class Shape:
#
#     def area(self):
#         pass
#
# class Rectangle(Shape):
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
# shapes = [Rectangle(3,4), Circle(10)]
# for shape in shapes:
#     print(shape.area())

#Exercise2

# class Animal:
#     def speak(self):
#         print("Animal speaks!!")
#
# class Dog(Animal):
#     def bark(self):
#         print("Woof!")
#
# my_dog = Dog()
# my_dog.speak()  #Inheritedd from Animal
# my_dog.bark()  #Specific to Dog

#Exercise 3

# class A:
#     def method_a(self):
#         print("Method A")
#
# class B:
#     def method_b(self):
#         print("Method B")
#
# class C(A,B):
#     def method_c(self):
#         print("Method C")
#
# my_object = C()
# my_object.method_a() #Inherited from A
# my_object.method_b() #Inherited from B
# my_object.method_c() #Specific to C

#Exercise 4: MRO- Handle Case

# class A:
#     def greet(self):
#         print("Hello from class A")
#
# class B:
#     def greet(self):
#         print("Hello from class B")
#
# class C(A,B):
#     pass
#
# class D(B,A):
#     pass
#
# obj1 = C()
# obj1.greet()
#
# obj2 = D()
# obj2.greet()
#
# print(C.mro())
# print(D.mro())

#Exercise 5: Multilevel Inheritance

# class Vehicle:
#     def start_engine(self):
#         print("Engine started")
#
# class Car(Vehicle):
#     def drive(self):
#         print("Driving the car")
#
# class SportsCar(Car):
#     def race(self):
#         print("Racing the Sports Car")
#
# my_car = SportsCar()
# my_car.start_engine()  #Inherited from Vehicle
# my_car.drive() #Inherited from Car
# my_car.race()  #Specific to SportsCar

#Exercise 6: Hierarchial Inheritance

# class Animal:
#     def speak(self):
#         print("Animal Speaks!")
#
# class Dog(Animal):
#     def bark(self):
#         print("Woof!")
#
# class Cat(Animal):
#     def meow(self):
#         print("Meow!")
#
# my_dog = Dog()
# my_dog.speak() #Inherited from Animal
# my_dog.bark() #Specific to Dog
#
# my_cat = Cat()
# my_cat.speak() #Inherited from Animal
# my_cat.meow() #Specific to Cat

#Exercise 7: Abstract Method

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class Rectangle(Shape):
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
#
# rect = Rectangle(4,5)
# print(rect.area())
# print(rect.perimeter())
#
# circle = Circle(3)
# print(circle.area())
# print(circle.perimeter())

#Exercise 8:

# try:
#     result = 10 / 0
# except ZeroDivisionError as error:
#     print("Error", error)




