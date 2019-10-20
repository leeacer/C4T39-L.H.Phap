numbers = ["10", "69", "420", "21", "360"]
find = input("Enter a number: ")
if find in numbers:
    position = numbers.index(find) + 1
    print("That's in position", position)
else:
    print("That's not on the list")