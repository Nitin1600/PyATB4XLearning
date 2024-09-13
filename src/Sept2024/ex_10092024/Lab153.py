#try, except and finally

try:
    num1 = int(input("Enter the value of num1:"))
    num2 = int(input("Enter the value of num2:"))
    division = num1 / num2
except ValueError as ve:
    print("ValueError, you have entered a string, instead we want integer")
except ZeroDivisionError as zde:
    print("Zerodivision, please make sure that num 2 entered number is not zero")
else:
    print(f"Result of {num1} / {num2} is {division}")
finally:
    print("This anyhow will be printed")
