password = '1378'
password_list = [password[0],password[1],password[2],password[3]]
c = 0

while c < 3:
    i_password = input("enter your password :")
    
    if len(i_password) == 4:
        if password == i_password:
            print("Welcome to account")
            exit(0)
        
        elif str([i_password[0],i_password[1],i_password[2],i_password[3]]) == str(password_list[::-1]):
            print("Calling the police!!!")
            exit(0)
        
        else:
            print("The password is wrong")
            c += 1
    
    else:
        print("try again!!")

print("Your account has been locked!!!!")