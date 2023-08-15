username = "admin"
password = 1378
username2 = "admins"
password2 = 8731
user_name_input = input("enter username:")
password_input = int(input("enter password:"))

if user_name_input == username and password_input == password or user_name_input == username2 and password_input == password2 :
    print("welcome to app")
elif user_name_input == username or password_input == password and user_name_input == username2 or password_input == password2:
    print("youre username or password is not defined")
    user_name_input = input("enter username:")
    password_input = int(input("enter password:"))
    if user_name_input == username and password_input == password or user_name_input == username2 and password_input == password2 :
        print("welcome to app")
    else:
        print("youre username or password is not defined")
else:
    print("youre username or password is not defined")