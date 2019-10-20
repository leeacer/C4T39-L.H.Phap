import random

empty_room = "-"
player = "P"
Escape = "E"
Key = "K"
up = "w"
down = "s"
left = "a"
right = "d"

line_1 = ["-", "-", "-", "-"]
line_2 = ["-", "-", "-", "-"]
line_3 = ["-", "-", "-", "-"]
line_4 = ["-", "-", "-", "-"]

l = list(range(1,17))

place = random.choice(l)
l.remove(place)
item = random.choice(l)
l.remove(item)
out = random.choice(l)
items = 0

complete = False

if place == 1:
    line_1[0] = "P"
elif place == 2:
    line_1[1] = "P"
elif place == 3:
    line_1[2] = "P"
elif place == 4:
    line_1[3] = "P"
elif place == 5:
    line_2[0] = "P"
elif place == 6:
    line_2[1] = "P"
elif place == 7:
    line_2[2] = "P"
elif place == 8:
    line_2[3] = "P"
elif place == 9:
    line_3[0] = "P"
elif place == 10:
    line_3[1] = "P"
elif place == 11:
    line_3[2] = "P"
elif place == 12:
    line_3[3] = "P"
elif place == 13:
    line_4[0] = "P"
elif place == 14:
    line_4[1] = "P"
elif place == 15:
    line_4[2] = "P"
elif place == 16:
    line_4[3] = "P"

if item == 1:
    line_1[0] = "K"
elif item == 2:
    line_1[1] = "K"
elif item == 3:
    line_1[2] = "K"
elif item == 4:
    line_1[3] = "K"
elif item == 5:
    line_2[0] = "K"
elif item == 6:
    line_2[1] = "K"
elif item == 7:
    line_2[2] = "K"
elif item == 8:
    line_2[3] = "K"
elif item == 9:
    line_3[0] = "K"
elif item == 10:
    line_3[1] = "K"
elif item == 11:
    line_3[2] = "K"
elif item == 12:
    line_3[3] = "K"
elif item == 13:
    line_4[0] = "K"
elif item == 14:
    line_4[1] = "K"
elif item == 15:
    line_4[2] = "K"
elif item == 16:
    line_4[3] = "K"

if out == 1:
    line_1[0] = "E"
elif out == 2:
    line_1[1] = "E"
elif out == 3:
    line_1[2] = "E"
elif out == 4:
    line_1[3] = "E"
elif out == 5:
    line_2[0] = "E"
elif out == 6:
    line_2[1] = "E"
elif out == 7:
    line_2[2] = "E"
elif out == 8:
    line_2[3] = "E"
elif out == 9:
    line_3[0] = "E"
elif out == 10:
    line_3[1] = "E"
elif out == 11:
    line_3[2] = "E"
elif out == 12:
    line_3[3] = "E"
elif out == 13:
    line_4[0] = "E"
elif out == 14:
    line_4[1] = "E"
elif out == 15:
    line_4[2] = "E"
elif out == 16:
    line_4[3] = "E"
        
print(*line_1, sep="    ")
print(*line_2, sep="    ")
print(*line_3, sep="    ")
print(*line_4, sep="    ")

actions = {
    "D" : "left",
    "A" : "right",
    "W" : "up",
    "S" : "down",
    "X" : "exit",
}

