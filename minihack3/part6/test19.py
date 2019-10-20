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

prices = {

}
for k,v in computers.items():
    prices[k] = computers[k] * price[k]

print(sum(prices.values()))