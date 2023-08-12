number = int(input("enter youre number:\n")) # 5
for i in range(4, number + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()