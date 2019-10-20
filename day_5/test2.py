import re
while True:
    PW = input("Enter your password: ")
    pattern = "^[A-Za-z]+[0-9]+$"
    PWMatch = re.match(pattern, PW)
    if PWMatch:
        print("Your password is valid")
        break
    else:
        print("Your password is invalid. Try agin")