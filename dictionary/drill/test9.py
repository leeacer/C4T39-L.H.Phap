quiz1 = {
    "1" : "sans",
    "2" : "minecraft steve",
    "3" : "shrek",
    "4" : "rachet"
}

quiz2 = {
    "1" : "charizard",
    "2" : "lugia",
    "3" : "rayquaza",
    "4" : "gyrados"
}

quiz3 = {
    "1" : "nintendo",
    "2" : "bandai",
    "3" : "sega",
    "4" : "atlus"
}

quiz4 = {
    "1" : "arsene",
    "2" : "izanagi",
    "3" : "captain kid",
    "4" : "dancing disco frog"
}

correct = 0
wrong = 0

print("Which of these characters are in Smash Bros?")
for k,v in quiz1.items():
    print(k + ".", v)
answer = input("Your answer:")
if answer == list(quiz1.keys())[0]:
    correct= correct + 1
else:
    wrong= wrong + 1

print("Which of these pokemon is dragon typed?")
for k,v in quiz2.items():
    print(k + ".", v)
answer = input("Your answer:")
if answer == list(quiz2.keys())[2]:
    correct= correct + 1
else:
    wrong= wrong + 1

print("Which of these companies own Persona 5?")
for k,v in quiz3.items():
    print(k + ".", v)
answer = input("Your answer:")
if answer == list(quiz3.keys())[3]:
    correct= correct + 1
else:
    wrong= wrong + 1

print("Which of these personas is the main one that Yu Narukami uses?")
for k,v in quiz4.items():
    print(k + ".", v)
answer = input("Your answer:")
if answer == list(quiz4.keys())[1]:
    correct= correct + 1
else:
    wrong= wrong + 1

print("Number of questions u got right:", correct)
print("Number of quesitons u got wrong:", wrong)

percent = correct / 4 * 100
print(percent, "% of questions were right")