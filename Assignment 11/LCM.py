def LCM(number_1, number_2):
    x = []
    y = []
    LCM = 0
    result = []
    if number_2 > number_1:
        print(number_1, ",", number_2)
        for i in range(1, number_2+1):
            y.append(number_1 * i)
            x.append(number_2 * i)
    elif number_1 > number_2:
        print(number_2, ",", number_1)
        for i in range(1, number_1+1):
            x.append(number_2 * i) 
            y.append(number_1 * i)
    else:
        LCM = number_1
    for j in y:
        for i in x:
            if j == i:
                result.append(i)
    LCM = result[0]
    return LCM
    

number_1 = int(input(" yore enter number1: "))
number_2 = int(input(" yore enter number2: "))
print("LCM:", LCM(number_1, number_2))