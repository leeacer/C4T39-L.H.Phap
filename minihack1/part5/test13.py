import random
score = 0
while True:
    number1 = random.randint(1 ,20)
    number2 = random.randint(1 ,20)
    maybe = random.randint(1 ,4)
    number3 = number1 + number2
    number4 = number1 - number2
    number5 = random.randint(-20 ,20)
    some = 0
    addition = number1 + number2
    minus = number1 - number2
    if maybe == 1:
        some = number3
    elif maybe == 2:
        some = number4
    elif maybe == 3:
        some = number5
    if maybe == 1:
        print(number1,"+",number2,"=",some)
    elif maybe == 2:
        print(number1,"-",number2,"=",some)
    else:
        print(number1,"+",number2,"=",some)
    answer = input("YES     OR      NO:        ")
    if addition == some or minus == some and answer == "yes":
        print("That's correct")
        score = score + 1
        print("Score:",score)
    elif addition != some and answer == "no":
        print("That's correct")
        score = score + 1
        print("Score:",score)
    else:
        print("You lose!")
        print("Score",score)
        break