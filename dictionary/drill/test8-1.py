quiz = {
    "1" : "One leg",
    "2" : "Two legs",
    "3" : "Four legs",
    "4" : "Eight legs",
}
while True:
    print("How many legs does an octopus have?")
    for k,v in quiz.items():
        print(k + ".", v)
    answer = input("Your answer:")
    if answer == list(quiz.keys())[3]:
        print("yay")
        break
    else:
        print("nay")