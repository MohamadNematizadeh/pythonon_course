from colorama import Fore
import pyfiglet


def show():

    for satr in game_board:
        for cell in satr:
            if cell=="X":
                print(cell ,end=" ")
            elif cell == "O":
                print(cell ,end=" ")
            else:
                
                print(cell, end="  ")
        print()

def chek_game(player1_c, player2_c):
    for i in range(3):
        if game_board[i][0] == player1_c and game_board[i][1] == player1_c and game_board[i][2] == player1_c or game_board[0][i] == player1_c and game_board[1][i] == player1_c and game_board[2][i] == player1_c or game_board[0][2] == player1_c and game_board[1][1] == player1_c and game_board[2][0] == player1_c or game_board[0][0] == player1_c and game_board[1][1] == player1_c and game_board[2][2] == player1_c:
            print("player 1 win!")
            exit()
        if game_board[i][0] == player2_c and game_board[i][1] == player2_c and game_board[i][2] == player2_c or game_board[0][i] == player2_c and game_board[1][i] == player2_c and game_board[2][i] == player2_c or game_board[0][2] == player2_c and game_board[1][1] == player2_c and game_board[2][0] == player2_c or game_board[0][0] == player2_c and game_board[1][1] == player2_c and game_board[2][2] == player2_c:
            print("player 2 win!")
            exit() 

def game():
    player1_ch = "❌"
    player2_ch = "⭕"

    b = 0
    while True:
        if b == 9:
            print("DRAW")
            exit()

        print("player 1")
        while True:
            satr = int(input("satr: "))
            soton = int(input("soton: "))

            if 1 <= satr <= 3 and 1 <= soton <= 3: 
                if game_board[satr-1][soton-1] == "-":
                    b = b + 1
                    game_board[satr-1][soton-1] = Fore.GREEN + player1_ch
                    break
                else:
                    print("this box is full!")      
                     
        show()
        chek_game(Fore.GREEN + player1_ch, Fore.YELLOW + player2_ch)

        if b == 9:
            exit()

        print("player 2")

        while True:  
            satr = int(input("satr: "))
            soton = int(input("soton: "))

            if 1 <= satr <= 3 and 1 <= soton <= 3:
                if game_board[satr-1][soton-1] == "-":
                    game_board[satr-1][soton-1] = Fore.YELLOW + player2_ch
                    b = b + 1
                    break
                else:
                    print("this box is full!")

        show()
        chek_game(Fore.GREEN + player1_ch, Fore.YELLOW + player2_ch)
text = pyfiglet.figlet_format("welcome to Tic Tac Toe game", font="bubble")
print(text)
game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]

show()
game() 