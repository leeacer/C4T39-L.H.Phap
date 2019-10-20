lists = ["red", "blue", "green", "yellow"]
print(*lists, sep=", ")
new = input("Add a new color: ")
lists.append(new)
print(*lists, sep=", ")