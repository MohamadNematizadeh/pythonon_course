def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)
        
number1 = int(input("yore enter first numbers: "))
number2 = int(input("yore enter second numbers: "))
print(GCD(number1, number2))