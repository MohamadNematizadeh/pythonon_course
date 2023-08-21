number = int(input(" yoer ernter a number: "))
x = [0,number,1]
for i in range(2):
    for i in range(x[0],x[1],x[2]):
        print(((number - i) * "  "), ((i * 2 - 1) * "💛"), ((number - i) * "    "), ((i * 2 - 1) * "💛"))
    x = [number, 0, -1]