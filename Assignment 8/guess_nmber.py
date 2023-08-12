import random
score_player1 = 0
score_player2 = 0
score_computer = 0

while True:
    start_game = int(input("1-player1 vs player2\n2-player2 vs player1\n3-player vs computer\n4-computer vs player\n\tenter youre number: "))
    if start_game == 1:
        number = int(input("player1: enter youre number:(range = 0 to 100)\t"))
        while True:
            input_number = int(input("player2: enter youre number:(range = 0 to 100)\t"))
            if input_number == number :
                print("you win!")
                score_player2 += 1
                break
            elif input_number > number:
                print("player2 go down!")
            else:
                print("player2 go up!")
        
    elif start_game == 2:
        number = int(input("player2: enter youre number:(range = 0 to 100)\t"))
        while True:
            input_number = int(input("player1: enter youre number:(range = 0 to 100)\t"))
            if input_number == number :
                print("you win!")
                score_player1 += 1
                break
            elif input_number > number:
                print("player1 go down!")
            else:
                print("player1 go up!")

    elif start_game == 3:
        number = int(input("player1: enter youre number:(range = 0 to 100)\t"))
        upperـbound = 100
        lowerـbound = 0
        input_number = random.randint(lowerـbound, upperـbound)
        while True:
            if input_number == number :
                print(f"computer number is:{input_number}", "computer win!")
                score_computer += 1
                break
            elif input_number > number:
                print(f"computer number is:{input_number}", "go down!")
                upperـbound = input_number
                input_number = random.randint(lowerـbound, upperـbound-1)
            else:
                print(f"computer number is:{input_number}", "go up!")
                lowerـbound = input_number
                input_number = random.randint(lowerـbound + 1, upperـbound)


    elif start_game == 4:
        number = random.randint(0, 100)
        while True:
            input_number = int(input("enter youre number:\t"))
            if input_number == number :
                print("you win!")
                score_player1 += 1
                break
            elif input_number > number:
                print("go down!")
            else:
                print("go up!")

    else:
        print("youre number doesnt find") 

    try_again = input("do you want to try again?(y, n):\t") # try again
    if try_again == "n":
        break
print(f"computer score is {score_computer}, player1 scors is {score_player1}, player2 scors is {score_player2}")