name = input("Enter your username: ")
email = input("Enter an email: ")
PW = input("Enter a password: ")
while True:
    Pw = input("Re-enter your password: ")

    if PW == Pw:
        print("Welcome",name)
        break
    else:
        print("Your passwords don't match. Please try again")