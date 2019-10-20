import random
item = ["Genji", "Lucio", "Ana", "Zenyatta", "Baptiste"]
rd = random.choice(item)
shuffle = random.sample(rd,len(rd))
print(*shuffle)
answer = input("What is this word: ")
if answer == rd.lower():
    print(rd)
    print("That's correct")
else:
    print(rd)
    print("That's in correct")