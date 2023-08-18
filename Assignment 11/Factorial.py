def Factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return Factorial(n - 1) * n

number = int(input("enter your numebr: "))
print(Factorial(number))