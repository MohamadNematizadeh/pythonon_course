Diamond = int(input(" yore enter diameter of the rhombus: "))

for i in range(Diamond):
    print((Diamond - i) * ' ', end='')
    print((i * 2 - 1) * '♠️')

for j in range(Diamond, 0, -1):
    print((Diamond - j) * ' ', end='')
    print((j * 2 - 1) * '♠️')