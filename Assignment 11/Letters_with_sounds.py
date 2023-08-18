def sounds(string):
    for s in string:
        if   ord(s) ==  97 or ord(s) == 65: 
            string = string.replace(s, "!")
        elif ord(s) == 101 or ord(s) == 69: 
            string = string.replace(s, "!")
        elif ord(s) == 105 or ord(s) == 73: 
            string = string.replace(s, "!")
        elif ord(s) == 111 or ord(s) == 79: 
            string = string.replace(s, "!")
        elif ord(s) == 117 or ord(s) == 85: 
            string = string.replace(s, "!")
    return string

string = input("youre enter  string:")
print(sounds(string))