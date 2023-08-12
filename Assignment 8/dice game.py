import random
import pyfiglet

title = pyfiglet.figlet_format("-Game--Dise-", font="slant")
print(title)
Dise_number = 0
Sum_numbers = 0
c = 0

while Dise_number != 6:
    Dise_number = random.randint(1,6)
    c += 1
    print(f"Number {c} = {Dise_number}")
    Sum_numbers += Dise_number

print("Sum = ",Sum_numbers)