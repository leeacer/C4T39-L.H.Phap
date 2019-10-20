import re
while True:
    name = input("Enter your name: ")
    pattern = "^[A-Za-z]+$"
    nameMatch = re.match(pattern, name)
    if nameMatch:
        print("Your name is valid")
        break
    else:
        print("Your name is invalid. Try agin")