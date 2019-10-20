computers = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}

for k,v in computers.items():
    print(k + ":", v)
print("----------------------------------------------------------------")

computers["FUJITSU"] = 15
computers["ALIENWARE"] = 5

for k,v in computers.items():
    print(k + ":", v)