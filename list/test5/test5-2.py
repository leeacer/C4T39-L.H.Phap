items = ["Overwatch", "Candy", "Persona"]
print(*items, sep=" | ")
items.append("Hot anime bois")
print(*items, sep=" | ")
items[0] = "Marvel"
items[-1] = "Fruit Robo"
print(*items, sep=" | ")