def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
number = int(input("enter your number: "))
print(Fibonacci(number))