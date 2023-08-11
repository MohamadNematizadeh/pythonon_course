import math

while True:
    print("""
    Enter the desired operation number:
    1 -> +    8 -> sin
    2 -> -    9 -> cos
    3 -> *    10 -> tan
    4 -> /    11 -> cot
    5 -> **   12 -> abs
    6 -> sqr  13 -> rou
    7 -> fac  14 -> exit
    """, end="")

    op = int(input())

    if op == 14:
        exit(0)


    if 1 <= op <= 5:
        number_1 = float(input("enter ferst number: "))
        number_2 = float(input("enter second number: "))

    elif 6 <= op <= 13:
        number_1 = float(input("enter number: "))
            
    if op == 1:
        result = number_1 + number_2

    elif op == 2:
        result = number_1 - number_2

    elif op == 3:
        result = number_1 * number_2

    elif op == 4:
        result = number_1 / number_2

    elif op == 5:
        result = number_1 ** number_2

    elif op == 6:
        result = math.sqrt(number_1)

    elif op == 7:
        result = math.factorial(number_1)
        
    elif op == 8:
        n = math.radians(number_1)
        result = math.sin(n)

    elif op == 9:
        n = math.radians(number_1)
        result = math.cos(n)

    elif op == 10:
        n = math.radians(number_1)
        result = math.tan(n)

    elif op == 11:
        n = math.radians(number_1)
        result = math.atan(n)

    elif op == 12:
        result = abs(number_1)

    elif op == 13:
        result = round(number_1)

    print(result)