while True:
    for k,v in actions.items():
        print(k + ":", v)
    print("What would you like to do?")
    action = input("")

    if action.upper() == "X":
        print("~~~~~~~~Cya later!~~~~~~~~~~")
        break
    
    elif action.upper() == "D":
        if place == 16 or place == 4 or place == 8 or place == 12:
            print("~~~~~~~You can't do that~~~~~~~~")
        elif out == place + 1 and items == 0:
            print("~~~~~~~You can't do that~~~~~~~~")
        else:
            if place == 1:
                line_1[0] = "-"
            elif place == 2:
                line_1[1] = "-"
            elif place == 3:
                line_1[2] = "-"
            elif place == 5:
                line_2[0] = "-"
            elif place == 6:
                line_2[1] = "-"
            elif place == 7:
                line_2[2] = "-"
            elif place == 9:
                line_3[0] = "-"
            elif place == 10:
                line_3[1] = "-"
            elif place == 11:
                line_3[2] = "-"
            elif place == 13:
                line_4[0] = "-"
            elif place == 14:
                line_4[1] = "-"
            elif place == 15:
                line_4[2] = "-"
                
            place = place + 1

            if place == 2:
                line_1[1] = "P"
            elif place == 3:
                line_1[2] = "P"
            elif place == 4:
                line_1[3] = "P"
            elif place == 6:
                line_2[1] = "P"
            elif place == 7:
                line_2[2] = "P"
            elif place == 8:
                line_2[3] = "P"
            elif place == 10:
                line_3[1] = "P"
            elif place == 11:
                line_3[2] = "P"
            elif place == 12:
                line_3[3] = "P"
            elif place == 14:
                line_4[1] = "P"
            elif place == 15:
                line_4[2] = "P"
            elif place == 16:
                line_4[3] = "P"

    elif action.upper() == "A":
        if place == 1 or place == 5 or place == 9 or place == 13:
            print("~~~~~~~You can't do that~~~~~~~~")
        elif out == place - 1 and items == 0:
            print("~~~~~~~You can't do that~~~~~~~~")
        else:
            if place == 2:
                line_1[1] = "-"
            elif place == 3:
                line_1[2] = "-"
            elif place == 4:
                line_1[3] = "-"
            elif place == 6:
                line_2[1] = "-"
            elif place == 7:
                line_2[2] = "-"
            elif place == 8:
                line_2[3] = "-"
            elif place == 10:
                line_3[1] = "-"
            elif place == 11:
                line_3[2] = "-"
            elif place == 12:
                line_3[3] = "-"
            elif place == 14:
                line_4[1] = "-"
            elif place == 15:
                line_4[2] = "-"
            elif place == 16:
                line_4[3] = "-"

            place = place - 1

            if place == 1:
                line_1[0] = "P"
            elif place == 2:
                line_1[1] = "P"
            elif place == 3:
                line_1[2] = "P"
            elif place == 5:
                line_2[0] = "P"
            elif place == 6:
                line_2[1] = "P"
            elif place == 7:
                line_2[2] = "P"
            elif place == 9:
                line_3[0] = "P"
            elif place == 10:
                line_3[1] = "P"
            elif place == 11:
                line_3[2] = "P"
            elif place == 13:
                line_4[0] = "P"
            elif place == 14:
                line_4[1] = "P"
            elif place == 15:
                line_4[2] = "P"

    elif action.upper() == "W":
        if place == 1 or place == 2 or place == 3 or place == 4:
            print("~~~~~~~You can't do that~~~~~~~~")
        elif out == place - 4 and items == 0:
            print("~~~~~~~You can't do that~~~~~~~~")
        else:
            if place == 5:
                line_2[0] = "-"
            elif place == 6:
                line_2[1] = "-"
            elif place == 7:
                line_2[2] = "-"
            elif place == 8:
                line_2[3] = "-"
            elif place == 9:
                line_3[0] = "-"
            elif place == 10:
                line_3[1] = "-"
            elif place == 11:
                line_3[2] = "-"
            elif place == 12:
                line_3[3] = "-"
            elif place == 13:
                line_4[0] = "-"
            elif place == 14:
                line_4[1] = "-"
            elif place == 15:
                line_4[2] = "-"
            elif place == 16:
                line_4[3] = "-"

            place = place - 4

            if place == 1:
                line_1[0] = "P"
            elif place == 2:
                line_1[1] = "P"
            elif place == 3:
                line_1[2] = "P"
            elif place == 4:
                line_1[3] = "P"
            elif place == 5:
                line_2[0] = "P"
            elif place == 6:
                line_2[1] = "P"
            elif place == 7:
                line_2[2] = "P"
            elif place == 8:
                line_2[3] = "P"
            elif place == 9:
                line_3[0] = "P"
            elif place == 10:
                line_3[1] = "P"
            elif place == 11:
                line_3[2] = "P"
            elif place == 12:
                line_3[3] = "P"

    elif action.upper() == "S":
        if place == 13 or place == 14 or place == 15 or place == 16:
            print("~~~~~~~You can't do that~~~~~~~~")
        elif out == place + 4 and items == 0:
            print("~~~~~~~You can't do that~~~~~~~~")
        else:
            if place == 1:
                line_1[0] = "-"
            elif place == 2:
                line_1[1] = "-"
            elif place == 3:
                line_1[2] = "-"
            elif place == 4:
                line_1[3] = "-"
            elif place == 5:
                line_2[0] = "-"
            elif place == 6:
                line_2[1] = "-"
            elif place == 7:
                line_2[2] = "-"
            elif place == 8:
                line_2[3] = "-"
            elif place == 9:
                line_3[0] = "-"
            elif place == 10:
                line_3[1] = "-"
            elif place == 11:
                line_3[2] = "-"
            elif place == 12:
                line_3[3] = "-"

            place = place + 4

            if place == 5:
                line_2[0] = "P"
            elif place == 6:
                line_2[1] = "P"
            elif place == 7:
                line_2[2] = "P"
            elif place == 8:
                line_2[3] = "P"
            elif place == 9:
                line_3[0] = "P"
            elif place == 10:
                line_3[1] = "P"
            elif place == 11:
                line_3[2] = "P"
            elif place == 12:
                line_3[3] = "P"
            elif place == 13:
                line_4[0] = "P"
            elif place == 14:
                line_4[1] = "P"
            elif place == 15:
                line_4[2] = "P"
            elif place == 16:
                line_4[3] = "P"

    if place == item:
        items = items + 1
        print("~~~~~~~~You got a key!~~~~~~~~")

    print(*line_1, sep="    ")
    print(*line_2, sep="    ")
    print(*line_3, sep="    ")
    print(*line_4, sep="    ")

    if items == 1 and place == out:
        print("~~~~~~~~You did it!~~~~~~~~")
        break