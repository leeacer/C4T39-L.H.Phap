import random

level = 1
actions = {
    "D" : "left",
    "A" : "right",
    "W" : "up",
    "S" : "down",
    "X" : "exit",
}
options = {
    "F" : "fight",
    "R" : "run",
}
fight = {
    "1" : "Attack",
    "2" : "Block",
    "3" : "Run",
    "4" : "Item",
}
pocket = {}
health = {
    10 : "████​███████████​█████",
    9 : "████​███████████​███  ",
    8 : "████​███████████​█    ",
    7 : "████​██████████      ",
    6 : "████​████████        ",
    5 : "████​██████          ",
    4 : "████​████            ",
    3 : "████​██              ",
    2 : "████​                ",
    1 : "██                  ",
    0 : "                    ",
}
name = input("Enter your name: ")
attack_damage = 1
monster_attack = 0

if level == 1: # BEGINNER
    line_1 = ["-", "-", "-", "-"]
    line_15 = [" ", " ", " ", " "]
    line_2 = ["-", "-", "-", "-"]
    line_25 = [" ", " ", " ", " "]
    line_3 = ["-", "-", "-", "-"]
    line_35 = [" ", " ", " ", " "]
    line_4 = ["-", "-", "-", "-"]

    l1 = list(range(1,17))

    place1 = random.choice(l1)
    l1.remove(place1)
    item1 = random.choice(l1)
    l1.remove(item1)
    out1 = random.choice(l1)
    items1 = 0

    if place1 == 1:
        line_1[0] = "P"
    elif place1 == 2:
        line_1[1] = "P"
    elif place1 == 3:
        line_1[2] = "P"
    elif place1 == 4:
        line_1[3] = "P"
    elif place1 == 5:
        line_2[0] = "P"
    elif place1 == 6:
        line_2[1] = "P"
    elif place1 == 7:
        line_2[2] = "P"
    elif place1 == 8:
        line_2[3] = "P"
    elif place1 == 9:
        line_3[0] = "P"
    elif place1 == 10:
        line_3[1] = "P"
    elif place1 == 11:
        line_3[2] = "P"
    elif place1 == 12:
        line_3[3] = "P"
    elif place1 == 13:
        line_4[0] = "P"
    elif place1 == 14:
        line_4[1] = "P"
    elif place1 == 15:
        line_4[2] = "P"
    elif place1 == 16:
        line_4[3] = "P"

    if item1 == 1:
        line_1[0] = "K"
    elif item1 == 2:
        line_1[1] = "K"
    elif item1 == 3:
        line_1[2] = "K"
    elif item1 == 4:
        line_1[3] = "K"
    elif item1 == 5:
        line_2[0] = "K"
    elif item1 == 6:
        line_2[1] = "K"
    elif item1 == 7:
        line_2[2] = "K"
    elif item1 == 8:
        line_2[3] = "K"
    elif item1 == 9:
        line_3[0] = "K"
    elif item1 == 10:
        line_3[1] = "K"
    elif item1 == 11:
        line_3[2] = "K"
    elif item1 == 12:
        line_3[3] = "K"
    elif item1 == 13:
        line_4[0] = "K"
    elif item1 == 14:
        line_4[1] = "K"
    elif item1 == 15:
        line_4[2] = "K"
    elif item1 == 16:
        line_4[3] = "K"

    if out1 == 1:
        line_1[0] = "E"
    elif out1 == 2:
        line_1[1] = "E"
    elif out1 == 3:
        line_1[2] = "E"
    elif out1 == 4:
        line_1[3] = "E"
    elif out1 == 5:
        line_2[0] = "E"
    elif out1 == 6:
        line_2[1] = "E"
    elif out1 == 7:
        line_2[2] = "E"
    elif out1 == 8:
        line_2[3] = "E"
    elif out1 == 9:
        line_3[0] = "E"
    elif out1 == 10:
        line_3[1] = "E"
    elif out1 == 11:
        line_3[2] = "E"
    elif out1 == 12:
        line_3[3] = "E"
    elif out1 == 13:
        line_4[0] = "E"
    elif out1 == 14:
        line_4[1] = "E"
    elif out1 == 15:
        line_4[2] = "E"
    elif out1 == 16:
        line_4[3] = "E"


    print("~~~~~~~~| LEVEL", level, "|~~~~~~~~")

    print(*line_1, sep="       ")
    print(*line_15, sep="       ")
    print(*line_2, sep="       ")
    print(*line_25, sep="       ")
    print(*line_3, sep="       ")
    print(*line_35, sep="       ")
    print(*line_4, sep="       ")

    while True: #MOVEMENT CONTROLS FOR LVL 1
            for k,v in actions.items():
                print(k + ":", v)
            print("What would you like to do?")
            action1 = input("")

            if action1.upper() == "X":
                print("~~~~~~~~Cya later!~~~~~~~~~~")
                break
            
            elif action1.upper() == "D":
                if place1 == 16 or place1 == 4 or place1 == 8 or place1 == 12:
                    print("~~~~~~~You can't do that~~~~~~~~")
                elif out1 == place1 + 1 and items1 == 0:
                    print("~~~~~~~You can't do that~~~~~~~~")
                else:
                    if place1 == 1:
                        line_1[0] = "-"
                    elif place1 == 2:
                        line_1[1] = "-"
                    elif place1 == 3:
                        line_1[2] = "-"
                    elif place1 == 5:
                        line_2[0] = "-"
                    elif place1 == 6:
                        line_2[1] = "-"
                    elif place1 == 7:
                        line_2[2] = "-"
                    elif place1 == 9:
                        line_3[0] = "-"
                    elif place1 == 10:
                        line_3[1] = "-"
                    elif place1 == 11:
                        line_3[2] = "-"
                    elif place1 == 13:
                        line_4[0] = "-"
                    elif place1 == 14:
                        line_4[1] = "-"
                    elif place1 == 15:
                        line_4[2] = "-"
                        
                    place1 = place1 + 1

                    if place1 == 2:
                        line_1[1] = "P"
                    elif place1 == 3:
                        line_1[2] = "P"
                    elif place1 == 4:
                        line_1[3] = "P"
                    elif place1 == 6:
                        line_2[1] = "P"
                    elif place1 == 7:
                        line_2[2] = "P"
                    elif place1 == 8:
                        line_2[3] = "P"
                    elif place1 == 10:
                        line_3[1] = "P"
                    elif place1 == 11:
                        line_3[2] = "P"
                    elif place1 == 12:
                        line_3[3] = "P"
                    elif place1 == 14:
                        line_4[1] = "P"
                    elif place1 == 15:
                        line_4[2] = "P"
                    elif place1 == 16:
                        line_4[3] = "P"

            elif action1.upper() == "A":
                if place1 == 1 or place1 == 5 or place1 == 9 or place1 == 13:
                    print("~~~~~~~You can't do that~~~~~~~~")
                elif out1 == place1 - 1 and items1 == 0:
                    print("~~~~~~~You can't do that~~~~~~~~")
                else:
                    if place1 == 2:
                        line_1[1] = "-"
                    elif place1 == 3:
                        line_1[2] = "-"
                    elif place1 == 4:
                        line_1[3] = "-"
                    elif place1 == 6:
                        line_2[1] = "-"
                    elif place1 == 7:
                        line_2[2] = "-"
                    elif place1 == 8:
                        line_2[3] = "-"
                    elif place1 == 10:
                        line_3[1] = "-"
                    elif place1 == 11:
                        line_3[2] = "-"
                    elif place1 == 12:
                        line_3[3] = "-"
                    elif place1 == 14:
                        line_4[1] = "-"
                    elif place1 == 15:
                        line_4[2] = "-"
                    elif place1 == 16:
                        line_4[3] = "-"

                    place1 = place1 - 1

                    if place1 == 1:
                        line_1[0] = "P"
                    elif place1 == 2:
                        line_1[1] = "P"
                    elif place1 == 3:
                        line_1[2] = "P"
                    elif place1 == 5:
                        line_2[0] = "P"
                    elif place1 == 6:
                        line_2[1] = "P"
                    elif place1 == 7:
                        line_2[2] = "P"
                    elif place1 == 9:
                        line_3[0] = "P"
                    elif place1 == 10:
                        line_3[1] = "P"
                    elif place1 == 11:
                        line_3[2] = "P"
                    elif place1 == 13:
                        line_4[0] = "P"
                    elif place1 == 14:
                        line_4[1] = "P"
                    elif place1 == 15:
                        line_4[2] = "P"

            elif action1.upper() == "W":
                if place1 == 1 or place1 == 2 or place1 == 3 or place1 == 4:
                    print("~~~~~~~You can't do that~~~~~~~~")
                elif out1 == place1 - 4 and items1 == 0:
                    print("~~~~~~~You can't do that~~~~~~~~")
                else:
                    if place1 == 5:
                        line_2[0] = "-"
                    elif place1 == 6:
                        line_2[1] = "-"
                    elif place1 == 7:
                        line_2[2] = "-"
                    elif place1 == 8:
                        line_2[3] = "-"
                    elif place1 == 9:
                        line_3[0] = "-"
                    elif place1 == 10:
                        line_3[1] = "-"
                    elif place1 == 11:
                        line_3[2] = "-"
                    elif place1 == 12:
                        line_3[3] = "-"
                    elif place1 == 13:
                        line_4[0] = "-"
                    elif place1 == 14:
                        line_4[1] = "-"
                    elif place1 == 15:
                        line_4[2] = "-"
                    elif place1 == 16:
                        line_4[3] = "-"

                    place1 = place1 - 4

                    if place1 == 1:
                        line_1[0] = "P"
                    elif place1 == 2:
                        line_1[1] = "P"
                    elif place1 == 3:
                        line_1[2] = "P"
                    elif place1 == 4:
                        line_1[3] = "P"
                    elif place1 == 5:
                        line_2[0] = "P"
                    elif place1 == 6:
                        line_2[1] = "P"
                    elif place1 == 7:
                        line_2[2] = "P"
                    elif place1 == 8:
                        line_2[3] = "P"
                    elif place1 == 9:
                        line_3[0] = "P"
                    elif place1 == 10:
                        line_3[1] = "P"
                    elif place1 == 11:
                        line_3[2] = "P"
                    elif place1 == 12:
                        line_3[3] = "P"

            elif action1.upper() == "S":
                if place1 == 13 or place1 == 14 or place1 == 15 or place1 == 16:
                    print("~~~~~~~You can't do that~~~~~~~~")
                elif out1 == place1 + 4 and items1 == 0:
                    print("~~~~~~~You can't do that~~~~~~~~")
                else:
                    if place1 == 1:
                        line_1[0] = "-"
                    elif place1 == 2:
                        line_1[1] = "-"
                    elif place1 == 3:
                        line_1[2] = "-"
                    elif place1 == 4:
                        line_1[3] = "-"
                    elif place1 == 5:
                        line_2[0] = "-"
                    elif place1 == 6:
                        line_2[1] = "-"
                    elif place1 == 7:
                        line_2[2] = "-"
                    elif place1 == 8:
                        line_2[3] = "-"
                    elif place1 == 9:
                        line_3[0] = "-"
                    elif place1 == 10:
                        line_3[1] = "-"
                    elif place1 == 11:
                        line_3[2] = "-"
                    elif place1 == 12:
                        line_3[3] = "-"

                    place1 = place1 + 4

                    if place1 == 5:
                        line_2[0] = "P"
                    elif place1 == 6:
                        line_2[1] = "P"
                    elif place1 == 7:
                        line_2[2] = "P"
                    elif place1 == 8:
                        line_2[3] = "P"
                    elif place1 == 9:
                        line_3[0] = "P"
                    elif place1 == 10:
                        line_3[1] = "P"
                    elif place1 == 11:
                        line_3[2] = "P"
                    elif place1 == 12:
                        line_3[3] = "P"
                    elif place1 == 13:
                        line_4[0] = "P"
                    elif place1 == 14:
                        line_4[1] = "P"
                    elif place1 == 15:
                        line_4[2] = "P"
                    elif place1 == 16:
                        line_4[3] = "P"

            if level == 1:
                print("~~~~~~~~| LEVEL", level, "|~~~~~~~~")
                print(*line_1, sep="       ")
                print(*line_15, sep="       ")
                print(*line_2, sep="       ")
                print(*line_25, sep="       ")
                print(*line_3, sep="       ")
                print(*line_35, sep="       ")
                print(*line_4, sep="       ")

            if place1 == item1:
                if items1 == 0:
                    items1 = items1 + 1
                    print("~~~~~~~~You got a key!~~~~~~~~")

            if items1 == 1 and place1 == out1:
                print("~~~~~~~~Level 1 completed!~~~~~~~~")
                level = level + 1
                break

