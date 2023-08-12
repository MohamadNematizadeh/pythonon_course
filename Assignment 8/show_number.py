number = int(input('Please enter a number: '))

for i in range(number,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()

for i in range(1,number+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
