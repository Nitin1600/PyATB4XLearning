"""
(Q)Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

"""
#Method1:

n = int(input("Enter the size of fibonacci series: "))
f1 = 0
f2 = 1
if n <= 0:
    print("Size of fibonacci series should be positive integer")
elif n == 1:
    print(f1)
else:
    #Print the first two numbers of the series
    print(f1, f2, end=" ")
    for i in range(n):
        sum = f1+f2
        print(sum, end=" ")
        f1 = f2
        f2 = sum

#Method2:

# f = int(input("ENter the number to find find fibonacci of: "))
# a = 0
# b = 1
# fib = 0
# if f == 0:
#     print(0)
# elif f == 1:
#     print(0)
# else:
#     for i in range(2, f+1):
#         fib=a+b
#         a = b
#         b = fib
#     print(fib, end=" ")


