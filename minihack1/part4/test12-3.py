import re

name = input("Enter your username: ")
while True:
    email = input("Enter an email: ")
    PW = input("Enter a password: ")
    Pw = input("Re-enter your password: ")
    alphabets = digits = 0
    for i in range(len(PW)):
        if(PW[i].isalpha()):
            alphabets = alphabets +1
        elif(PW[i].isdigit()):
            digits = digits +1
    wordcount = digits + alphabets
    pattern = "^[A-Za-z0-9]+\@[A-Za-z0-9]+\.[A-Za-z0-9]+$"
    emailMatch = re.match(pattern, email)
    if PW == Pw and wordcount >= 8 and digits >= 1 and emailMatch:
        print("Welcome",name)
        break
    else:
        print("Your password is'nt valid. Please try again")   
