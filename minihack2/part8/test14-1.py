highscore = [9999, 9, 1223, 122222222222]
highscore.sort(reverse = True)  
for i in highscore:
    print(highscore.index(i) + 1, i)