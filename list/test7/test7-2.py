items = ["Overwatch", "Candy", "Persona"]
print(*items, sep=" | ")
items.append("Hot anime bois")
print(*items, sep=" | ")
number = input("Which one would you like to delete: ")
if number == "Overwatch" or number == "Candy" or number == "Persona" or number == "Hot anime bois":
    items.remove(number)
    print(*items, sep=" | ")
else:
    print("That does not exist in this list")