items = ["Overwatch", "Candy", "Persona"]
print(*items, sep=" | ")
items.append("Hot anime bois")
print(*items, sep=" | ")
items.pop(1)
print(*items, sep=" | ")