def gcd(num1, num2):
    x = []
    y = []
    gcd = 0
    result = []
    for i in range(1, num2+1):
        if num2 % i == 0:
            y.append(i)
    for i in range(1, num1+1):
        if num1 % i == 0:
            x.append(i) 

    for j in y:
        for i in x:
            if j == i:
                result.append(i)
    gcd = result[len(result)-1]  
    return gcd

num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))
print("gcd:", gcd(num1, num2))