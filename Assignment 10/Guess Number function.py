import random

def check_number(number, number_input, player):
    if number_input == number :
        return f"{player} is win!"
    elif number_input > number:
        return f"{player} go down!"
    else:
        return f"{player} go up!"

def game(number):
    if number == 1 or number == 2 or number == 4:
        if number == 4:
            numberr = random.randint(0, 100)
        else:
            numberr = int(input(f"player{number}: enter youre number:(range = 0 to 100)\t"))
        if number == 4 or number == 2:
            number == 1
        else:
            number += 1
        while True:
            input_number = int(input(f"player{number}: enter youre number:(range = 0 to 100)\t"))
            print(check_number(numberr, input_number, f"player{number}"))
            if "win" in check_number(numberr, input_number, f"player{number}"):
                break
    elif number == 3:
        numberr = int(input("player1: enter youre number:(range = 0 to 100)\t"))
        upperـbound = 100
        lowerـbound = 0
        input_number = random.randint(lowerـbound, upperـbound)
        while True:
            check = check_number(numberr, input_number, "computer")
            if "win" in check :
                print(check)
                break
            elif "down" in check:
                print(f"computer number is:{input_number}", check)
                upperـbound = input_number
                input_number = random.randint(lowerـbound, upperـbound-1)
            elif "up" in check:
                print(f"computer number is:{input_number}", check)
                lowerـbound = input_number
                input_number = random.randint(lowerـbound + 1, upperـbound)
    else:
        print("youre number doesnt find") 

while True:
    start_game = int(input("1_player1 vs player2\n2_player2 vs player1\n3_player vs computer\n4_computer vs player\n\tenter youre number: "))
    game(start_game)
    try_again = input("do you want to try again?(y, n):\t") # try again
    if try_again == "n":
        break
print("good bye!")