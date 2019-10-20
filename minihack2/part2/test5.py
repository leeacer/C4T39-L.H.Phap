lists = ["red", "blue", "green", "yellow"]
for i in range(len(lists)):
    print(i + 1,lists[i])
delete = input("Which one do you want to delete: ")
if delete.isdigit():
    if int(delete) > len(lists):
        print("That does not exist in this list")
    else:
        lists.pop(int(delete)-1)
        for i in range(len(lists)):
            print(i + 1,lists[i])
else:
    if delete == "red" or delete == "blue" or delete == "green" or delete == "yellow":
        lists.remove(delete)
        for i in range(len(lists)):
            print(i + 1,lists[i])
    else:
        print("That's is not on the list")