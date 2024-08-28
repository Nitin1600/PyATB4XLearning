# def print_arguments(*args):
#      print(args)
# # for i in args:
# #     print(i)
# print_arguments("amith", "pinto", "rao")
# print_arguments("amith", "pinto",)
# # print_arguments()
# print_arguments(10)
# print_arguments("amith", 10, True, "pinto", False)
# print_arguments("amith", "pinto", "rao")

# year = int(input("Enter the year:\n"))
# if (year %4 == 0 and year %100 != 0) or (year %400 == 0):
#     print("It's a leap year")
# else:
#     print("It's not a leap year")

# a = float(input("Enter side a:\n"))
# b = float(input("Enter side b:\n"))
# c = float(input("Enter side c:\n"))
#
# if a == b == c:
#     print("Equvilateral")
# elif a == b or b == c or a == c:
#     print("Isosceles")
# else:
#     print("Scalene")

# for i in range(1,101,1):
#     if i%3 == 0 and i%5 == 0:
#         print("Fizzbuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# num = int(input("Enter the number:"))
# fact = 1
# if num == 0 or num == 1:
#     fact=1
#     print(1)
# else:
#     # for i in range(1, num+1, 1):
#     #     fact = fact*i
#     # print(f"The factorial of {num} is {fact}")
#     i = 1
#     while(i <= num):
#         fact = fact*i
#         i = i+1
#     print(fact)