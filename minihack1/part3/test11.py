month = int(input("Enter a month: "))
flag = month%2
if month >= 1 and month < 8:
    if month == 2:
        print("month",month,"has either 28 or 29 days")
    elif month == 1 and month > 2:
        print("month",month,"has 30 days")
    else:
        print("month",month,"has 31 days")
elif month >= 8 and month < 13:
    if flag == 0:
        print("month",month,"has 31 days")
    else:
        print("month",month,"has 30 days")
else:
    print("that month is invalid")