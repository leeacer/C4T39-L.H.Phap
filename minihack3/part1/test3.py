computers = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}

for i in computers:
    print(i)

types = input("Which computer would you like to see: ")

if types.upper() == list(computers.keys())[0]:
    print(list(computers.keys())[0] + ":", computers["HP"])
elif types.upper() == list(computers.keys())[1]:
    print(list(computers.keys())[1] + ":", computers["HP"])
elif types.upper() == list(computers.keys())[2]:
    print(list(computers.keys())[2] + ":", computers["HP"])
elif types.upper() == list(computers.keys())[3]:
    print(list(computers.keys())[3] + ":", computers["HP"])