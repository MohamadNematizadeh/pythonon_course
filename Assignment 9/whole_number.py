number = abs(int(input("enter your number:\n")))
numbers = []
for i in range(1, number):
    if (number % i) == 0:
        numbers.append(i)

if sum(numbers) == number:
    print("your number is whole!")
else:
    print("your number is not whole!")