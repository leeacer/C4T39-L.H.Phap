price = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 12000,
    "ASUS" : 400,
    "ACER" : 350,
    "TOSHIBA" : 600,
    "FUJITSU" : 900,
    "ALIENWARE" : 1000,
}

company = input("Which computer: ")
number = int(input("How many: "))

print(price[company.upper()] * number)