if level == 2: # HAS WALLS
    floor_1 = ["-", " ", "-", " ", "-", " ", "-"]
    floor_1_2 = [" ", " ", " ", " ", " ", " ", " "]
    floor_2 = ["-", " ", "-", " ", "-", " ", "-"]
    floor_2_2 = [" ", " ", " ", " ", " ", " ", " "]
    floor_3 = ["-", " ", "-", " ", "-", " ", "-"]
    floor_3_2 = [" ", " ", " ", " ", " ", " ", " "]
    floor_4 = ["-", " ", "-", " ", "-", " ", "-"]

    l2 = list(range(1,50))
    l2.remove(8)
    l2.remove(9)
    l2.remove(10)
    l2.remove(11)
    l2.remove(12)
    l2.remove(13)
    l2.remove(14)
    l2.remove(22)
    l2.remove(23)
    l2.remove(24)
    l2.remove(25)
    l2.remove(26)
    l2.remove(27)
    l2.remove(28)
    l2.remove(36)
    l2.remove(37)
    l2.remove(38)
    l2.remove(39)
    l2.remove(40)
    l2.remove(41)
    l2.remove(42)

    walls2 = []
    places2 = []

    for num1 in l2: #GENERATOR FOR WALLS
        if num1 in range(1, 8): 
            if num1 % 2 == 0: 
                walls2.append(num1)
        if num1 in range(15, 22):
            if num1 % 2 == 0:
                walls2.append(num1)
        if num1 in range(29, 36):
            if num1 % 2 == 0: 
                walls2.append(num1)
        if num1 in range(43, 50):
            if num1 % 2 == 0: 
                walls2.append(num1)

    walls2.append(8)
    walls2.append(9)
    walls2.append(10)
    walls2.append(11)
    walls2.append(12)
    walls2.append(13)
    walls2.append(14)
    walls2.append(22)
    walls2.append(23)
    walls2.append(24)
    walls2.append(25)
    walls2.append(26)
    walls2.append(27)
    walls2.append(28)
    walls2.append(36)
    walls2.append(37)
    walls2.append(38)
    walls2.append(39)
    walls2.append(40)
    walls2.append(41)
    walls2.append(42)

    for num2 in l2: #GENERATOR FOR OTHERS
        if num2 in range(1, 8): 
            if num2 % 2 != 0: 
                places2.append(num2)
        if num2 in range(15, 22):
            if num2 % 2 != 0:
                places2.append(num2)
        if num2 in range(29, 36):
            if num2 % 2 != 0: 
                places2.append(num2)
        if num2 in range(43, 50):
            if num2 % 2 != 0: 
                places2.append(num2)

    wall21 = random.choice(walls2)
    walls2.remove(wall21)
    wall22 = random.choice(walls2)
    walls2.remove(wall22)
    wall23 = random.choice(walls2)
    walls2.remove(wall23)
    wall24 = random.choice(walls2)
    walls2.remove(wall24)

    place2 = random.choice(places2)
    places2.remove(place2)
    item21 = random.choice(places2)
    places2.remove(item21)
    item22 = random.choice(places2)
    places2.remove(item22)
    out2 = random.choice(places2)
    items2 = 0
        
    if wall21 == 2:
        floor_1[1] = "W"
    elif wall21 == 4:
        floor_1[3] = "W"
    elif wall21 == 6:
        floor_1[5] = "W"
    elif wall21 == 8:
        floor_1_2[0] = "W"
    elif wall21 == 10:
        floor_1_2[2] = "W"
    elif wall21 == 12:
        floor_1_2[4] = "W"
    elif wall21 == 14:
        floor_1_2[6] = "W"
    elif wall21 == 16:
        floor_2[1] = "W"
    elif wall21 == 18:
        floor_2[3] = "W"
    elif wall21 == 20:
        floor_2[5] = "W"
    elif wall21 == 22:
        floor_2_2[0] = "W"
    elif wall21 == 24:
        floor_2_2[2] = "W"
    elif wall21 == 26:
        floor_2_2[4] = "W"
    elif wall21 == 28:
        floor_2_2[6] = "W"
    elif wall21 == 30:
        floor_3[1] = "W"
    elif wall21 == 32:
        floor_3[3] = "W"
    elif wall21 == 34:
        floor_3[5] = "W"
    elif wall21 == 36:
        floor_3_2[0] = "W"
    elif wall21 == 38:
        floor_3_2[2] = "W"
    elif wall21 == 40:
        floor_3_2[4] = "W"
    elif wall21 == 42:
        floor_3_2[6] = "W"
    elif wall21 == 44:
        floor_4[1] = "W"
    elif wall21 == 46:
        floor_4[3] = "W"
    elif wall21 == 48:
        floor_4[5] = "W"

    if wall22 == 2:
        floor_1[1] = "W"
    elif wall22 == 4:
        floor_1[3] = "W"
    elif wall22 == 6:
        floor_1[5] = "W"
    elif wall22 == 8:
        floor_1_2[0] = "W"
    elif wall22 == 10:
        floor_1_2[2] = "W"
    elif wall22 == 12:
        floor_1_2[4] = "W"
    elif wall22 == 14:
        floor_1_2[6] = "W"
    elif wall22 == 16:
        floor_2[1] = "W"
    elif wall22 == 18:
        floor_2[3] = "W"
    elif wall22 == 20:
        floor_2[5] = "W"
    elif wall22 == 22:
        floor_2_2[0] = "W"
    elif wall22 == 24:
        floor_2_2[2] = "W"
    elif wall22 == 26:
        floor_2_2[4] = "W"
    elif wall22 == 28:
        floor_2_2[6] = "W"
    elif wall22 == 30:
        floor_3[1] = "W"
    elif wall22 == 32:
        floor_3[3] = "W"
    elif wall22 == 34:
        floor_3[5] = "W"
    elif wall22 == 36:
        floor_3_2[0] = "W"
    elif wall22 == 38:
        floor_3_2[2] = "W"
    elif wall22 == 40:
        floor_3_2[4] = "W"
    elif wall22 == 42:
        floor_3_2[6] = "W"
    elif wall22 == 44:
        floor_4[1] = "W"
    elif wall22 == 46:
        floor_4[3] = "W"
    elif wall22 == 48:
        floor_4[5] = "W"

    if wall23 == 2:
        floor_1[1] = "W"
    elif wall23 == 4:
        floor_1[3] = "W"
    elif wall23 == 6:
        floor_1[5] = "W"
    elif wall23 == 8:
        floor_1_2[0] = "W"
    elif wall23 == 10:
        floor_1_2[2] = "W"
    elif wall23 == 12:
        floor_1_2[4] = "W"
    elif wall23 == 14:
        floor_1_2[6] = "W"
    elif wall23 == 16:
        floor_2[1] = "W"
    elif wall23 == 18:
        floor_2[3] = "W"
    elif wall23 == 20:
        floor_2[5] = "W"
    elif wall23 == 22:
        floor_2_2[0] = "W"
    elif wall23 == 24:
        floor_2_2[2] = "W"
    elif wall23 == 26:
        floor_2_2[4] = "W"
    elif wall23 == 28:
        floor_2_2[6] = "W"
    elif wall23 == 30:
        floor_3[1] = "W"
    elif wall23 == 32:
        floor_3[3] = "W"
    elif wall23 == 34:
        floor_3[5] = "W"
    elif wall23 == 36:
        floor_3_2[0] = "W"
    elif wall23 == 38:
        floor_3_2[2] = "W"
    elif wall23 == 40:
        floor_3_2[4] = "W"
    elif wall23 == 42:
        floor_3_2[6] = "W"
    elif wall23 == 44:
        floor_4[1] = "W"
    elif wall23 == 46:
        floor_4[3] = "W"
    elif wall23 == 48:
        floor_4[5] = "W"

    if wall24 == 2:
        floor_1[1] = "W"
    elif wall24 == 4:
        floor_1[3] = "W"
    elif wall24 == 6:
        floor_1[5] = "W"
    elif wall24 == 8:
        floor_1_2[0] = "W"
    elif wall24 == 10:
        floor_1_2[2] = "W"
    elif wall24 == 12:
        floor_1_2[4] = "W"
    elif wall24 == 14:
        floor_1_2[6] = "W"
    elif wall24 == 16:
        floor_2[1] = "W"
    elif wall24 == 18:
        floor_2[3] = "W"
    elif wall24 == 20:
        floor_2[5] = "W"
    elif wall24 == 22:
        floor_2_2[0] = "W"
    elif wall24 == 24:
        floor_2_2[2] = "W"
    elif wall24 == 26:
        floor_2_2[4] = "W"
    elif wall24 == 28:
        floor_2_2[6] = "W"
    elif wall24 == 30:
        floor_3[1] = "W"
    elif wall24 == 32:
        floor_3[3] = "W"
    elif wall24 == 34:
        floor_3[5] = "W"
    elif wall24 == 36:
        floor_3_2[0] = "W"
    elif wall24 == 38:
        floor_3_2[2] = "W"
    elif wall24 == 40:
        floor_3_2[4] = "W"
    elif wall24 == 42:
        floor_3_2[6] = "W"
    elif wall24 == 44:
        floor_4[1] = "W"
    elif wall24 == 46:
        floor_4[3] = "W"
    elif wall24 == 48:
        floor_4[5] = "W"

    if place2 == 1:
        floor_1[0] = "P"
    elif place2 == 3:
        floor_1[2] = "P"
    elif place2 == 5:
        floor_1[4] = "P"
    elif place2 == 7:
        floor_1[6] = "P"
    elif place2 == 15:
        floor_2[0] = "P"
    elif place2 == 17:
        floor_2[2] = "P"
    elif place2 == 19:
        floor_2[4] = "P"
    elif place2 == 21:
        floor_2[6] = "P"
    elif place2 == 29:
        floor_3[0] = "P"
    elif place2 == 31:
        floor_3[2] = "P"
    elif place2 == 33:
        floor_3[4] = "P"
    elif place2 == 35:
        floor_3[6] = "P"
    elif place2 == 43:
        floor_4[0] = "P"
    elif place2 == 45:
        floor_4[2] = "P"
    elif place2 == 47:
        floor_4[4] = "P"
    elif place2 == 49:
        floor_4[6] = "P"

    if item21 == 1:
        floor_1[0] = "K"
    elif item21 == 3:
        floor_1[2] = "K"
    elif item21 == 5:
        floor_1[4] = "K"
    elif item21 == 7:
        floor_1[6] = "K"
    elif item21 == 15:
        floor_2[0] = "K"
    elif item21 == 17:
        floor_2[2] = "K"
    elif item21 == 19:
        floor_2[4] = "K"
    elif item21 == 21:
        floor_2[6] = "K"
    elif item21 == 29:
        floor_3[0] = "K"
    elif item21 == 31:
        floor_3[2] = "K"
    elif item21 == 33:
        floor_3[4] = "K"
    elif item21 == 35:
        floor_3[6] = "K"
    elif item21 == 43:
        floor_4[0] = "K"
    elif item21 == 45:
        floor_4[2] = "K"
    elif item21 == 47:
        floor_4[4] = "K"
    elif item21 == 49:
        floor_4[6] = "K"

    if item22 == 1:
        floor_1[0] = "K"
    elif item22 == 3:
        floor_1[2] = "K"
    elif item22 == 5:
        floor_1[4] = "K"
    elif item22 == 7:
        floor_1[6] = "K"
    elif item22 == 15:
        floor_2[0] = "K"
    elif item22 == 17:
        floor_2[2] = "K"
    elif item22 == 19:
        floor_2[4] = "K"
    elif item22 == 21:
        floor_2[6] = "K"
    elif item22 == 29:
        floor_3[0] = "K"
    elif item22 == 31:
        floor_3[2] = "K"
    elif item22 == 33:
        floor_3[4] = "K"
    elif item22 == 35:
        floor_3[6] = "K"
    elif item22 == 43:
        floor_4[0] = "K"
    elif item22 == 45:
        floor_4[2] = "K"
    elif item22 == 47:
        floor_4[4] = "K"
    elif item22 == 49:
        floor_4[6] = "K"

    if out2 == 1:
        floor_1[0] = "E"
    elif out2 == 3:
        floor_1[2] = "E"
    elif out2 == 5:
        floor_1[4] = "E"
    elif out2 == 7:
        floor_1[6] = "E"
    elif out2 == 15:
        floor_2[0] = "E"
    elif out2 == 17:
        floor_2[2] = "E"
    elif out2 == 19:
        floor_2[4] = "E"
    elif out2 == 21:
        floor_2[6] = "E"
    elif out2 == 29:
        floor_3[0] = "E"
    elif out2 == 31:
        floor_3[2] = "E"
    elif out2 == 33:
        floor_3[4] = "E"
    elif out2 == 35:
        floor_3[6] = "E"
    elif out2 == 43:
        floor_4[0] = "E"
    elif out2 == 45:
        floor_4[2] = "E"
    elif out2 == 47:
        floor_4[4] = "E"
    elif out2 == 49:
        floor_4[6] = "E"

    print("~~~~~~~~| LEVEL", level, "|~~~~~~~~")

    print(*floor_1, sep="   ")
    print(*floor_1_2, sep="   ")
    print(*floor_2, sep="   ")
    print(*floor_2_2, sep="   ")
    print(*floor_3, sep="   ")
    print(*floor_3_2, sep="   ")
    print(*floor_4, sep="   ")

    while True: #MOVEMENT CONTROLS FOR LVL 4
        for k,v in actions.items():
            print(k + ":", v)
        print("What would you like to do?")
        action2 = input("")

        if action2.upper() == "X":
            print("~~~~~~~~Cya later!~~~~~~~~~~")
            break
            
        elif action2.upper() == "D":
            if place2 == 7 or place2 == 21 or place2 == 35 or place2 == 49:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif out2 == place2 + 2 and items2 < 2:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif wall21 == place2 + 1 or wall22 == place2 + 1 or wall23 == place2 + 1 or wall24 == place2 + 1:
                print("~~~~~~~There's a wall in your way~~~~~~")
            else:
                if place2 == 1:
                    floor_1[0] = "-"
                elif place2 == 3:
                    floor_1[2] = "-"
                elif place2 == 5:
                    floor_1[4] = "-"
                elif place2 == 15:
                    floor_2[0] = "-"
                elif place2 == 17:
                    floor_2[2] = "-"
                elif place2 == 19:
                    floor_2[4] = "-"
                elif place2 == 29:
                    floor_3[0] = "-"
                elif place2 == 31:
                    floor_3[2] = "-"
                elif place2 == 33:
                    floor_3[4] = "-"
                elif place2 == 43:
                    floor_4[0] = "-"
                elif place2 == 45:
                    floor_4[2] = "-"
                elif place2 == 47:
                    floor_4[4] = "-"
                        
                place2 = place2 + 2

                if place2 == 3:
                    floor_1[2] = "P"
                elif place2 == 5:
                    floor_1[4] = "P"
                elif place2 == 7:
                    floor_1[6] = "P"
                elif place2 == 17:
                    floor_2[2] = "P"
                elif place2 == 19:
                    floor_2[4] = "P"
                elif place2 == 21:
                    floor_2[6] = "P"
                elif place2 == 31:
                    floor_3[2] = "P"
                elif place2 == 33:
                    floor_3[4] = "P"
                elif place2 == 35:
                    floor_3[6] = "P"
                elif place2 == 45:
                    floor_4[2] = "P"
                elif place2 == 47:
                    floor_4[4] = "P"
                elif place2 == 49:
                    floor_4[6] = "P"

        elif action2.upper() == "A":
            if place2 == 1 or place2 == 15 or place2 == 29 or place2 == 43:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif out2 == place2 - 2 and items2 < 2:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif wall21 == place2 - 1 or wall22 == place2 - 1 or wall23 == place2 - 1 or wall24 == place2 - 1:
                print("~~~~~~~There's a wall in your way~~~~~~")
            else:
                if place2 == 3:
                    floor_1[2] = "-"
                elif place2 == 5:
                    floor_1[4] = "-"
                elif place2 == 7:
                    floor_1[6] = "-"
                elif place2 == 17:
                    floor_2[2] = "-"
                elif place2 == 19:
                    floor_2[4] = "-"
                elif place2 == 21:
                    floor_2[6] = "-"
                elif place2 == 31:
                    floor_3[2] = "-"
                elif place2 == 33:
                    floor_3[4] = "-"
                elif place2 == 35:
                    floor_3[6] = "-"
                elif place2 == 45:
                    floor_4[2] = "-"
                elif place2 == 47:
                    floor_4[4] = "-"
                elif place2 == 49:
                    floor_4[6] = "-"
                
                place2 = place2 - 2
                
                if place2 == 1:
                    floor_1[0] = "P"
                elif place2 == 3:
                    floor_1[2] = "P"
                elif place2 == 5:
                    floor_1[4] = "P"
                elif place2 == 15:
                    floor_2[0] = "P"
                elif place2 == 17:
                    floor_2[2] = "P"
                elif place2 == 19:
                    floor_2[4] = "P"
                elif place2 == 29:
                    floor_3[0] = "P"
                elif place2 == 31:
                    floor_3[2] = "P"
                elif place2 == 33:
                    floor_3[4] = "P"
                elif place2 == 43:
                    floor_4[0] = "P"
                elif place2 == 45:
                    floor_4[2] = "P"
                elif place2 == 47:
                    floor_4[4] = "P"

        elif action2.upper() == "W":
            if place2 == 1 or place2 == 3 or place2 == 5 or place2 == 7:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif out2 == place2 - 14 and items2 < 2:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif wall21 == place2 - 7 or wall22 == place2 - 7 or wall23 == place2 - 7 or wall24 == place2 - 7:
                print("~~~~~~~There's a wall in your way~~~~~~")
            else:
                if place2 == 15:
                    floor_2[0] = "-"
                elif place2 == 17:
                    floor_2[2] = "-"
                elif place2 == 19:
                    floor_2[4] = "-"
                elif place2 == 21:
                    floor_2[6] = "-"
                elif place2 == 29:
                    floor_3[0] = "-"
                elif place2 == 31:
                    floor_3[2] = "-"
                elif place2 == 33:
                    floor_3[4] = "-"
                elif place2 == 35:
                    floor_3[6] = "-"
                elif place2 == 43:
                    floor_4[0] = "-"
                elif place2 == 45:
                    floor_4[2] = "-"
                elif place2 == 47:
                    floor_4[4] = "-"
                elif place2 == 49:
                    floor_4[6] = "-"

                place2 = place2 - 14

                if place2 == 1:
                    floor_1[0] = "P"
                elif place2 == 3:
                    floor_1[2] = "P"
                elif place2 == 5:
                    floor_1[4] = "P"
                elif place2 == 7:
                    floor_1[6] = "P"
                elif place2 == 15:
                    floor_2[0] = "P"
                elif place2 == 17:
                    floor_2[2] = "P"
                elif place2 == 19:
                    floor_2[4] = "P"
                elif place2 == 21:
                    floor_2[6] = "P"
                elif place2 == 29:
                    floor_3[0] = "P"
                elif place2 == 31:
                    floor_3[2] = "P"
                elif place2 == 33:
                    floor_3[4] = "P"
                elif place2 == 35:
                    floor_3[6] = "P"

        elif action2.upper() == "S":
            if place2 == 43 or place2 == 45 or place2 == 47 or place2 == 49:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif out2 == place2 + 14 and items2 < 2:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif wall21 == place2 + 7 or wall22 == place2 + 7 or wall23 == place2 + 7 or wall24 == place2 + 7:
                print("~~~~~~~There's a wall in your way~~~~~~")
            else:
                if place2 == 1:
                    floor_1[0] = "-"
                elif place2 == 3:
                    floor_1[2] = "-"
                elif place2 == 5:
                    floor_1[4] = "-"
                elif place2 == 7:
                    floor_1[6] = "-"
                elif place2 == 15:
                    floor_2[0] = "-"
                elif place2 == 17:
                    floor_2[2] = "-"
                elif place2 == 19:
                    floor_2[4] = "-"
                elif place2 == 21:
                    floor_2[6] = "-"
                elif place2 == 29:
                    floor_3[0] = "-"
                elif place2 == 31:
                    floor_3[2] = "-"
                elif place2 == 33:
                    floor_3[4] = "-"
                elif place2 == 35:
                    floor_3[6] = "-"

                place2 = place2 + 14

                if place2 == 15:
                    floor_2[0] = "P"
                elif place2 == 17:
                    floor_2[2] = "P"
                elif place2 == 19:
                    floor_2[4] = "P"
                elif place2 == 21:
                    floor_2[6] = "P"
                elif place2 == 29:
                    floor_3[0] = "P"
                elif place2 == 31:
                    floor_3[2] = "P"
                elif place2 == 33:
                    floor_3[4] = "P"
                elif place2 == 35:
                    floor_3[6] = "P"
                elif place2 == 43:
                    floor_4[0] = "P"
                elif place2 == 45:
                    floor_4[2] = "P"
                elif place2 == 47:
                    floor_4[4] = "P"
                elif place2 == 49:
                    floor_4[6] = "P"

        if level == 2:
            print("~~~~~~~~| LEVEL", level, "|~~~~~~~~")
            print(*floor_1, sep="   ")
            print(*floor_1_2, sep="   ")
            print(*floor_2, sep="   ")
            print(*floor_2_2, sep="   ")
            print(*floor_3, sep="   ")
            print(*floor_3_2, sep="   ")
            print(*floor_4, sep="   ")

        if place2 == item21: 
            items2 = items2 + 1
            item21 = 0
            print("~~~~~~~~You got a key!~~~~~~~~")

        if place2 == item22:
            items2 = items2 + 1
            item22 = 0
            print("~~~~~~~~You got a key!~~~~~~~~")

        if items2 == 2 and place2 == out2:
            print("~~~~~~~~Level 2 completed!~~~~~~~~")
            level = level + 1
            break

