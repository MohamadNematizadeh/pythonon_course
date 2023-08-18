def number(number):
    number = str(number)
    n1 = number
    n2 = number+number
    n3 = number+number+number
    return int(n1) + int(n2) + int(n3)
number_user = int(input("enter youre number: "))
print(number(number_user))