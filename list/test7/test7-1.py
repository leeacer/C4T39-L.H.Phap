items = ["Overwatch", "Candy", "Persona"]
print(*items, sep=" | ")
items.append("Hot anime bois")
print(*items, sep=" | ")
number = int(input("Which one would you like to delete: "))
if number >= -4 and number <= 3:
    items.pop(number)
    print(*items, sep=" | ")
else:
    print("That does not exist in this list")