if level == 3: #ENCOUNTER
    print("|||||||||MONSTER HAS APPEARED|||||||||")
    
    for a,b in options.items():
        print(a + ":", b)
    print("What shall you do?")
    do = input("")
    
    if do.upper() == "R": #RUN FROM ENCOUNTER
        chance = random.randrange(0, 2)
        if chance == 0:
            print("You got away!")
            level = level + 1
        elif chance == 1:
            print("You couldn't get away!")
    
    if do.upper() == "F" or chance == 1: #FIGHT
        monster_health = 10
        player_health = 10
        print("           --------------------")
        print("         |", health[monster_health], "|")
        print("           --------------------")
        print("                        MONSTER")
        print("                               ")
        print("                               ")
        print(" --------------------")
        print("|", health[player_health], "|")
        print(" --------------------")
        print(name.upper())
        monster_damage = 1
        monster_armor = 0
        while True: # BATTLE MECHANICS
            for m,n in fight.items():
                print(m + ":", n)
            print("What will you do?")
            battle = input("")
            
            crit_chance = random.randrange(0, 2)

            if battle == "1": #ATTACK
                if crit_chance == 1:
                    monster_health = monster_health - ((attack_damage * 2) - monster_armor)
                    print("--CRIT--")
                    print("You've delt", (attack_damage * 2) - monster_armor, "damage")
                else: 
                    monster_health = monster_health - (attack_damage - monster_armor)
                    print("You've delt", attack_damage - monster_armor, "damage")
            
            elif battle == "2": #BLOCK
                print("You are now blocking, next attack will do less damage")
            
            elif battle == "3": #ESCAPE
                chance = random.randrange(0, 2)
                if chance == 0:
                    print("You got away!")
                    level = level + 1
                    break
                elif chance == 1:
                    print("You couldn't get away!")
                    player_health = player_health - 1

            elif battle == "4": #ITEM
                if pocket == {}:
                    print("There's nothing")
                else:
                    for k,v in pocket:
                        print(k + ":", v)

            monster_attack = random.randrange(1, 3)

            if monster_health <= 0:
                monster_health = 0

            elif monster_attack == 1: #MONSTER ATTACK
                print("Monster attacks")
                if battle == "2":
                    if monster_damage >= 5:
                        print("The attack was too strong, you took half damage")
                        player_health == player_health - (monster_damage // 2)
                    else:
                        print("You've blocked the attack")
                elif monster_attack == 2:
                    player_health = player_health - monster_damage * 2
                else:
                    player_health = player_health - monster_damage
            
            elif monster_attack == 2: #MONSTER POWER UP
                print("The monster is charging up!")
            
            print("           --------------------")
            print("         |", health[monster_health], "|")
            print("           --------------------")
            print("                        MONSTER")
            print("                               ")
            print("                               ")
            print(" --------------------")
            print("|", health[player_health], "|")
            print(" --------------------")
            print(name.upper())
            
            if monster_health == 0:
                print("You've killed the monster!")
                print("LEVEL UP!")
                print("Unlocked Attack UP skill!")
                level = level + 1
                break

            elif player_health == 0:
                print("You died!")
                break
            
if level == 4: #HIDDEN ITEM
    floor_1 = ["-", " ", "-", " ", "-", " ", "-"]
    floor_1_2 = [" ", " ", " ", " ", " ", " ", " "]
    floor_2 = ["-", " ", "-", " ", "-", " ", "-"]
    floor_2_2 = [" ", " ", " ", " ", " ", " ", " "]
    floor_3 = ["-", " ", "-", " ", "-", " ", "-"]
    floor_3_2 = [" ", " ", " ", " ", " ", " ", " "]
    floor_4 = ["-", " ", "-", " ", "-", " ", "-"]

    l2 = list(range(1,50))
    l2.remove(8)
    l2.remove(9)
    l2.remove(10)
    l2.remove(11)
    l2.remove(12)
    l2.remove(13)
    l2.remove(14)
    l2.remove(22)
    l2.remove(23)
    l2.remove(24)
    l2.remove(25)
    l2.remove(26)
    l2.remove(27)
    l2.remove(28)
    l2.remove(36)
    l2.remove(37)
    l2.remove(38)
    l2.remove(39)
    l2.remove(40)
    l2.remove(41)
    l2.remove(42)

    walls2 = []
    places2 = []

    for num1 in l2: #GENERATOR FOR WALLS
        if num1 in range(1, 8): 
            if num1 % 2 == 0: 
                walls2.append(num1)
        if num1 in range(15, 22):
            if num1 % 2 == 0:
                walls2.append(num1)
        if num1 in range(29, 36):
            if num1 % 2 == 0: 
                walls2.append(num1)
        if num1 in range(43, 50):
            if num1 % 2 == 0: 
                walls2.append(num1)

    walls2.append(8)
    walls2.append(9)
    walls2.append(10)
    walls2.append(11)
    walls2.append(12)
    walls2.append(13)
    walls2.append(14)
    walls2.append(22)
    walls2.append(23)
    walls2.append(24)
    walls2.append(25)
    walls2.append(26)
    walls2.append(27)
    walls2.append(28)
    walls2.append(36)
    walls2.append(37)
    walls2.append(38)
    walls2.append(39)
    walls2.append(40)
    walls2.append(41)
    walls2.append(42)

    for num2 in l2: #GENERATOR FOR OTHERS
        if num2 in range(1, 8): 
            if num2 % 2 != 0: 
                places2.append(num2)
        if num2 in range(15, 22):
            if num2 % 2 != 0:
                places2.append(num2)
        if num2 in range(29, 36):
            if num2 % 2 != 0: 
                places2.append(num2)
        if num2 in range(43, 50):
            if num2 % 2 != 0: 
                places2.append(num2)

    wall21 = random.choice(walls2)
    walls2.remove(wall21)
    wall22 = random.choice(walls2)
    walls2.remove(wall22)
    wall23 = random.choice(walls2)
    walls2.remove(wall23)
    wall24 = random.choice(walls2)
    walls2.remove(wall24)

    place2 = random.choice(places2)
    places2.remove(place2)
    item21 = random.choice(places2)
    places2.remove(item21)
    item22 = random.choice(places2)
    places2.remove(item22)
    out2 = random.choice(places2)
    places2.remove(out2)
    hidden = random.choice(places2)
    items2 = 0

    if wall21 == 2:
        floor_1[1] = "W"
    elif wall21 == 4:
        floor_1[3] = "W"
    elif wall21 == 6:
        floor_1[5] = "W"
    elif wall21 == 8:
        floor_1_2[0] = "W"
    elif wall21 == 10:
        floor_1_2[2] = "W"
    elif wall21 == 12:
        floor_1_2[4] = "W"
    elif wall21 == 14:
        floor_1_2[6] = "W"
    elif wall21 == 16:
        floor_2[1] = "W"
    elif wall21 == 18:
        floor_2[3] = "W"
    elif wall21 == 20:
        floor_2[5] = "W"
    elif wall21 == 22:
        floor_2_2[0] = "W"
    elif wall21 == 24:
        floor_2_2[2] = "W"
    elif wall21 == 26:
        floor_2_2[4] = "W"
    elif wall21 == 28:
        floor_2_2[6] = "W"
    elif wall21 == 30:
        floor_3[1] = "W"
    elif wall21 == 32:
        floor_3[3] = "W"
    elif wall21 == 34:
        floor_3[5] = "W"
    elif wall21 == 36:
        floor_3_2[0] = "W"
    elif wall21 == 38:
        floor_3_2[2] = "W"
    elif wall21 == 40:
        floor_3_2[4] = "W"
    elif wall21 == 42:
        floor_3_2[6] = "W"
    elif wall21 == 44:
        floor_4[1] = "W"
    elif wall21 == 46:
        floor_4[3] = "W"
    elif wall21 == 48:
        floor_4[5] = "W"

    if wall22 == 2:
        floor_1[1] = "W"
    elif wall22 == 4:
        floor_1[3] = "W"
    elif wall22 == 6:
        floor_1[5] = "W"
    elif wall22 == 8:
        floor_1_2[0] = "W"
    elif wall22 == 10:
        floor_1_2[2] = "W"
    elif wall22 == 12:
        floor_1_2[4] = "W"
    elif wall22 == 14:
        floor_1_2[6] = "W"
    elif wall22 == 16:
        floor_2[1] = "W"
    elif wall22 == 18:
        floor_2[3] = "W"
    elif wall22 == 20:
        floor_2[5] = "W"
    elif wall22 == 22:
        floor_2_2[0] = "W"
    elif wall22 == 24:
        floor_2_2[2] = "W"
    elif wall22 == 26:
        floor_2_2[4] = "W"
    elif wall22 == 28:
        floor_2_2[6] = "W"
    elif wall22 == 30:
        floor_3[1] = "W"
    elif wall22 == 32:
        floor_3[3] = "W"
    elif wall22 == 34:
        floor_3[5] = "W"
    elif wall22 == 36:
        floor_3_2[0] = "W"
    elif wall22 == 38:
        floor_3_2[2] = "W"
    elif wall22 == 40:
        floor_3_2[4] = "W"
    elif wall22 == 42:
        floor_3_2[6] = "W"
    elif wall22 == 44:
        floor_4[1] = "W"
    elif wall22 == 46:
        floor_4[3] = "W"
    elif wall22 == 48:
        floor_4[5] = "W"

    if wall23 == 2:
        floor_1[1] = "W"
    elif wall23 == 4:
        floor_1[3] = "W"
    elif wall23 == 6:
        floor_1[5] = "W"
    elif wall23 == 8:
        floor_1_2[0] = "W"
    elif wall23 == 10:
        floor_1_2[2] = "W"
    elif wall23 == 12:
        floor_1_2[4] = "W"
    elif wall23 == 14:
        floor_1_2[6] = "W"
    elif wall23 == 16:
        floor_2[1] = "W"
    elif wall23 == 18:
        floor_2[3] = "W"
    elif wall23 == 20:
        floor_2[5] = "W"
    elif wall23 == 22:
        floor_2_2[0] = "W"
    elif wall23 == 24:
        floor_2_2[2] = "W"
    elif wall23 == 26:
        floor_2_2[4] = "W"
    elif wall23 == 28:
        floor_2_2[6] = "W"
    elif wall23 == 30:
        floor_3[1] = "W"
    elif wall23 == 32:
        floor_3[3] = "W"
    elif wall23 == 34:
        floor_3[5] = "W"
    elif wall23 == 36:
        floor_3_2[0] = "W"
    elif wall23 == 38:
        floor_3_2[2] = "W"
    elif wall23 == 40:
        floor_3_2[4] = "W"
    elif wall23 == 42:
        floor_3_2[6] = "W"
    elif wall23 == 44:
        floor_4[1] = "W"
    elif wall23 == 46:
        floor_4[3] = "W"
    elif wall23 == 48:
        floor_4[5] = "W"

    if wall24 == 2:
        floor_1[1] = "W"
    elif wall24 == 4:
        floor_1[3] = "W"
    elif wall24 == 6:
        floor_1[5] = "W"
    elif wall24 == 8:
        floor_1_2[0] = "W"
    elif wall24 == 10:
        floor_1_2[2] = "W"
    elif wall24 == 12:
        floor_1_2[4] = "W"
    elif wall24 == 14:
        floor_1_2[6] = "W"
    elif wall24 == 16:
        floor_2[1] = "W"
    elif wall24 == 18:
        floor_2[3] = "W"
    elif wall24 == 20:
        floor_2[5] = "W"
    elif wall24 == 22:
        floor_2_2[0] = "W"
    elif wall24 == 24:
        floor_2_2[2] = "W"
    elif wall24 == 26:
        floor_2_2[4] = "W"
    elif wall24 == 28:
        floor_2_2[6] = "W"
    elif wall24 == 30:
        floor_3[1] = "W"
    elif wall24 == 32:
        floor_3[3] = "W"
    elif wall24 == 34:
        floor_3[5] = "W"
    elif wall24 == 36:
        floor_3_2[0] = "W"
    elif wall24 == 38:
        floor_3_2[2] = "W"
    elif wall24 == 40:
        floor_3_2[4] = "W"
    elif wall24 == 42:
        floor_3_2[6] = "W"
    elif wall24 == 44:
        floor_4[1] = "W"
    elif wall24 == 46:
        floor_4[3] = "W"
    elif wall24 == 48:
        floor_4[5] = "W"

    if place2 == 1:
        floor_1[0] = "P"
    elif place2 == 3:
        floor_1[2] = "P"
    elif place2 == 5:
        floor_1[4] = "P"
    elif place2 == 7:
        floor_1[6] = "P"
    elif place2 == 15:
        floor_2[0] = "P"
    elif place2 == 17:
        floor_2[2] = "P"
    elif place2 == 19:
        floor_2[4] = "P"
    elif place2 == 21:
        floor_2[6] = "P"
    elif place2 == 29:
        floor_3[0] = "P"
    elif place2 == 31:
        floor_3[2] = "P"
    elif place2 == 33:
        floor_3[4] = "P"
    elif place2 == 35:
        floor_3[6] = "P"
    elif place2 == 43:
        floor_4[0] = "P"
    elif place2 == 45:
        floor_4[2] = "P"
    elif place2 == 47:
        floor_4[4] = "P"
    elif place2 == 49:
        floor_4[6] = "P"

    if item21 == 1:
        floor_1[0] = "K"
    elif item21 == 3:
        floor_1[2] = "K"
    elif item21 == 5:
        floor_1[4] = "K"
    elif item21 == 7:
        floor_1[6] = "K"
    elif item21 == 15:
        floor_2[0] = "K"
    elif item21 == 17:
        floor_2[2] = "K"
    elif item21 == 19:
        floor_2[4] = "K"
    elif item21 == 21:
        floor_2[6] = "K"
    elif item21 == 29:
        floor_3[0] = "K"
    elif item21 == 31:
        floor_3[2] = "K"
    elif item21 == 33:
        floor_3[4] = "K"
    elif item21 == 35:
        floor_3[6] = "K"
    elif item21 == 43:
        floor_4[0] = "K"
    elif item21 == 45:
        floor_4[2] = "K"
    elif item21 == 47:
        floor_4[4] = "K"
    elif item21 == 49:
        floor_4[6] = "K"

    if item22 == 1:
        floor_1[0] = "K"
    elif item22 == 3:
        floor_1[2] = "K"
    elif item22 == 5:
        floor_1[4] = "K"
    elif item22 == 7:
        floor_1[6] = "K"
    elif item22 == 15:
        floor_2[0] = "K"
    elif item22 == 17:
        floor_2[2] = "K"
    elif item22 == 19:
        floor_2[4] = "K"
    elif item22 == 21:
        floor_2[6] = "K"
    elif item22 == 29:
        floor_3[0] = "K"
    elif item22 == 31:
        floor_3[2] = "K"
    elif item22 == 33:
        floor_3[4] = "K"
    elif item22 == 35:
        floor_3[6] = "K"
    elif item22 == 43:
        floor_4[0] = "K"
    elif item22 == 45:
        floor_4[2] = "K"
    elif item22 == 47:
        floor_4[4] = "K"
    elif item22 == 49:
        floor_4[6] = "K"

    if out2 == 1:
        floor_1[0] = "E"
    elif out2 == 3:
        floor_1[2] = "E"
    elif out2 == 5:
        floor_1[4] = "E"
    elif out2 == 7:
        floor_1[6] = "E"
    elif out2 == 15:
        floor_2[0] = "E"
    elif out2 == 17:
        floor_2[2] = "E"
    elif out2 == 19:
        floor_2[4] = "E"
    elif out2 == 21:
        floor_2[6] = "E"
    elif out2 == 29:
        floor_3[0] = "E"
    elif out2 == 31:
        floor_3[2] = "E"
    elif out2 == 33:
        floor_3[4] = "E"
    elif out2 == 35:
        floor_3[6] = "E"
    elif out2 == 43:
        floor_4[0] = "E"
    elif out2 == 45:
        floor_4[2] = "E"
    elif out2 == 47:
        floor_4[4] = "E"
    elif out2 == 49:
        floor_4[6] = "E"

    if hidden == 1:
        floor_1[0] = "*"
    elif hidden == 3:
        floor_1[2] = "*"
    elif hidden == 5:
        floor_1[4] = "*"
    elif hidden == 7:
        floor_1[6] = "*"
    elif hidden == 15:
        floor_2[0] = "*"
    elif hidden == 17:
        floor_2[2] = "*"
    elif hidden == 19:
        floor_2[4] = "*"
    elif hidden == 21:
        floor_2[6] = "*"
    elif hidden == 29:
        floor_3[0] = "*"
    elif hidden == 31:
        floor_3[2] = "*"
    elif hidden == 33:
        floor_3[4] = "*"
    elif hidden == 35:
        floor_3[6] = "*"
    elif hidden == 43:
        floor_4[0] = "*"
    elif hidden == 45:
        floor_4[2] = "*"
    elif hidden == 47:
        floor_4[4] = "*"
    elif hidden == 49:
        floor_4[6] = "*"

    print("~~~~~~~~| LEVEL", level, "|~~~~~~~~")

    print(*floor_1, sep="   ")
    print(*floor_1_2, sep="   ")
    print(*floor_2, sep="   ")
    print(*floor_2_2, sep="   ")
    print(*floor_3, sep="   ")
    print(*floor_3_2, sep="   ")
    print(*floor_4, sep="   ")

    while True: #MOVEMENT CONTROLS FOR LVL 4
        for k,v in actions.items():
            print(k + ":", v)
        print("What would you like to do?")
        action2 = input("")

        if action2.upper() == "X":
            print("~~~~~~~~Cya later!~~~~~~~~~~")
            break
            
        elif action2.upper() == "D":
            if place2 == 7 or place2 == 21 or place2 == 35 or place2 == 49:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif out2 == place2 + 2 and items2 < 2:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif wall21 == place2 + 1 or wall22 == place2 + 1 or wall23 == place2 + 1 or wall24 == place2 + 1:
                print("~~~~~~~There's a wall in your way~~~~~~")
            else:
                if place2 == 1:
                    floor_1[0] = "-"
                elif place2 == 3:
                    floor_1[2] = "-"
                elif place2 == 5:
                    floor_1[4] = "-"
                elif place2 == 15:
                    floor_2[0] = "-"
                elif place2 == 17:
                    floor_2[2] = "-"
                elif place2 == 19:
                    floor_2[4] = "-"
                elif place2 == 29:
                    floor_3[0] = "-"
                elif place2 == 31:
                    floor_3[2] = "-"
                elif place2 == 33:
                    floor_3[4] = "-"
                elif place2 == 43:
                    floor_4[0] = "-"
                elif place2 == 45:
                    floor_4[2] = "-"
                elif place2 == 47:
                    floor_4[4] = "-"
                        
                place2 = place2 + 2

                if place2 == 3:
                    floor_1[2] = "P"
                elif place2 == 5:
                    floor_1[4] = "P"
                elif place2 == 7:
                    floor_1[6] = "P"
                elif place2 == 17:
                    floor_2[2] = "P"
                elif place2 == 19:
                    floor_2[4] = "P"
                elif place2 == 21:
                    floor_2[6] = "P"
                elif place2 == 31:
                    floor_3[2] = "P"
                elif place2 == 33:
                    floor_3[4] = "P"
                elif place2 == 35:
                    floor_3[6] = "P"
                elif place2 == 45:
                    floor_4[2] = "P"
                elif place2 == 47:
                    floor_4[4] = "P"
                elif place2 == 49:
                    floor_4[6] = "P"

        elif action2.upper() == "A":
            if place2 == 1 or place2 == 15 or place2 == 29 or place2 == 43:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif out2 == place2 - 2 and items2 < 2:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif wall21 == place2 - 1 or wall22 == place2 - 1 or wall23 == place2 - 1 or wall24 == place2 - 1:
                print("~~~~~~~There's a wall in your way~~~~~~")
            else:
                if place2 == 3:
                    floor_1[2] = "-"
                elif place2 == 5:
                    floor_1[4] = "-"
                elif place2 == 7:
                    floor_1[6] = "-"
                elif place2 == 17:
                    floor_2[2] = "-"
                elif place2 == 19:
                    floor_2[4] = "-"
                elif place2 == 21:
                    floor_2[6] = "-"
                elif place2 == 31:
                    floor_3[2] = "-"
                elif place2 == 33:
                    floor_3[4] = "-"
                elif place2 == 35:
                    floor_3[6] = "-"
                elif place2 == 45:
                    floor_4[2] = "-"
                elif place2 == 47:
                    floor_4[4] = "-"
                elif place2 == 49:
                    floor_4[6] = "-"
                
                place2 = place2 - 2
                
                if place2 == 1:
                    floor_1[0] = "P"
                elif place2 == 3:
                    floor_1[2] = "P"
                elif place2 == 5:
                    floor_1[4] = "P"
                elif place2 == 15:
                    floor_2[0] = "P"
                elif place2 == 17:
                    floor_2[2] = "P"
                elif place2 == 19:
                    floor_2[4] = "P"
                elif place2 == 29:
                    floor_3[0] = "P"
                elif place2 == 31:
                    floor_3[2] = "P"
                elif place2 == 33:
                    floor_3[4] = "P"
                elif place2 == 43:
                    floor_4[0] = "P"
                elif place2 == 45:
                    floor_4[2] = "P"
                elif place2 == 47:
                    floor_4[4] = "P"

        elif action2.upper() == "W":
            if place2 == 1 or place2 == 3 or place2 == 5 or place2 == 7:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif out2 == place2 - 14 and items2 < 2:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif wall21 == place2 - 7 or wall22 == place2 - 7 or wall23 == place2 - 7 or wall24 == place2 - 7:
                print("~~~~~~~There's a wall in your way~~~~~~")
            else:
                if place2 == 15:
                    floor_2[0] = "-"
                elif place2 == 17:
                    floor_2[2] = "-"
                elif place2 == 19:
                    floor_2[4] = "-"
                elif place2 == 21:
                    floor_2[6] = "-"
                elif place2 == 29:
                    floor_3[0] = "-"
                elif place2 == 31:
                    floor_3[2] = "-"
                elif place2 == 33:
                    floor_3[4] = "-"
                elif place2 == 35:
                    floor_3[6] = "-"
                elif place2 == 43:
                    floor_4[0] = "-"
                elif place2 == 45:
                    floor_4[2] = "-"
                elif place2 == 47:
                    floor_4[4] = "-"
                elif place2 == 49:
                    floor_4[6] = "-"

                place2 = place2 - 14

                if place2 == 1:
                    floor_1[0] = "P"
                elif place2 == 3:
                    floor_1[2] = "P"
                elif place2 == 5:
                    floor_1[4] = "P"
                elif place2 == 7:
                    floor_1[6] = "P"
                elif place2 == 15:
                    floor_2[0] = "P"
                elif place2 == 17:
                    floor_2[2] = "P"
                elif place2 == 19:
                    floor_2[4] = "P"
                elif place2 == 21:
                    floor_2[6] = "P"
                elif place2 == 29:
                    floor_3[0] = "P"
                elif place2 == 31:
                    floor_3[2] = "P"
                elif place2 == 33:
                    floor_3[4] = "P"
                elif place2 == 35:
                    floor_3[6] = "P"

        elif action2.upper() == "S":
            if place2 == 43 or place2 == 45 or place2 == 47 or place2 == 49:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif out2 == place2 + 14 and items2 < 2:
                print("~~~~~~~You can't do that~~~~~~~~")
            elif wall21 == place2 + 7 or wall22 == place2 + 7 or wall23 == place2 + 7 or wall24 == place2 + 7:
                print("~~~~~~~There's a wall in your way~~~~~~")
            else:
                if place2 == 1:
                    floor_1[0] = "-"
                elif place2 == 3:
                    floor_1[2] = "-"
                elif place2 == 5:
                    floor_1[4] = "-"
                elif place2 == 7:
                    floor_1[6] = "-"
                elif place2 == 15:
                    floor_2[0] = "-"
                elif place2 == 17:
                    floor_2[2] = "-"
                elif place2 == 19:
                    floor_2[4] = "-"
                elif place2 == 21:
                    floor_2[6] = "-"
                elif place2 == 29:
                    floor_3[0] = "-"
                elif place2 == 31:
                    floor_3[2] = "-"
                elif place2 == 33:
                    floor_3[4] = "-"
                elif place2 == 35:
                    floor_3[6] = "-"

                place2 = place2 + 14

                if place2 == 15:
                    floor_2[0] = "P"
                elif place2 == 17:
                    floor_2[2] = "P"
                elif place2 == 19:
                    floor_2[4] = "P"
                elif place2 == 21:
                    floor_2[6] = "P"
                elif place2 == 29:
                    floor_3[0] = "P"
                elif place2 == 31:
                    floor_3[2] = "P"
                elif place2 == 33:
                    floor_3[4] = "P"
                elif place2 == 35:
                    floor_3[6] = "P"
                elif place2 == 43:
                    floor_4[0] = "P"
                elif place2 == 45:
                    floor_4[2] = "P"
                elif place2 == 47:
                    floor_4[4] = "P"
                elif place2 == 49:
                    floor_4[6] = "P"

        if level == 4:
            print("~~~~~~~~| LEVEL", level, "|~~~~~~~~")
            print(*floor_1, sep="   ")
            print(*floor_1_2, sep="   ")
            print(*floor_2, sep="   ")
            print(*floor_2_2, sep="   ")
            print(*floor_3, sep="   ")
            print(*floor_3_2, sep="   ")
            print(*floor_4, sep="   ")

        if place2 == item21: 
            items2 = items2 + 1
            item21 = 0
            print("~~~~~~~~You got a key!~~~~~~~~")

        if place2 == hidden:
            healthpot = 0
            healthpot = healthpot + 1
            pocket["healthpot"] = healthpot
            print("You found a secret health potion!")

        if place2 == item22:
            items2 = items2 + 1
            item22 = 0
            print("~~~~~~~~You got a key!~~~~~~~~")

        if items2 == 2 and place2 == out2:
            print("~~~~~~~~Level 2 completed!~~~~~~~~")
            level = level + 1
            break

if level == 5: #MONSTER WITH ITEMS
    print("|||||||||MONSTER HAS APPEARED|||||||||")
    
    for a,b in options.items():
        print(a + ":", b)
    print("What shall you do?")
    do = input("")
    
    if do.upper() == "R": #RUN FROM ENCOUNTER
        chance = random.randrange(0, 2)
        if chance == 0:
            print("You got away!")
            level = level + 1
        elif chance == 1:
            print("You couldn't get away!")
    
    if do.upper() == "F" or chance == 1: #FIGHT
        monster_health = 10
        player_health = 10
        print("           --------------------")
        print("         |", health[monster_health], "|")
        print("           --------------------")
        print("                        MONSTER")
        print("                               ")
        print("                               ")
        print(" --------------------")
        print("|", health[player_health], "|")
        print(" --------------------")
        print(name.upper())
        monster_damage = 1
        monster_armor = 0
        while True: # BATTLE MECHANICS
            for m,n in fight.items():
                print(m + ":", n)
            print("What will you do?")
            battle = input("")
            
            crit_chance = random.randrange(0, 2)

            if battle == "1": #ATTACK
                if crit_chance == 1:
                    monster_health = monster_health - ((attack_damage * 2) - monster_armor)
                    print("--CRIT--")
                    print("You've delt", (attack_damage * 2) - monster_armor, "damage")
                else: 
                    monster_health = monster_health - (attack_damage - monster_armor)
                    print("You've delt", attack_damage - monster_armor, "damage")
            
            elif battle == "2": #BLOCK
                print("You are now blocking, next attack will do less damage")
            
            elif battle == "3": #ESCAPE
                chance = random.randrange(0, 2)
                if chance == 0:
                    print("You got away!")
                    level = level + 1
                    break
                elif chance == 1:
                    print("You couldn't get away!")
                    player_health = player_health - 1

            elif battle == "4": #ITEM
                if pocket == {}:
                    print("There's nothing")
                else:
                    for o,q in pocket.items():
                        print(o + ":", q)
                    print("Which item?")
                    choice = input("")
                    if choice == "health":
                        if player_health == 10:
                            print("Your fully healed")
                        else:
                            healthpot = healthpot - 1
                            if healthpot == 0:
                                del pocket["healthpot"]
                            player_health = player_health + 2
                            if player_health >= 10:
                                player_health = 10
                        

            print("           --------------------")
            print("         |", health[monster_health], "|")
            print("           --------------------")
            print("                        MONSTER")
            print("                               ")
            print("                               ")
            print(" --------------------")
            print("|", health[player_health], "|")
            print(" --------------------")
            print(name.upper())
            
            monster_attack = random.randrange(1, 3)

            if monster_health <= 0:
                monster_health = 0

            elif monster_attack == 1: #MONSTER ATTACK
                print("Monster attacks")
                if battle == "2":
                    if monster_damage >= 5:
                        print("The attack was too strong, you took half damage")
                        player_health == player_health - (monster_damage // 2)
                    else:
                        print("You've blocked the attack")
                elif monster_attack == 2:
                    player_health = player_health - monster_damage * 2
                else:
                    player_health = player_health - monster_damage
            
            elif monster_attack == 2: #MONSTER POWER UP
                print("The monster is charging up!")
            
            print("           --------------------")
            print("         |", health[monster_health], "|")
            print("           --------------------")
            print("                        MONSTER")
            print("                               ")
            print("                               ")
            print(" --------------------")
            print("|", health[player_health], "|")
            print(" --------------------")
            print(name.upper())
            
            if monster_health == 0:
                print("You've killed the monster!")
                print("LEVEL UP!")
                print("Unlocked Attack UP skill!")
                level = level + 1
                break

            elif player_health == 0:
                print("You died!")
                break
    