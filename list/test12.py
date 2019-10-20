lists = []
while True:
    print("|||||What would you like to do to the list?|||||")
    option = input("C      R      U      D  or  done:     ")
    if option == "c":
        add = input("What would you like to add to the list: ")
        lists.append(add)
        for i in range(len(lists)):
            print(lists[i])
    elif option == "r":
        if lists == []:
            print("|||||There's nothing in the list|||||")
        else:
            for i in range(len(lists)):
                print(lists[i])
    elif option == "u":
        if lists == []:
            print("|||||There's nothing in the list|||||")
        else:
            position = int(input("Where do you want to change: "))
            if position > len(lists) - 1:
                print("|||||That does not exist in this list|||||")
            else:
                thing = input("What would you like to add: ")
                lists[position] = thing
                for i in range(len(lists)):
                    print(lists[i])
    elif option == "d":
        if lists == []:
            print("|||||There's nothing in the list|||||")
        else:
            if position > len(lists) - 1:
                print("|||||That does not exist in this list|||||")
            else:
                delete = int(input("Which one do you want to delete: "))
                lists.pop(delete)
                for i in range(len(lists)):
                    print(lists[i])
    elif option == "done":
        for i in range(len(lists)):
            print(lists[i])
        break
    else:
        print("|||||That's not a valid option|||||")