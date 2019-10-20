items = ["Overwatch", "Candy", "Persona"]
print(*items, sep=" | ")
items.append("Hot anime bois")
print(*items, sep=" | ")
items[0] = "Marvel"
items[-1] = "Fruit Robo"
number = int(input("Enter the part: "))
change = input("What do you want to change it to: ")
items[number] = change
print(*items, sep=" | ")