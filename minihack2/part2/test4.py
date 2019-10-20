lists = ["red", "blue", "green", "yellow"]
position = int(input("Which one would you like to see: "))
if position > len(lists) - 1:
    print("That's not possible")
else:
    print(lists[position - 1])