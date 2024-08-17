"""

Take two numbers and fetch 

-Add,Div,Mul,Pow,Sub,Pow,Max.
-Format output in string format

"""

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

max_num = max(num1,num2)
print("Max is: ", f"{max_num}")

pow = num1**num2
print("Pow is: ", f"{pow}")

Sum = num1+num2
print("Sum is: ", f"{Sum}")

Sub = num1-num2
print("Sub is: ", f"{Sub}")

Mul = num1*num2
print("Mul is: ", f"{Mul}")

Div = num1/num2
print("Div is: ",f"{Div}")