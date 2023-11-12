from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
import random
from functools import partial
class Hangman(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        loader = QUiLoader()
        self.ui = loader.load("hangman.ui", None)
        self.ui2 = loader.load("hangman_game.ui", None)
        self.ui.show()
        self.heart = 5
        self.show_word = []
        self.ui.btn_check.clicked.connect(self.check)
        self.Animals_easy = ["cat", "dog", "cow", "pig", "fly", "eik", "fox", "bat", "ant", "bee"]
        self.Animals_medium = ["deer", "crab", "duck", "fish", "goat", "wolf", "tang", "lion", "hare", "frog"]
        self.Animals_difficult = ["dhole", "bison", "fossa", "lemur", "xerus", "prawn", "moose", "liger", "zorse", "sloth"]
        self.Colors_easy = ["red", "blue", "black", "white", "green", "orange", "gold", "gray", "coral", "purple"]
        self.Colors_medium = ["teal", "cyan", "pink", "bice", "puce", "jade", "aero", "fawn", "finn", "erin"]
        self.Colors_difficult = ["azure", "ebony", "beige", "yellow", "coquelicot", "magenta", "fallow", "champagne", "hibiscus", "ginger"]
        self.Musical_instruments_easy = ["harp", "flute", "guitar", "drums", "tuba", "organ", "sitar", "piano", "ukelele", "violin"]
        self.Musical_instruments_medium = ["banjo", "bugle", "bagpipes", "accordion", "bassoon", "keyboard", "maracas", "triangle", "cymbals", "clarinet"]
        self.Musical_instruments_difficult = ["didgeridoo", "mandolin", "harpsichord", "saxophone", "xylophone", "trombone", "harmonica", "mridangam", "euphonium", "harmonium"]
        self.Sports_easy = ["soccer", "tennis", "golf", "boxing", "skiing", "pool", "rugby", "karate", "archery", "judo"]
        self.Sports_medium = ["basketball", "baseball", "volleyball", "cricket", "bowling", "fencing", "rowing", "handball", "sailing", "hiking"]
        self.Sports_difficult = ["badminton", "snowboarding", "skateboarding", "taekwondo", "gymnastics", "paddleboarding", "equestrian", "snowmobiling", "bobsledding", "orienteering"]
        self.Clothes_easy = ["skirt", "cap", "hat", "vest", "scarf", "dress", "boots", "tie", "socks", "ring"]
        self.Clothes_medium = ["bathrobe", "jumper", "overalls", "mittens", "diaper", "singlet", "cardigan", "sweater", "swimsuit", "blazer"]
        self.Clothes_difficult = ["sunglasses", "pullover", "waistcoat", "earrings", "trenchcoat", "earmuffs", "umbrella", "mortarboard", "longsleevetop", "businessshoes"]
        self.ui2.btn_a.clicked.connect(partial(self.start_game, "a"))
        self.ui2.btn_b.clicked.connect(partial(self.start_game, "b"))
        self.ui2.btn_c.clicked.connect(partial(self.start_game, "c"))
        self.ui2.btn_d.clicked.connect(partial(self.start_game, "d"))
        self.ui2.btn_e.clicked.connect(partial(self.start_game, "e"))
        self.ui2.btn_f.clicked.connect(partial(self.start_game, "f"))
        self.ui2.btn_g.clicked.connect(partial(self.start_game, "g"))
        self.ui2.btn_h.clicked.connect(partial(self.start_game, "h"))
        self.ui2.btn_i.clicked.connect(partial(self.start_game, "i"))
        self.ui2.btn_j.clicked.connect(partial(self.start_game, "j"))
        self.ui2.btn_k.clicked.connect(partial(self.start_game, "k"))
        self.ui2.btn_l.clicked.connect(partial(self.start_game, "l"))
        self.ui2.btn_m.clicked.connect(partial(self.start_game, "m"))
        self.ui2.btn_n.clicked.connect(partial(self.start_game, "n"))
        self.ui2.btn_o.clicked.connect(partial(self.start_game, "o"))
        self.ui2.btn_p.clicked.connect(partial(self.start_game, "p"))
        self.ui2.btn_q.clicked.connect(partial(self.start_game, "q"))
        self.ui2.btn_r.clicked.connect(partial(self.start_game, "r"))
        self.ui2.btn_s.clicked.connect(partial(self.start_game, "s"))
        self.ui2.btn_t.clicked.connect(partial(self.start_game, "t"))
        self.ui2.btn_u.clicked.connect(partial(self.start_game, "u"))
        self.ui2.btn_v.clicked.connect(partial(self.start_game, "v"))
        self.ui2.btn_w.clicked.connect(partial(self.start_game, "w"))
        self.ui2.btn_x.clicked.connect(partial(self.start_game, "x"))
        self.ui2.btn_y.clicked.connect(partial(self.start_game, "y"))
        self.ui2.btn_z.clicked.connect(partial(self.start_game, "z"))



    def check(self):
        if self.ui.rbtn_easy.isChecked() == True:
            if self.ui.rbtn_colors.isChecked() == True:
                self.word = random.choice(self.Colors_easy)
                self.start_game()
            elif self.ui.rbtn_sports.isChecked() == True:
                self.word = random.choice(self.Sports_easy)
                self.start_game()
            elif self.ui.rbtn_clothes.isChecked() == True:
                self.word = random.choice(self.Clothes_easy)
                self.start_game()
            elif self.ui.rbtn_animals.isChecked() == True:
                self.word = random.choice(self.Animals_easy)
                self.start_game()
            elif self.ui.rbtn_musical.isChecked() == True:
                self.word = random.choice(self.Musical_instruments_easy)
                self.start_game()
            else:
                self.ui.text_state.setText("choose category of game:)")
            
        elif self.ui.rbtn_medium.isChecked() == True:
            if self.ui.rbtn_colors.isChecked() == True:
                self.word = random.choice(self.Colors_medium)
                self.start_game()
            elif self.ui.rbtn_sports.isChecked() == True:
                self.word = random.choice(self.Sports_medium)
                self.start_game()
            elif self.ui.rbtn_clothes.isChecked() == True:
                self.word = random.choice(self.Clothes_medium)
                self.start_game()
            elif self.ui.rbtn_animals.isChecked() == True:
                self.word = random.choice(self.Animals_medium)
                self.start_game()
            elif self.ui.rbtn_musical.isChecked() == True:
                self.word = random.choice(self.Musical_instruments_medium)
                self.start_game()
            else:
                self.ui.text_state.setText("choose category of game:)")

        elif self.ui.rbtn_hard.isChecked() == True:
            if self.ui.rbtn_colors.isChecked() == True:
                self.word = random.choice(self.Colors_difficult)
                self.start_game()
            elif self.ui.rbtn_sports.isChecked() == True:
                self.word = random.choice(self.Sports_difficult)
                self.start_game()
            elif self.ui.rbtn_clothes.isChecked() == True:
                self.word = random.choice(self.Clothes_difficult)
                self.start_game()
            elif self.ui.rbtn_animals.isChecked() == True:
                self.word = random.choice(self.Animals_difficult)
                self.start_game()
            elif self.ui.rbtn_musical.isChecked() == True:
                self.word = random.choice(self.Musical_instruments_difficult)
                self.start_game()
            else:
                self.ui.text_state.setText("choose category of game:)")
        else:
            self.ui.text_state.setText("choose level of game:(")
        for i in range(len(self.word)):
            self.show_word.append("_ ")
        print(self.word)
        

    def start_game(self, l=""):
        self.ui2.show()
        self.ui.close()
        self.word
        idx = 0
        if l != "":
            self.ui2.label_h.setText("❤️"*self.heart)
            if self.heart == 0:
                self.ui2.label_h.setText("Game over!:(")
            if not("_ " in self.show_word):
                self.ui2.label_h.setText("Hip Hip Hoorey!:)")

            if l in self.word:
                for j in self.word:
                    if l == j:
                        self.show_word[self.word.index(j, idx)] = l
                    idx += 1
            else:
                self.heart -= 1
            self.ui2.label.setText(str("".join(self.show_word)))

app = QApplication([])
window = Hangman()
app.exec()