while True:
    string = input("Enter a password: ")
    alphabets = digits = 0

    for i in range(len(string)):
        if(string[i].isalpha()):
            alphabets = alphabets +1
        elif(string[i].isdigit()):
            digits = digits +1

    wordcount = alphabets + digits

    if digits >= 1 or wordcount >= 8:
        print("Your password is valid")
        break
    else:
        print("Your password is invalid. Try agin")