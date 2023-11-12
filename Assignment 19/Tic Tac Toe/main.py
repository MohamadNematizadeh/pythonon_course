import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

app = QApplication(sys.argv)
player = 1
p_1 = 0 
p_2 = 0
k = 0
loder = QUiLoader()
main_window2 = loder.load("TicTacToe_start.ui")
main_window2.show()

def start_p_p_game():
    if main_window2.player_player.isChecked():
        main_window = loder.load("TicTacToe.ui")
        main_window.show()
        main_window2.hide()

        def play(row,col):
            global player
            global k

            main_window.player_1.setText(str(p_1))
            main_window.player_2.setText(str(p_2))
            
            if buttons[row][col].text() == "":
                if player == 1:
                    buttons[row][col].setText("X")
                    buttons[row][col].setStyleSheet("color:#34c3be;")
                    player = 2
                    k += 1
                    check()

                elif player == 2:
                    buttons[row][col].setText("O")
                    buttons[row][col].setStyleSheet("color: #f2b138;")
                    player = 1
                    k += 1
                    check()

        def check():
            global p_1
            global p_2
            global k
            
            for j in range(3):
                if buttons[j][0].text() == "X" and buttons[j][1].text() == "X" and buttons[j][2].text() == "X"or buttons[0][j].text() == "X" and buttons[1][j].text() == "X" and buttons[2][j].text() == "X" or buttons[0][2].text() == "X" and buttons[1][1].text() == "X" and buttons[2][0].text() == "X" or buttons[0][0].text() == "X" and buttons[1][1].text() == "X" and buttons[2][2].text() == "X":
                    p_1 += 1
                    main_window.player_1.setText(str(p_1))
                    main_window.player_2.setText(str(p_2))
                    msg_box = QMessageBox(text= "Player 1 wins.")
                    msg_box.exec_()
                    new_game()
                    k = 0
                    break

                elif buttons[j][0].text() == "O" and buttons[j][1].text() == "O" and buttons[j][2].text() == "O"or buttons[0][j].text() == "O" and buttons[1][j].text() == "O" and buttons[2][j].text() == "O" or buttons[0][2].text() == "O" and buttons[1][1].text() == "O" and buttons[2][0].text() == "O" or buttons[0][0].text() == "O" and buttons[1][1].text() == "O" and buttons[2][2].text() == "O":
                    p_2 += 1
                    main_window.player_1.setText(str(p_1))
                    main_window.player_2.setText(str(p_2))
                    msg_box = QMessageBox(text= "Player 2 wins.")
                    msg_box.exec_()
                    new_game()
                    k = 0
                    break
            
                elif k == 9:
                    main_window.player_1.setText(str(p_1))
                    main_window.player_2.setText(str(p_2))
                    msg_box = QMessageBox(text= "The game equalised.")
                    msg_box.exec_()
                    new_game()
                    k = 0
                    break

        def about():
            msg_box1 = QMessageBox(text= "I,m Mohammad \n  my github adres: https://github.com/MohamadNematizadeh")
            msg_box1.exec_()

        def new_game():
            for i in range(3):
                for j in range(3):
                    buttons[i][j].setText("")
                    buttons[i][j].setStyleSheet("background-color: rgb(125, 125, 125);")
                
        buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
                [main_window.btn_4, main_window.btn_5, main_window.btn_6],
                [main_window.btn_7, main_window.btn_8, main_window.btn_9]]

        for i in range(3):
            for j in range(3):
                buttons[i][j].clicked.connect(partial(play,i ,j))

        main_window.about.clicked.connect(about)
        main_window.n_g.clicked.connect(new_game)

def start_p_c_game():
    if main_window2.player_CPU.isChecked():
        main_window = loder.load("TicTacToe.ui")
        main_window.show()
        main_window2.hide()
            
        def play(row,col):
            global player
            global k

            main_window.player_1.setText(str(p_1))
            main_window.player_2.setText(str(p_2))
            
            if buttons[row][col].text() == "":
                if player == 1:
                    buttons[row][col].setText("X")
                    buttons[row][col].setStyleSheet("color: #34c3be;")
                    player = 2
                    k += 1
                    check()

                if player == 2:
                    while True:
                        c_row = random.randint(0, 2)
                        c_col = random.randint(0, 2)
                        
                        if buttons[c_row][c_col].text() == "":
                            buttons[c_row][c_col].setText("O")
                            buttons[c_row][c_col].setStyleSheet("color: #f2b138;")
                            player = 1
                            k += 1
                            check()
                            break

        def check():
            global p_1
            global p_2
            global k
            
            for j in range(3):
                if buttons[j][0].text() == "X" and buttons[j][1].text() == "X" and buttons[j][2].text() == "X"or buttons[0][j].text() == "X" and buttons[1][j].text() == "X" and buttons[2][j].text() == "X" or buttons[0][2].text() == "X" and buttons[1][1].text() == "X" and buttons[2][0].text() == "X" or buttons[0][0].text() == "X" and buttons[1][1].text() == "X" and buttons[2][2].text() == "X":
                    p_1 += 1
                    main_window.player_1.setText(str(p_1))
                    main_window.player_2.setText(str(p_2))
                    msg_box = QMessageBox(text= "Player 1 wins.")
                    msg_box.exec_()
                    new_game()
                    k = 0
                    break

                elif buttons[j][0].text() == "O" and buttons[j][1].text() == "O" and buttons[j][2].text() == "O"or buttons[0][j].text() == "O" and buttons[1][j].text() == "O" and buttons[2][j].text() == "O" or buttons[0][2].text() == "O" and buttons[1][1].text() == "O" and buttons[2][0].text() == "O" or buttons[0][0].text() == "O" and buttons[1][1].text() == "O" and buttons[2][2].text() == "O":
                    p_2 += 1
                    main_window.player_1.setText(str(p_1))
                    main_window.player_2.setText(str(p_2))
                    msg_box = QMessageBox(text= "Player 2 wins.")
                    msg_box.exec_()
                    new_game()
                    k = 0
                    break
            
                elif k == 9:
                    main_window.player_1.setText(str(p_1))
                    main_window.player_2.setText(str(p_2))
                    msg_box = QMessageBox(text= "The game equalised.")
                    msg_box.exec_()
                    new_game()
                    k = 0
                    break

        def about():
            msg_box1 = QMessageBox(text= "I,m Mohammad \n  my github adres: https://github.com/MohamadNematizadeh")
            msg_box1.exec_()
            
        def new_game():
            k = 0
            for i in range(3):
                for j in range(3):
                    buttons[i][j].setText("")
                    buttons[i][j].setStyleSheet("background-color: rgb(125, 125, 125);")
                
        buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
                [main_window.btn_4, main_window.btn_5, main_window.btn_6],
                [main_window.btn_7, main_window.btn_8, main_window.btn_9]]

        for i in range(3):
            for j in range(3):
                buttons[i][j].clicked.connect(partial(play,i ,j))

        main_window.about.clicked.connect(about)
        main_window.n_g.clicked.connect(new_game)

main_window2.player_player.toggled.connect(start_p_p_game)
main_window2.player_CPU.toggled.connect(start_p_c_game)

app.exec_()