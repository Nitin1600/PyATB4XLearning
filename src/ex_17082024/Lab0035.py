'''(Q)Write a Python program to calculate the
area of a circle given its radius using the formula
 area=π×r^2``` ( Take pie as 3.14)'''


import math

radius = float(input("Enter the radius: \n"))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius,2)
area2 = 3.14 * (radius**2)
print("Area of the circle -> ", area)
print("Area of the circle -> ", area2)
print(f"Area of the circle -> {area2:.2f}")

print(3.14 * (float(input("Enter the radius: \n"))**2))
