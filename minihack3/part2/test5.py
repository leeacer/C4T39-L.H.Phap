computers = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}

for k,v in computers.items():
    print(k + ":", v)

computer = input("Which type of computer do you want to add: ")
number = int(input("How many are in storage: "))

computers[computer.upper()] = number

for k,v in computers.items():
    print(k + ":", v)