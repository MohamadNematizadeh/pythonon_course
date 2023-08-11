7 -> exit
input your number ->  
"""))

    if op == 7:
        exit(0)

    number = float(input("number = "))

    if op == 1:
        result = number + 273.15
        print(f"{number} Celsius -> {result} Kelvin")

    elif op == 2:
        result = (number * (9 / 5)) + 32
        print(f"{number} Celsius -> {result} Fahrenheit")

    elif op == 3:
        result = number - 273.15
        print(f"{number} Kelvin -> {result} Celsius")

    elif op == 4:
        result = (number - 273.15) * (9 / 5) + 32
        print(f"{number} Kelvin -> {result} Fahrenheit")

    elif op == 5:
        result = (number - 32) * (5 / 9)
        print(f"{number} Fahrenheit -> {result} Celsius")
