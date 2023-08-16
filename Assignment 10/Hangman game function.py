import random
import pyfiglet

Animals_easy = ["cat", "dog", "cow", "pig", "fly", "eik", "fox", "bat", "ant", "bee"]
Animals_medium = ["deer", "crab", "duck", "fish", "goat", "wolf", "tang", "lion", "hare", "frog"]
Animals_difficult = ["dhole", "bison", "fossa", "lemur", "xerus", "prawn", "moose", "liger", "zorse", "sloth"]
Colors_easy = ["red", "blue", "black", "white", "green", "orange", "gold", "gray", "coral", "purple"]
Colors_medium = ["teal", "cyan", "pink", "bice", "puce", "jade", "aero", "fawn", "finn", "erin"]
Colors_difficult = ["azure", "ebony", "beige", "yellow", "coquelicot", "magenta", "fallow", "champagne", "hibiscus", "ginger"]
Musical_instruments_easy = ["harp", "flute", "guitar", "drums", "tuba", "organ", "sitar", "piano", "ukelele", "violin"]
Musical_instruments_medium = ["banjo", "bugle", "bagpipes", "accordion", "bassoon", "keyboard", "maracas", "triangle", "cymbals", "clarinet"]
Musical_instruments_difficult = ["didgeridoo", "mandolin", "harpsichord", "saxophone", "xylophone", "trombone", "harmonica", "mridangam", "	euphonium", "harmonium"]
Sports_easy = ["soccer", "tennis", "golf", "boxing", "skiing", "pool", "rugby", "karate", "archery", "judo"]
Sports_medium = ["basketball", "baseball", "volleyball", "cricket", "bowling", "fencing", "rowing", "handball", "sailing", "hiking"]
Sports_difficult = ["badminton", "snowboarding", "skateboarding", "taekwondo", "gymnastics", "paddleboarding", "equestrian", "snowmobiling", "bobsledding", "orienteering"]
Clothes_easy = ["skirt", "cap", "hat", "vest", "scarf", "dress", "boots", "tie", "socks", "ring"]
Clothes_medium = ["bathrobe", "jumper", "overalls", "mittens", "diaper", "singlet", "cardigan", "sweater", "swimsuit", "blazer"]
Clothes_difficult = ["sunglasses", "pullover", "waistcoat", "earrings", "trenchcoat", "earmuffs", "umbrella", "mortarboard", "longsleevetop", "businessshoes"]


def choose_word():
    while True:
        choose_category = int(input("1_Animals\n2_Colors\n3_Musical_instruments\n4_Sports\n5_Clothes\nenter number of the category you have chosen: "))
        if choose_category == 1:
            Animals_level = int(input("1_easy\n2_medium\n3_difficult\nenter number of the Animals category level:(deafult = 1)\n"))
            if Animals_level == 2:
                word = random.choice(Animals_medium)
            elif Animals_level == 3:
                word = random.choice(Animals_difficult)
            else:
                word = random.choice(Animals_easy)
            break
        elif choose_category == 2:
            Colors_level = int(input("1_easy\n2_medium\n3_difficult\nenter number of the Colors category level:(deafult = 1)\n"))
            if Colors_level == 2:
                word = random.choice(Colors_medium)
            elif Colors_level == 3:
                word = random.choice(Colors_difficult)
            else:
                word = random.choice(Colors_easy)
            break

        elif choose_category == 3:
            Musical_instruments_level = int(input("1_easy\n2_medium\n3_difficult\nenter number of the Musical_instruments category level:(deafult = 1)\n"))
            if Musical_instruments_level == 2:
                word = random.choice(Musical_instruments_medium)
            elif Musical_instruments_level == 3:
                word = random.choice(Musical_instruments_difficult)
            else:
                word = random.choice(Musical_instruments_easy)
            break

        elif choose_category == 4:
            Sports_level = int(input("1_easy\n2_medium\n3_difficult\nenter number of the Sports category level:(deafult = 1)\n"))
            if Sports_level == 2:
                word = random.choice(Sports_medium)
            elif Sports_level == 3:
                word = random.choice(Sports_difficult)
            else:
                word = random.choice(Sports_easy)
            break

        elif choose_category == 5:
            Clothes_level = int(input("1_easy\n2_medium\n3_difficult\nenter number of the Clothes category level:(deafult = 1)\n"))
            if Clothes_level == 2:
                word = random.choice(Clothes_medium)
            elif Clothes_level == 3:
                word = random.choice(Clothes_difficult)
            else:
                word = random.choice(Clothes_easy)
            break
        else:
            print("your number of the category is not in range(1, 5)(deafult = Animals , level = easy)")
            try_again = input("do you want to chosen agian?(y, n)\t")
            if try_again != "y":
                word = random.choice(Animals_easy)
                break
    return word

def check_game(word):
    hearts = (len(word) * 1.5) // 1
    show_word = []
    number_of_true_char = 0
    for i in range(len(word)):
        show_word.append("_")
    while True:
        # print word hearts
        print("".join(show_word))
        print("❤️" * int(hearts))
        if hearts == 0:
            print("Game over🎮❌")
            break
        # check_end_game
        if not("_" in show_word):
            print("Hip Hip Hoorey!🎆")
            break
        user_char = input("enter your character : ").lower()
        # new_char
        idx = 0
        if user_char in word:
            for j in word:
                if user_char == j:
                    show_word[word.index(j, idx)] = user_char
                idx += 1  
        else:
            print("your character is not exist")
            hearts -= 1

            
while True:
    result= pyfiglet.figlet_format("Hangman-game-", font="slant")

    print(result) 
    word = choose_word()
    check_game(word)
    try_again = input("do you want to try agian?(y, n)🤔\t")
    if try_again != "y":
        break