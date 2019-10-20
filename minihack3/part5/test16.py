computers = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}

computers["TOSHIBA"] = 10
computers["DELL"] = computers["DELL"] + 10
computers["MACBOOK"] = computers["MACBOOK"] - 2
computers["FUJITSU"] = 15
computers["ALIENWARE"] = 5

for k,v in computers.items():
    print(k + ":", v)

order = input("Which one would you like to order: ")
while True:
    number = int(input("How many: "))
    if number > computers[order.upper()]:
        print("We don't have enough in stock")
    else:
        break

computers[order.upper()] = computers[order.upper()] - number

for k,v in computers.items():
    print(k + ":", v)