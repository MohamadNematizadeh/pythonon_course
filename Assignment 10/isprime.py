def isprime(number):
    numbers = []
    for i in range(1, number):
        if (i != 1) and ((number % i) == 0) and(i != number):
            numbers.append(i)
            number_status = "not prime"
    if len(numbers) == 0:
        number_status = "prime"

    return number_status
number = int(input("enter your number: "))

print("your number is",isprime(number))