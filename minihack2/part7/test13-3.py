highscore = [9999, 9, 1223, 122222222222]
for i in highscore:
    print(highscore.index(i) + 1, i)
new = int(input("Enter your new highscore: "))
highscore.append(new)
for i in highscore:
    print(highscore.index(i) + 1, i)