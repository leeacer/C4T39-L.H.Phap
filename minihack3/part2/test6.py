computers = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}

for k,v in computers.items():
    print(k + ":", v)
print("----------------------------------------------------------------")

computers["DELL"] = 50 + 10
computers["MACBOOK"] = 12 - 2

for k,v in computers.items():
    print(k + ":", v)