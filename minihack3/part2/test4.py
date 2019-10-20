computers = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}

for k,v in computers.items():
    print(k + ":", v)
print("----------------------------------------------------------------")

computers["TOSHIBA"] = 10

for k,v in computers.items():
    print(k + ":", v)