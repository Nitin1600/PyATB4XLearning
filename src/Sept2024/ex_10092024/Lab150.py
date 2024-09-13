print("-----Start of the Programme-----")
try:
    a = int(input("Enter the num1"))  # ValueError: invalid literal for int() with base 10: 'a'
    b = int(input("Enter th num2"))  # ZeroDivisionError: division by zero
    c = a / b
    print("Result Div is ", c)
except Exception as e:
    print(e)
    print("Please check your inputs, it should not be a string or integer")

print("-----End of the Programme-----")