string = input("enter your sentence: ")
string = string.split()
string = "".join(string)

a = -1
for i in range(len(string) // 2):
    if string[i] != string[a]:
        print("No Palindrome")
        exit(0)
    else:
        a += -1
print("Yes Palindrome")