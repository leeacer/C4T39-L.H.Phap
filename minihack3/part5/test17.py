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

while True:
    order, number = input("Which one and how many: ").split()
    if int(number) > computers[order.upper()]:
        print("We don't have enough in stock")
    else:
        break

computers[order.upper()] = computers[order.upper()] - int(number)

for k,v in computers.items():
    print(k + ":", v)