month = int(input("What month it is: "))

if month == 1 or month == 11 or month == 12:
    print("It's winter")
elif month == 2 or month == 3 or month == 4:
    print("It's spring")
elif month == 5 or month == 6 or month == 7:
    print("It's summer")
elif month == 8 or month == 9 or month == 10:
    print("It's autumm")
else:
    print("Invalid month")